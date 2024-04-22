import os
import csv
from utils_custom.dir_utils import create_dir_if_not_exists



def create_csv_file(csv_full_filename: str, csv_headers: list,
                    data_dicts_list: list, file_rewrite: bool = False) -> None:
    """
    Create CSV file from data_list. If file_rewrite is True,
    the file will allways be rewritten when creating. Otherwise, it will
    be passing creating a new csv file
    :param csv_full_filename: str: Full initial_name of the csv file
    :param csv_headers: list: List of the columns(fields) names to be included in the csv file
    :param data_dicts_list: list: Data with dictionaries list to be saved into csv file
    :param file_rewrite: bool: Rewrite existing csv file or not
    :return: None
    """

    if not file_rewrite and os.path.exists(csv_full_filename):
        print(f"\n\tExisting CSV file '{csv_full_filename}' used")
        return

    create_dir_if_not_exists(csv_full_filename)

    try:
        with open(csv_full_filename, "w", encoding="utf-8", newline="") as csv_file:

            try:
                writer = csv.DictWriter(csv_file,
                                        fieldnames=csv_headers,
                                        dialect="excel",
                                        # restval="",  # if has no value in dictionary
                                        extrasaction="ignore"  # if dictionary key not not found field names
                                        )
                writer.writeheader()
                writer.writerows(data_dicts_list)

                print(f"\n\tCSV file '{csv_full_filename}' created")
            except (csv.Error, Exception) as csv_error:
                print(f"CSV write error: {csv_error}")

    except (IOError, FileExistsError, Exception) as file_error:
        print(f"File write error: {file_error}")
