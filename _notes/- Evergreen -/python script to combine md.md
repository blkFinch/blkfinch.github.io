---
title: python script to combine md
date: 2023-09-04
feed: hide
tags: []
---

#### example code
```python
import os

import sys

#depends on filenaming convention MR-%3Cnum%3E-- <str>
def get_record_number(filename):
    try:
        return int(filename.split('--')[0].split('-')[1])
    except (IndexError, ValueError):
        return float('inf')  # Set a very high value for filenames without numeric part


def combine_markdown_files(folder_path, output_file):
    print("combining: ", folder_path)
    files = sorted(os.listdir(folder_path), key=get_record_number)
    with open(output_file, "w", encoding="utf-8") as output:

        for file_name in files:

             if file_name.endswith(".md"):
                file_path = os.path.join(folder_path, file_name)

                with open(file_path, "r", encoding="utf-8") as markdown_file:
                    markdown_content = markdown_file.read()

                    output.write(markdown_content)

                    output.write("\n\n")

  

if __name__ == "__main__":

        folder_path = sys.argv[1]

        output_file = "combined.md"

combine_markdown_files(folder_path, output_file)>)
```
run from console:
```
<full path>/combiner.py <full path to folder to combine>pythi
```


