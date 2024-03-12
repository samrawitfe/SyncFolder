# SyncFolder

SyncFolder is a Python-based tool designed to synchronize the contents of a source directory with a replica directory, ensuring that the replica is an exact copy of the source. This utility handles file copying, updating, deletion, and supports advanced features like symbolic link replication and preserving file permissions, making it suitable for a wide range of synchronization tasks.

## Features

- One-way synchronization from source to replica directory.
- Support for symbolic links and file permission preservation.
- Periodic synchronization based on a user-defined interval.
- Comprehensive logging of operations to both console and file.
- Cross-platform support (Windows, Linux, macOS).

## Installation

To use SyncFolder, ensure you have Python 3.6 or newer installed on your system. Clone this repository to get started:

```bash
git clone https://github.com/samrawitfe/SyncFolder.git
cd SyncFolder
```

## Usage

python main.py --source_dir /path/to/source --replica_dir /path/to/replica --interval <60> --log_path /path/to/sync.log

- --source_dir: The path to the source directory.
- --replica_dir: The path to the replica directory.
- --interval: Synchronization interval in seconds.
- --log_path: Path to the log file where operations will be logged.

SyncFolder includes `test_source_dir` and `test_replica_dir` directories within the repository for testing purposes. These directories are designed to help you verify the synchronization functionality, including handling of regular files, symbolic links, and preservation of file permissions.

## Author

Samrawit Fentaye Abebe
samrawitabebe108@gmail.com
