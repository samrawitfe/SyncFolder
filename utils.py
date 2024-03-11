import argparse
import logging
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(description='Synchronize a source folder with a replica folder.')
    parser.add_argument('--source_dir', required=True, help='Path to the source directory')
    parser.add_argument('--replica_dir', required=True, help='Path to the replica directory')
    parser.add_argument('--interval', type=int, required=True, help='Synchronization interval in seconds')
    parser.add_argument('--log_path', required=True, help='Path to the log file')
    return parser.parse_args()


def setup_logging(log_path):
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        handlers=[logging.FileHandler(log_path, 'a', 'utf-8'),
                                  logging.StreamHandler(sys.stdout)])