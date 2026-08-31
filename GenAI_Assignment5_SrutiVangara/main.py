import math_utils
from math_utils import square
print("Addition of 2,3 : ",math_utils.add(2,3))
print("Subtraction of 4 ,3: ",math_utils.subtract(4,3))
print("Square of 4 is: ",square(4))

import string_utils
text = "hello world"
print("Capitalize: ",string_utils.capitalize_words(text))
print("Reverse string: ",string_utils.reverse_string(text))
print("Word count: ",string_utils.word_count(text))

import shop_package.discount as disc
from shop_package.billing import calculate_total
print(disc.apply_discount(1000,10))
print(calculate_total([100,200,300]))