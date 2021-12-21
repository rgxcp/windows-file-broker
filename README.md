# 🦠 Python - Windows File Broker
**EN**: Simple Windows virus implementation to destroy files in directories.

**ID**: Implementasi virus Windows sederhana untuk merusak file dalam direktori.

## Status
END OF LIFE

## Requirements
1. Python 3

## How to Use
1. Clone this repository to your desired location.
2. Change the path and file extension in `app.py`.
3. Run `python app.py`.
4. Do-what-you-want-with-it!

## How it Works
1. First, we will walk through the provided directory.
2. Second, we will loop through the file in that directory.
3. Third, if the file type is equal with the provided file type, we will read the binary of that file.
4. Fourth, we will shuffle the binary of that file.
5. Finally, we will write the shuffled binary into that file.

NOTE: Please use this carefully, because there's no way to restore the file.

Well, technically we could, we just need to run this program for `bytes` factorial times.

Example, file with 5 bytes of data, we will need to run `5! = 120` times, and test every file to search the correct one.
