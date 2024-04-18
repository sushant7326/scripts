import os
import time
from datetime import datetime, timedelta
import subprocess

# Set the folder path containing the images
folder_path = "/media/sushant-singh/SteamLibrary1/Walls/anime"

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".png", ".jpeg", ".gif"))]

# Initialize the current index to 0
current_index = 0

while True:
    # Get the current image file
    current_image = image_files[current_index]
    
    # Set the desktop wallpaper
    subprocess.run(["dbus-send", "--session", "--type=method_call", "--dest=org.gnome.Desktop.WallpaperManager", "/org/gnome/Desktop/WallpaperManager", "org.gnome.Desktop.WallpaperManager.SetWallpaper", f"string:{os.path.join(folder_path, current_image)}"], check=True)
    
    # Print the current time and the image file being set as the wallpaper
    print(f"{datetime.now().strftime('%H:%M:%S')} - Setting wallpaper to: {current_image}")
    
    # Wait for 10 minutes
    next_change = datetime.now() + timedelta(seconds=5)
    while datetime.now() < next_change:
        time.sleep(1)
    
    # Move to the next image file
    current_index = (current_index + 1) % len(image_files)
