import os
import argparse
import re

def rename_files(args):
    """Core function to rename files based on command-line arguments,
    sorting by creation date."""
    
    # Check if the path exists
    if not os.path.isdir(args.path):
        print(f"Error: Directory not found at {args.path}")
        return

    print(f"Starting rename in: **{args.path}** (Sorted by Creation Date)")
    
    # Get all files and their creation times
    file_data = []
    for filename in os.listdir(args.path):
        filepath = os.path.join(args.path, filename)
        if os.path.isfile(filepath):
            try:
                # Get the creation time (ctime)
                creation_time = os.path.getctime(filepath)
                file_data.append((filename, creation_time))
            except Exception as e:
                print(f"Warning: Could not get creation time for '{filename}'. Skipping. Error: {e}")
                continue

    # Sort the list based on the creation time (the second element in the tuple)
    # The sort order is ascending (oldest first)
    file_data.sort(key=lambda item: item[1])
    
    rename_count = 0
    
    # Extract just the filenames for the loop
    sorted_files = [item[0] for item in file_data]

    for index, filename in enumerate(sorted_files, start=1):
        try:
            name, extension = os.path.splitext(filename)
            new_name = name
            
            # 1. Sequential Numbering Feature (if prefix is provided)
            if args.prefix:
                # Format: [prefix]_[number]
                new_name = f"{args.prefix}_{index}"
            
            # 2. Find & Replace Feature
            if args.find and args.replace is not None:
                # Use sub() for regex support, which is more powerful
                new_name = re.sub(args.find, args.replace, new_name)
            
            # Skip if no change was made and prefix wasn't used
            if new_name == name and not args.prefix:
                continue

            # Construct the final filename and path
            new_filename = f"{new_name}{extension}"
            old_filepath = os.path.join(args.path, filename)
            new_filepath = os.path.join(args.path, new_filename)
            
            # Perform the rename
            os.rename(old_filepath, new_filepath)
            
            print(f"Renamed: '{filename}' -> '{new_filename}'")
            rename_count += 1
            
        except Exception as e:
            print(f"Could not rename '{filename}'. Error: {e}")

    print(f"\nFinished. Total files renamed: **{rename_count}**")

# --- Argument Parsing remains the same ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A Better Finder Rename minimal Python clone for sequential numbering and find/replace, **sorting by creation date**.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Required positional argument for the folder path
    parser.add_argument("path", help="The absolute path to the directory containing files to rename.")
    
    # Optional arguments for renaming modes
    parser.add_argument("-p", "--prefix", help="Prefix for sequential renaming (e.g., -p Photo would rename files to Photo_1.jpg, Photo_2.jpg, etc.).")
    parser.add_argument("-f", "--find", help="Text or **regex pattern** to find in the filenames.")
    parser.add_argument("-r", "--replace", default=None, help="Text to replace the found pattern with (default is None).")
    
    args = parser.parse_args()
    
    # Check for valid combination of find/replace
    if (args.find and args.replace is None) or (args.replace is not None and not args.find):
        parser.error("--find and --replace must be used together.")

    rename_files(args)