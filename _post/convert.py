import os

# Directory containing the .md files
directory = "./"

# Revised script with specified encoding and exception handling

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        filepath = os.path.join(directory, filename)

        try:
            # Read the content of the file with UTF-8 encoding
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # Replace 'layout: post' with 'layout: blog-post'
            updated_content = content.replace('\ncategories: Blog', '')

            # Write the updated content back to the file with UTF-8 encoding
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(updated_content)
        except UnicodeDecodeError:
            try:
                # If UTF-8 fails, try with 'latin-1' encoding
                with open(filepath, 'r', encoding='latin-1') as file:
                    content = file.read()

                updated_content = content.replace('layout: post', 'layout: blog-post')

                with open(filepath, 'w', encoding='latin-1') as file:
                    file.write(updated_content)
            except Exception as e:
                # If another error occurs, print the error message
                print(f"Error processing {filename}: {e}")

"Files have been updated, with exceptions handled for encoding issues."
