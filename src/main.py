import os
import shutil

def copy_directory_contents(src, dest):
    # Step 1: Ensure destination directory is empty
    if os.path.exists(dest):
        shutil.rmtree(dest)
        print(f"Deleted existing contents in {dest}")
    
    # Create the destination directory
    os.makedirs(dest)
    print(f"Created destination directory: {dest}")
    
    # Step 2: Recursively copy contents from source to destination
    for item in os.listdir(src):
        s = os.path.join(src, item)  # Source item
        d = os.path.join(dest, item)  # Destination item
        
        if os.path.isdir(s):
            # If it's a directory, recurse into it
            copy_directory_contents(s, d)
        else:
            # If it's a file, copy it
            shutil.copy(s, d)
            print(f"Copied file: {s} to {d}")

def main():
    src = 'static'  # Source directory
    dest = 'public'  # Destination directory
    copy_directory_contents(src, dest)

if __name__ == "__main__":
    main()
