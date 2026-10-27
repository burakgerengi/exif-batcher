# native libraries
import argparse
from importlib.metadata import version


class EBParserHandler:

    @staticmethod
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
