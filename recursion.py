import argparse
from pathlib import Path
import shutil

# To run the code
# py .\recursion.py -s .\picture\ 


def parse_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--source", type=Path, required=True, help="Source folder"
    )
    parser.add_argument(
        "-d", "--dest", type=Path, default=Path("dest"), help="Destination folder"
    )
    return parser.parse_args()


def recursive_copy(source: Path, dest: Path):
    try:
        for el in source.iterdir():
            if el.is_dir():
                recursive_copy(el, dest)
            else:
                file_extension = el.suffix
                folder_name = file_extension if file_extension else "unknown"
                folder = dest / folder_name
                folder.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, folder)
                
    except shutil.SameFileError:
        print("Source and destination represents the same file")

    except PermissionError:
        print("Permission denied")

    except shutil.Error as e:
        print(f"Error occurred {e}")


def main():
    args = parse_argv()
    recursive_copy(args.source, args.dest)
    print(args)


if __name__ == "__main__":
    main()
