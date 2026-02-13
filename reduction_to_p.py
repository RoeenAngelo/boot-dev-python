# Reduction to P
# Let's take an exponential time algorithm and fix it up so it can run in polynomial time!

# The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it. Like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# We want a function that, given an index in the sequence, returns the Fibonacci number at that index. For example:

# fib(0) -> 0
# fib(1) -> 1
# fib(2) -> 1
# fib(3) -> 2
# fib(4) -> 3
# fib(5) -> 5
# fib(6) -> 8
# fib(7) -> 13
# Here are the implementation details to do it in polynomial time:

# The input n represents the index of the desired Fibonacci number.
# If n is less than or equal to 1, then return n.
# Initialize three variables: grandparent = 0, parent = 1, and a placeholder current to store the new Fibonacci number at each step.
# Write a loop that iterates n - 1 times. (For example, if n = 2, one iteration occurs.)
# Inside the loop:
# Set current = parent + grandparent
# Adjust the ancestor values (parent and grandparent) to maintain the sequence.
# Once the loop completes, return current.
# Assignment
# Our data scientists at LockedIn have found that the growth of the average influencer's follow count is roughly the same growth rate as the Fibonacci sequence! In other words, after 6 weeks of good social media posts, the average influencer will have 8 followers. After 7 weeks, 13 followers, and so on.

# The trouble is, our current implementation of the fib function takes so long (exponential time!) to complete that when our influencers navigate to their analytics page it often never completes loading!

# Adjust the fib function using the given algorithm to achieve polynomial runtime.

def fib(n):
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    current = 0

    for _ in range(n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current