import os
import zipfile
import shutil

def move_png_files(zip_folder_name):
    # Check if PNG files already exist
    png_files_exist = all([os.path.exists(f"{i}.png") for i in range(1, 7)])

    if png_files_exist:
        print("PNG files already exist. Moving them to their respective directories.")
        for i in range(1, 7):
            language_code = str(i)
            if language_code == '1':
                destination_dir = ''
            elif language_code == '2':
                destination_dir = './ar'
            elif language_code == '3':
                destination_dir = './es'
            elif language_code == '4':
                destination_dir = './fr'
            elif language_code == '5':
                destination_dir = './hi'
            elif language_code == '6':
                destination_dir = './zh'

            if destination_dir:
                shutil.move(f"{i}.png", os.path.join(destination_dir, f"{zip_folder_name.split('.')[0]}.png"))
    else:
        print("PNG files not found. Extracting zip folder.")
        # Unzip the folder
        with zipfile.ZipFile(zip_folder_name, 'r') as zip_ref:
            zip_ref.extractall()

        # Get the name of the zip folder (without the extension)
        folder_name = os.path.splitext(zip_folder_name)[0]

        # Check if the folder exists
        if os.path.exists(folder_name):
            # Loop through the extracted files
            for file_name in os.listdir(folder_name):
                # Get the file extension
                _, extension = os.path.splitext(file_name)
                if extension == '.png':
                    # Determine the destination directory based on language code
                    if file_name == '1.png':
                        destination_dir = ''
                    elif file_name == '2.png':
                        destination_dir = './ar'
                    elif file_name == '3.png':
                        destination_dir = './es'
                    elif file_name == '4.png':
                        destination_dir = './fr'
                    elif file_name == '5.png':
                        destination_dir = './hi'
                    elif file_name == '6.png':
                        destination_dir = './zh'
                    else:
                        continue

                    # Move the file to the appropriate directory
                    shutil.move(os.path.join(folder_name, file_name), os.path.join(destination_dir, f"{folder_name}.png"))
            
            # Clean up: remove the extracted folder
            os.rmdir(folder_name)
        else:
            print(f"Error: Failed to extract {zip_folder_name}")

# Example usage:
zip_folder_name = "pdf-to-epub.zip"
move_png_files(zip_folder_name)
