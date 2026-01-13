from functools import reduce
numbers = [1,4,9,11,21]

ans1 = map(lambda n:n**2, numbers)
print(list(ans1))

ans2 = filter(lambda n:n%2==1, numbers)
print(list(ans2))

ans3 = reduce(lambda n1,n2:n1+n2, numbers)
print(ans3)

# Finding the maximum value in a list
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum value: {max_value}")  # Output: Maximum value:

# Concatenating strings with an initializer
words = ["Python", "is", "fun"]
sentence = reduce(lambda x, y: f"{x} {y}", words, "Learning")
print(f"Sentence: {sentence}") # Output: Sentence: Learning Python is fun
