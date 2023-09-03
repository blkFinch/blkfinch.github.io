import os

import sys
def combine_markdown_files(folder_path, output_file):
    with open(output_file, "w", encoding="utf-8") as output:
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".md"):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "r", encoding="utf-8") as markdown_file:
                    markdown_content = markdown_file.read()
                    output.write(markdown_content)
                    output.write("\n\n")

if __name__ == "__main__":
    folder_path = sys.argv[1]
    output_file = "combined.md"
combine_markdown_files(folder_path, output_file)