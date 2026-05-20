#----1----#  Find the second largest number in a list 


nums = [10, 20, 5, 40, 30]

first = second = float("-inf")

for n in nums:
    if n >= first:
        second = first
        first = n
        print(first)
