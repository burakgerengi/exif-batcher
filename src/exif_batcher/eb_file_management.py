# native libraries
from pathlib import PurePosixPath
import os


class EBFileManager:

    @staticmethod
    def add_folder_to_config(folder_path: str = "") -> None:
        """
        add current directory to the config.toml file for batch processing.

        Arguments:
        folder_path: folder path as string, uses the current working directory as default.
        """

        if folder_path == "":
            folder_path = os.getcwd()

        is_folder_for_batch = input(
            f"current working directory: {folder_path}\nAdd to the batch list? (y/N): "
        )

        # validate
        if is_folder_for_batch in ["", "N", "n", "no"]:
            return

        elif is_folder_for_batch in ["Y", "y", "yes"]:
            # TODO: fix config.toml reference
            config_file_path = str(PurePosixPath(__file__).parent / "config.toml")

            with open(config_file_path, "a") as config:
                config.writelines(f"batch folder path: {folder_path}")

    @staticmethod
    def extract_files_from_folder(folder_path: str = "") -> list:
        """
        extract files from the current working directory.

        Arguments:
        folder_path: folder path as string, uses the current working directory as default.
        """

        if folder_path == "":
            folder_path = os.getcwd()

        print(f"selected folder to get files extracted: {folder_path}")

        # get all files in the current working directory
        files = os.listdir(folder_path)

        # filter out directories and keep only files
        files = []

        for file in os.listdir(folder_path):
            if os.path.isfile(file):
                print(file)
                files.append(file)
            else:
                continue

        return files


if __name__ == "__main__":
    print("this is a module.")
