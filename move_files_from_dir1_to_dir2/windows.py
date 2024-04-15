import os
import shutil

def move_files_to_downloads(desktop_path, downloads_path):
    # Get list of files on the desktop
    desktop_files = os.listdir(desktop_path)
    
    # Iterate through each file
    for file_name in desktop_files:
        # Construct full path of the file
        file_path = os.path.join(desktop_path, file_name)
        
        # Check if it's a file (not directory)
        if os.path.isfile(file_path):
            # Move the file to the Downloads directory
            shutil.move(file_path, downloads_path)
            print(f"Moved {file_name} to {downloads_path}")

if __name__ == "__main__":
    # Desktop and Downloads paths
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    downloads_path = "F:/Downloads"  # Change this to your Downloads path
    
    # Move files
    move_files_to_downloads(desktop_path, downloads_path)
