# user libraries
from . import eb_file_management

# external libraries
import exiftool


class EBJPEGSegmentParser:

    @staticmethod
    def get_metadata(files: list):
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(files)
            for d in metadata:
                print(
                    "{:20.20} {:20.20}".format(
                        d["SourceFile"], d["EXIF:DateTimeOriginal"]
                    )
                )


if __name__ == "__main__":
    print("this is a module.")
