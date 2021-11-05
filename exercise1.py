n = int(input())
i = 1  # Iterating number
sumOfOdd = 0
sumOfEven = 0

while i <= n:
    isOdd = (i % 2) == 1
    if isOdd:
        sumOfOdd = sumOfOdd + i
    else:
        sumOfEven = sumOfEven + i
    i = i + 1

print("Sum of odd numbers: ", sumOfOdd)
print("Average of even numbers: ", (sumOfEven / (n / 2)))
