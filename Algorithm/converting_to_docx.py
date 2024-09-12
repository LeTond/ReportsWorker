import glob
import os
import shutil
import subprocess


def docx_(root, path, new_path):
    """
    Converting documents from .doc, .odt, .rtf formats to .docx format
    and recursion copying all docx format documents into new directory
    :param root: root path
    :param path: path to directory with documents for converting
    :return: None
    """
    current_path = path
    os.chdir(current_path)
    # new_path = current_path + '_copy'
    os.mkdir(new_path)

    # for filename in os.walk(path=path):
    for filename in glob.glob("**/*.doc", recursive=True):
        converting_to_docx(filename, new_path)

    for filename in glob.glob("**/*.odt", recursive=True):
        converting_to_docx(filename, new_path)

    for filename in glob.glob("**/*.rtf", recursive=True):
        converting_to_docx(filename, new_path)

    copy_docx_to_new_directory(current_path, new_path)


def converting_to_docx(filename, new_path):
    """
    Converting files to docx format
    :param filename: filename for converting
    :param new_path: new directory for converted files
    :return: None
    """
    subprocess.call([
        'soffice', '--headless', '--convert-to', 'docx', '--outdir',
        new_path,
        filename
    ])


def copy_docx_to_new_directory(current_path, new_path):
    """
    Copy files in docx format in to new directory
    :param current_path: path to directory with files
    :param new_path: path to new directory
    :return: None
    """
    for directs, direct, files in os.walk(current_path):
        for file in files:
            if file.endswith(".docx"):
                shutil.copy(os.path.join(directs, file), new_path)


if __name__ == '__main__':
    root = "/root_directory"
    old_path = "/path_to_old_directory"
    new_path = "/path_to_new_directory"
    docx_(root, old_path, new_path)

