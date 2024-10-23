from django.test import TestCase

# Create your tests here.
import random as rnd
import math
a = [[3, 3, 3],
     [3, 3, 3],
     [3, 3, 3]]

b = [rnd.randint(1, 30) for i in range(10)]
even_nums = [i for i in b if i % 2 == 0]

sum_nums = 0
product = 1
for num in even_nums:
    sum_nums += num
    product *= num

print(f"Reference array: {b}\nEven numbers: {even_nums}\nProduct: {product}\n"
      f"Average even: {sum_nums/len(even_nums)}\nSum even: {sum_nums}\n")
print(f"Using math and sum:\nReference array: {b}\nEven numbers: {even_nums}\n"
      f"Product: {math.prod(even_nums)}\nAverage even: {sum(even_nums)/len(even_nums)}\nSum even: {sum(even_nums)}")





