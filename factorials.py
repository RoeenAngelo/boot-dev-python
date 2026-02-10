# Factorials
# We're almost done with the math that you'll need for this course! Just one last thing... factorials.

# Click to hide video

# The factorial of a positive integer n, written n!, is the product of all positive integers less than and equal to n.

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# The results of a factorial grow even faster than exponentiation!

# n! grows faster than 2^n:

# n!	2^n
# 2	2	4
# 3	6	8
# 4	24	16
# 5	120	32
# 6	720	64
# Assignment
# Influencers need to be able to schedule posts to be published in the future. We've found that the order in which the posts are published drastically affects their performance.

# Complete the num_possible_orders function. It takes the number of posts an influencer has in their backlog as input and returns the total number of possible orders in which we could publish the posts.

# Tip
# Factorials are useful whenever you're trying to count how many ways a collection can be ordered. For example, how many different ways can a deck of cards be arranged?

# The first card could be any of the 52 cards.
# The second card can be any of the 51 remaining cards.
# The third card can be any of the 50 remaining cards, and so on.
# That means the total number of possibilities is the 52 options multiplied by 51 options multiplied then by 50 options, and so on.

# 52 * 51 * 50 ... * 2 * 1

# Or in other words, the number of possible combinations for a deck of cards is 52!, or 80,658,175,170,943,878,571,660,636,856,403,766,975,289,505,440,883,277,824,000,000,000,000 (I didn't count the zeros but I think this is correct).

def num_possible_orders(num_posts):
    product = 1
    for i in range(1, num_posts + 1):
        product *= i
    return product
