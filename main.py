import logging

from sync_folder import start_sync
from utils import parse_arguments, setup_logging


def main():
    args = parse_arguments()
    setup_logging(args.log_path)

    logging.info("Starting SyncFolder with source dir: %s, replica dir: %s, interval: %s seconds",
                 args.source_dir, args.replica_dir, args.interval)

    start_sync(args.source_dir, args.replica_dir, args.interval)


if __name__ == '__main__':
    main()

