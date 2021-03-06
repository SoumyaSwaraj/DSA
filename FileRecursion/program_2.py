import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    mylist = []

    dirs = os.listdir(path)
    # This would print all the files and directories
    for filex in dirs:
        f = os.path.join(path, filex)
        isdir = os.path.isdir(f)
        
        if isdir:
            new_path = os.path.join(path, filex)
            newlist = find_files(".c", new_path)
            mylist.extend(newlist)
        isfile = os.path.isfile(f)
        if isfile and filex.endswith(".c"):
            mylist.append(f)
    return mylist

find_files(".c", "C:\\Users\\user\\Desktop\\testdir")
