import os
import re



def basename_in_full_filename(full_path_filename: str) -> str:
    """
    Get file basename from the full filename containing both directories
    paths and base filename with extension
    :param full_path_filename: str: full filename containing both
           dirs paths and base filename with extension
    :return: str: file basename with extension
    """
    file_name = os.path.basename(full_path_filename)
    return file_name


def path_in_full_filename(full_path_filename: str) -> str:
    """
    Get all directories path from the full filename containing both
    directories paths and base filename with extension
    :param full_path_filename: str: full filename containing both
           dirs paths and base filename with extension
    :return: str: all dirs path without base filename
    """
    path = os.path.dirname(full_path_filename)
    return path


def compose_full_filename(path_directories: tuple | str,
                          file_name: str) -> str|None:
    """
    Create a fullpath local_full_filename
    :param path_directories: str containing one directory
    or tuple containing directories
    :param file_name: str containing the local_full_filename with extension
    :return: str containing the fullpath local_full_filename with extension
    """
    if file_name:
        if isinstance(path_directories, tuple):
            return os.path.join(*path_directories, file_name)

        if isinstance(path_directories, str):
            return os.path.join(path_directories, file_name)
    return None


def make_slashed_name(initial_name: str):
    initial_name = initial_name.strip()
    substitutable_symbols = (", ", "' ", "- ", "\\. ", ",", "'", "-", "\\.", " ", "__", "___")
    substitutable_re_string = "|".join(substitutable_symbols)
    slashed_name = re.sub(substitutable_re_string, "_", initial_name)
    # for symbol in substitutable_symbols:
    #     if symbol in initial_name:
    #         initial_name = initial_name.replace(symbol, "_")
    #         print(initial_name)
    return slashed_name
