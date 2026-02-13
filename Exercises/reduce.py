# Reduce
# The built-in functools.reduce() function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes.



# # import functools from the standard library
# import functools

# def add(sum_so_far, x):
#     print(f"sum_so_far: {sum_so_far}, x: {x}")
#     return sum_so_far + x

# numbers = [1, 2, 3, 4]
# sum = functools.reduce(add, numbers)
# # sum_so_far: 1, x: 2
# # sum_so_far: 3, x: 3
# # sum_so_far: 6, x: 4
# # 10 doesn't print, it's just the final result
# print(sum)
# # 10

# Notice that we are passing the function add without the ().

# It means that reduce will take care of the execution and pass the parameters for you.

# Think of passing add like handing someone a recipe (the instructions), instead
# of the finished dish (the result of the execution).

# Assignment
# Complete the join and the join_first_sentences functions.

# Complete the join function. It's a helper function we'll use in join_first_sentences.
# It takes two inputs:
# A doc_so_far accumulator string - similar to the sum_so_far variable in the example above.
# A sentence string - this is the next string we want to add to the accumulator.
# Returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:
# doc = "This is the first sentence"
# sentence = "This is the second sentence"
# print(join(doc, sentence))
# # This is the first sentence. This is the second sentence

# Complete the join_first_sentences function.
# It accepts two arguments:
# A list of sentence strings
# An integer n
# Only use the first n sentences from the list. If n is zero, just return an empty string.
# Use functools.reduce() with your join function to combine the sliced sentences into a single string.
# Add a final period without a trailing space and return this string.
# Use list slicing to get the first n sentences.

# Here's an example of the expected behavior:

# joined = join_first_sentences(
#     ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
#     2
# )
# print(joined)
# # This is the first sentence. This is the second sentence.

import functools


def join(doc_so_far, sentence):
    return f"{doc_so_far}. {sentence}"


def join_first_sentences(sentences, n):
    if n == 0:
        return ""

    # string = functools.reduce(join, sentences[:n])
    # return f"{string}."  
    return functools.reduce(join, sentences[:n]) + "."
      