#--- shell ---
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive


# make a duplicate of an existing file
if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt");

# separate the path part from the filename
    (head, tail) = path.split(src)
    print("path: %s", str(head))
    print("file: %s", str(tail))

    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    # now use the shell to make a copy of the file
    shutil.copy(src,dst)

    # copy meta data such as permissions, modification times, and other info
    shutil.copystat(src, dst)

    # rename the original file
    os.rename("textfile.txt", "newfile.txt")

    # now put things into a ZIP archive; how to archive an entire dir
    root_dir, tail = path.split(src)  # split path and file name
    shutil.make_archive("archive", "zip", root_dir)  # (archive_name, type, zipped_directory)

    # more fine-grained control over ZIP files; jut adding two files to the archive
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("newfile.txt")
      newzip.write("textfile.txt.bak")

