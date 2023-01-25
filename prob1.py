# Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# OBJECTIVE: Find the sum of all the multiples of 3 or 5 below 1000.

def three_five_sum(n):
  sum = 0
  for num in range(1,n+1):
    if (num % 3 == 0) or (num % 5 == 0):
      sum += num
      
  return (sum-n)

my_sum = three_five_sum(10)

print(my_sum)