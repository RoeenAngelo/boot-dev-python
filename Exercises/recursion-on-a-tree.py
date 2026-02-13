# Recursion on a Tree
# Recursion is often used in "tree-like" structures. For example:

# Nested dictionaries
# File systems
# HTML documents
# JSON objects
# That's because trees can have unknown depth. It's hard to write a series of loops because you don't know how many levels deep the tree goes.

# for entry_i in directory:
#     if entry_i.is_dir:
#         for entry_j in entry_i:
#             if entry_j.is_dir:
#                 for entry_k in entry_j:
#                     ...

# Assignment
# You're responsible for a module in Doc2Doc that can scan a file system (represented in our code as nested dictionaries) and create a list of the filenames.

# Complete the recursive list_files function. It accepts two arguments:

# parent_directory: A dictionary of dictionaries representing the current directory. A child directory's value is a dictionary and a file's value is None.
# current_filepath: A string representing the current path (e.g. /dir1/dir2/filename.txt)
# It should return a list of all filepaths in the parent_directory.

# Steps
# Create an empty list to store the file paths.
# Use a for-loop to iterate through the keys of the parent_directory dictionary:
# Use the key to create a new file path by concatenating a slash / and the key to the end of the current_filepath.
# If the value is None, the key is a filename. .append() the new file path to the list of file paths.
# Otherwise, the value is a child directory dictionary. Recursively call list_files with the child directory dictionary and the new file path.
# Use .extend() to add the results of the recursive call to the list of file paths.
# Return the list of file paths.
# Example parent_directory:

# {
#     "Documents": {
#         "Proposal.docx": None,
#         "Receipts": {
#             "January": {
#                 "receipt1.txt": None,
#                 "receipt2.txt": None
#             },
#             "February": {
#                 "receipt3.txt": None
#             }
#         }
#     },
# }

# Resulting list of file paths:

# [
#     "/Documents/Proposal.docx",
#     "/Documents/Receipts/January/receipt1.txt",
#     "/Documents/Receipts/January/receipt2.txt",
#     "/Documents/Receipts/February/receipt3.txt"
# ]

# Tips
# What's the base case? It looks a bit different than before, but it's just when a nested node's value is None because in that case we don't have any more directories to explore.
# You might be wondering why we used a loop! Loops are nice when we know how many times we need to iterate (the number of keys in the dictionary). Recursion is nice when we don't know how many times we need to iterate (the number of nested dictionaries).
# Use .extend() to add a list's items to another list:
# items = ["six-string lute", "petrified dragon egg", "the only ring"]
# items.extend(["philosopher's stone", "invisibility cloak", "moistened scimitar"])
# # ["six-string lute", "petrified dragon egg", "the only ring", "philosopher's stone", "invisibility cloak", "moistened scimitar"]

def list_files(parent_directory, current_filepath=""):
    file_paths = []

    for item in parent_directory:
        new_path = current_filepath + "/" + item
        if parent_directory[item] == None:
            file_paths.append(new_path)
        else:
            file_paths.extend((list_files(parent_directory[item], new_path)))

    return file_paths
