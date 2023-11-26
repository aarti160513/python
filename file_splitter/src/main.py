import os
import logging
from pathlib import Path
import typer

logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
c_handler.setFormatter(
    logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(c_handler)
logger.setLevel(logging.DEBUG)


def get_file_size(file_path: Path) -> int:
    """
    Returns file size of the specified file

    Parameters:
        file_path (str): file path
    
    Returns:
        file_size(int): file size in bytes

    """

    # Get file size in bytes
    file_size: int = os.path.getsize(file_path)
    return file_size


def split_file(
    input_file: Path,
    no_files_to_split: int = 10,
    output_dir: Path = Path('.')) -> [Path]:
    """
    Returns files created after splitting original file

    Parameters:
        file_path (Path): path of file to be split
    
    Returns:
        split_files([Path]): array of file Paths

    """
    split_files: [Path] = []
    file_size = get_file_size(input_file)
    output_file_name = input_file.name

    with open(input_file, 'rb') as fin:

        chunk_size = int(file_size / no_files_to_split)
        logger.info(f'file size = {file_size} chunk size = {chunk_size}')

        # Write first n-1 files
        for i in range(1, no_files_to_split):
            file = output_dir / f'{output_file_name}_{i}'
            with open(file, 'wb') as fout:
                logger.info(f'writing file {file}')
                split_files.append(file)
                fout.write(fin.read(chunk_size))

        # Write the last file. The size might vary depending upon if file size
        # is evenly divisible by no of files to split
        file = output_dir / f'{output_file_name}_{no_files_to_split}'
        with open(file, 'wb') as fout:
            split_files.append(file)
            if not file_size % no_files_to_split:
                logger.info(f'writing file {file}')
                fout.write(fin.read(chunk_size))
            else:
                last_chunk_size = chunk_size + (file_size % no_files_to_split)
                logger.info(
                    f'file size = {file_size} chunk size = {chunk_size}  last_chunk_size = {last_chunk_size}'
                )
                logger.info(f'writing file {file}')
                fout.write(fin.read(last_chunk_size))

    return split_files


# def merge_files(files: [Path], output_file):

#     with open(output_file, 'wb') as fout:
#         for file in files:
#             with open(file, 'rb') as fin:
#                 fout.write(fin.read())


if __name__ == "__main__":

    typer.run(split_file)
