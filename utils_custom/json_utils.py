import os
import json
from utils_custom.dir_utils import create_dir_if_not_exists



def create_json_file(json_full_filename: str, data_dictionary: dict|list,
                     file_rewrite: bool = False) -> None:
    """
    Create JSON file from data_dicts_list. If file_rewrite is True,
    the file will allways be rewritten when creating. Otherwise, it will
    be passing creating a new json file
    :param json_full_filename: str: Full initial_name of the json file
    :param data_dictionary: dict: Data dictionary to be saved into json file
    :param file_rewrite: bool: Rewrite existing json or not
    :return: None
    """

    if not file_rewrite and os.path.exists(json_full_filename):
        print(f"\n\tExisting JSON file '{json_full_filename}' used")
        return

    create_dir_if_not_exists(json_full_filename)

    try:
        with open(json_full_filename, "w", encoding="utf-8") as json_file:

            try:
                json.dump(data_dictionary, json_file, ensure_ascii=False, indent=4)
                print(f"\n\tJSON file '{json_full_filename}' created")
            except (json.JSONDecodeError, Exception) as json_error:
                print(f"JSON dump error: {json_error}")

    except (IOError, FileExistsError, Exception) as file_error:
        print(f"File write error: {file_error}")


def read_json_file(json_full_filename: str) -> dict:
    """
    Reads the json file specified by csv_full_filename
    :param json_full_filename: str: Full initial_name of the json
    :return: dict: Data dictionary to be red from the json file
    """
    try:
        with open(json_full_filename, "r", encoding="utf-8") as json_file:

            try:
                json_data = json.load(json_file)
                return json_data
            except (json.JSONDecodeError, Exception) as json_error:
                print(f"JSON load error: {json_error}")

    except (IOError, FileNotFoundError, Exception) as file_error:
        print(f"File opening error: {file_error}")
