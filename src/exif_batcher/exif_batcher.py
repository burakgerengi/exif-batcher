# native libraries
import argparse
from importlib.metadata import version


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
        version=str(version("exif-batcher")),
        help="show the script version",
    )

    parser.parse_args()


def main():
    """
    main function to execute the script logic.
    """

    # maestro
    handle_parser()


if __name__ == "__main__":
    main()
