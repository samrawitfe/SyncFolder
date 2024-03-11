import logging

from utils import parse_arguments, setup_logging


def main():
    args = parse_arguments()
    setup_logging(args.log_path)

    logging.info("Starting SyncFolder with source: %s, replica: %s, interval: %s seconds",
                 args.source_dir, args.replica_dir, args.interval)


if __name__ == '__main__':
    main()

