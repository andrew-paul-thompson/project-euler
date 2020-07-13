# Solution in O(1) time.
# Count numbers divisible by three, five or three and five. The sum of numbers 1 to N is N*(N+1)/2.
# If A is the number of integers under N that are multiples of three, then the sum of those numbers is (A*(A+1)/2) * 3.
# Add totals for numbers divisible by three and five, then subtract the total for numbers divisible by both.
a = (1000 - 1) // 3
b = (1000 - 1) // 5
c = (1000 - 1) // 15
result = (3 * a * (a + 1) + 5 * b * (b + 1) - 15 * c * (c + 1)) // 2
print(result)
