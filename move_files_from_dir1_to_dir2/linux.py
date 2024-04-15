import os
import shutil

def move_files_to_destination(source_path, destination_path):
    # Get list of files and folders on the source path (desktop)
    source_items = os.listdir(source_path)
    
    # Iterate through each item
    for item_name in source_items:
        # Construct full path of the item
        item_path = os.path.join(source_path, item_name)
        
        # Move the item to the destination directory
        shutil.move(item_path, destination_path)
        print(f"Moved {item_name} to {destination_path}")

if __name__ == "__main__":
    # Desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Destination path for Linux
    destination_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Move files and folders
    move_files_to_destination(desktop_path, destination_path)
