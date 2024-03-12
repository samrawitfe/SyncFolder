import os
import shutil
import logging
from pathlib import Path
from filecmp import dircmp


def replicate_symlink(source_path, replica_path):
    """Replicates a symbolic link."""
    try:
        target_path = os.readlink(source_path)
        if replica_path.exists():
            replica_path.unlink()
        os.symlink(target_path, replica_path)
        shutil.copystat(source_path, replica_path, follow_symlinks=False)
        logging.info(f"Created symbolic link {replica_path} -> {target_path}")
    except OSError as e:
        logging.error(f"Error replicating symbolic link {source_path} -> {replica_path}: {e}")


def sync_directories(source_dir, replica_dir):
    """
    Synchronize contents from source_dir to replica_dir.
    """
    source_dir = Path(source_dir)
    replica_dir = Path(replica_dir)

    try:
        dir_cmp = dircmp(source_dir, replica_dir)
    except OSError as e:
        logging.error(f"Error comparing directories {source_dir} and {replica_dir}: {e}")
        return

    for filename in dir_cmp.left_only + dir_cmp.diff_files:
        source_path = source_dir / filename
        replica_path = replica_dir / filename

        if source_path.is_symlink():
            replicate_symlink(source_path, replica_path)
        elif source_path.is_dir():
            if not replica_path.exists():
                os.makedirs(replica_path)
            shutil.copystat(source_path, replica_path)
            logging.info(f"Created directory {replica_path} with preserved permissions")

        else:
            shutil.copy2(source_path, replica_path)
            logging.info(f"Copied file {source_path} to {replica_path} with preserved permissions")

    for filename in dir_cmp.right_only:
        replica_path = replica_dir / filename
        if replica_path.is_dir():
            shutil.rmtree(replica_path)
            logging.info(f"Removed directory {replica_path}")
        else:
            replica_path.unlink()
            logging.info(f"Removed file {replica_path}")

    for sub_dir in dir_cmp.common_dirs:
        sync_directories(source_dir / sub_dir, replica_dir / sub_dir)


def start_sync(source_dir, replica_dir, interval):
    """
    Start the synchronization process, repeating it at the specified interval.
    """
    import time

    while True:
        logging.info("Starting synchronization...")
        sync_directories(source_dir, replica_dir)
        logging.info(f"Synchronization complete. Waiting for next {interval} seconds.")
        time.sleep(interval)

