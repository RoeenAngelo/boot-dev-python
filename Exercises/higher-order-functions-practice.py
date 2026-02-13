# Higher Order Functions Practice
# Doc2Doc needs a way to restore documents from saved backups. However, not all original documents may have backups, and some backups might be corrupted.

# Assignment
# Complete the restore_documents function in one line - if you can. It takes two tuples of document strings, originals and backups, as input and returns a set.

# Convert all documents to the same case with .upper() for comparison.
# Filter out documents that are corrupted strings of random numbers with .isdigit().
# Return a set that combines (and deduplicates) the documents from originals and backups.
# Tip
# I used map, filter and lambda functions to complete the function on one line, but it's split up by multi-line formatting for your readability.

def restore_documents(originals, backups):
    return set(filter
               (lambda doc: not doc.isdigit(), 
                map(lambda doc: doc.upper(), originals + backups)
                )
            )
