import os
import shutil
import logging
from pathlib import Path
from filecmp import dircmp


def sync_directories(source_dir, replica_dir):
    """
    Synchronize contents from source_dir to replica_dir.
    """
    source_dir = Path(source_dir)
    replica_dir = Path(replica_dir)

    dcmp = dircmp(source_dir, replica_dir)

    for filename in dcmp.left_only + dcmp.diff_files:
        source_path = source_dir / filename
        replica_path = replica_dir / filename

        if source_path.is_dir():
            shutil.copytree(source_path, replica_path)
            logging.info(f"Copied directory {source_path} to {replica_path}")
        else:
            shutil.copy2(source_path, replica_path)
            logging.info(f"Copied file {source_path} to {replica_path}")

    for filename in dcmp.right_only:
        replica_path = replica_dir / filename
        if replica_path.is_dir():
            shutil.rmtree(replica_path)
            logging.info(f"Removed directory {replica_path}")
        else:
            replica_path.unlink()
            logging.info(f"Removed file {replica_path}")

    for sub_dir in dcmp.common_dirs:
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

