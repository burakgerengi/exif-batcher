
# exif-batcher

A free, open-source, cross-platform tool for batch image metadata sanitization.

## overview

Images can contain embedded metadata, including location, device information, timestamps, and other potentially sensitive details.

exif-batcher aims to provide a safe, configurable, and automated way to sanitize image metadata while preserving original files and avoiding unnecessary image recompression.

## project status

**early development — not yet functional.**

The initial release will focus on JPEG processing through a Python command-line interface. Additional formats and interfaces are planned for future releases.

## planned features

- configurable metadata sanitization policies
- batch processing with separate input and output directories
- preservation of original files
- metadata removal without unnecessary recompression
- output verification and fail-closed error handling
- safe filename collision handling
- idempotent and policy-aware reprocessing
- manual, scheduled, and continuous processing
- clear logging and error reporting
- future support for additional image formats and a GUI

## license

exif-batcher is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE) for details.
