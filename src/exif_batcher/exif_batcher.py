# native libraries
import argparse
import sys
import pathlib
import yaml


def get_script_path() -> str:
    """
    get the path of the script.

    returns:
        str: The path of the script.
    """
    return str(pathlib.PurePath(__file__).parent)


def handle_script_path(path_as_str: str) -> None:

    # open config
    config = open(f"{path_as_str}/config.yaml", "r+")
    loaded_data = yaml.safe_load(config)

    try:
        # set the script path in the config if changed
        if loaded_data.get("savedScriptPath") != path_as_str:

            # write data
            data_to_write = {"savedScriptPath": path_as_str}
            yaml.dump(data_to_write, config)

            # loaded_data["savedScriptPath"] = path_as_str
            sys.path.append(path_as_str)

    except (TypeError, AttributeError) as e:
        print(f"error occurred while updating config: {e}")
        user_intention = input(
            "the error might be regarding an empty YAML file. Do you want to update the config? (Y/n): "
        )
        if user_intention.lower() == "y" or user_intention == "":
            # write data
            data_to_write = {"savedScriptPath": path_as_str}
            yaml.dump(data_to_write, config)
            sys.path.append(path_as_str)

        else:
            print("exiting the script due to the error.")
            sys.exit(1)


def handle_parser() -> None:
    """
    handle parser operations.
    """

    # init parser
    parser = argparse.ArgumentParser()

    # optional arguments
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="1.0",
        help="show the script version",
    )

    parser.parse_args()


def main():
    """
    main function to execute the script logic.
    """

    handle_parser()
    str_script_path = get_script_path()


if __name__ == "__main__":
    main()
