#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.

 

def is_happy(n):  # Happy number is a number that will eventually equal 1 after a series of math operications
    def get_next(num):
        # Function to calculate the sum of the squares of the digits of a number.
        total_sum = 0   #Keeps track of the cumulative sum of the number squared ( squares the number and adds the resuly)
        while num > 0:   # 3
            num, digit = divmod(num, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

# Example usage:
n = 19
result = is_happy(n)
if result:
    print(f"{n} is a happy number.")
else:
    print(f"{n} is not a happy number.")

