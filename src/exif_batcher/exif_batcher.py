# user libraries
from . import parser_handler
from . import eb_file_management
from . import eb_jpeg_segment_parser


# maestro
def main():
    """
    main function to execute the script logic.
    """

    # handle parser operations
    parser_handler.EBParserHandler.handle_parser()

    files = eb_file_management.EBFileManager.extract_files_from_folder()
    eb_jpeg_segment_parser.EBJPEGSegmentParser.get_metadata(files)


if __name__ == "__main__":
    main()
