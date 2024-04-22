import os



def create_dir_if_not_exists(full_filename: str) -> None:
    """
    Check whether a directory exists and creates it if not
    :param full_filename: string containing the full path and local_full_filename
    :return: None
    """
    directory_name = os.path.dirname(full_filename)
    try:
        os.makedirs(directory_name, exist_ok=True)
    except (IOError, Exception) as error:
            print(f"Error occurred: {error}")
