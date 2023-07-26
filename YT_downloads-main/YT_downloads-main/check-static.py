import os
import glob

html_files_path = r"YT_downloads-main\YT_downloads-main\templates"  # Path to the 'snapsave.io' directory
css_path = r"YT_downloads-main\YT_downloads-main\static\css\css"
images_path = r"YT_downloads-main\YT_downloads-main\static\images"


def replace_static_paths():
    for root, dirs, files in os.walk(html_files_path):
        for file_name in files:
            if file_name.endswith(".html"):
                file_path = os.path.join(root, file_name)

                with open(file_path, "r") as file:
                    content = file.read()

                # Replace CSS path
                content = content.replace("path/to/old/css", css_path)

                # Replace image paths
                content = content.replace("path/to/old/images", images_path)

                # Replace icon paths
                content = content.replace("path/to/old/icons", icons_path)

                # Replace JS path
                content = content.replace("path/to/old/js", js_path)

                # Write the updated content back to the file
                with open(file_path, "w") as file:
                    file.write(content)

    print("Static paths replaced successfully!")

replace_static_paths()
