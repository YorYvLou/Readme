import math
import random

x = int(input("range : "))
parent1=str(input("Enter a list of 1s and 0s, the two should be the same lenght : " ))
parent2=str(input("Enter a list of 1s and 0s, the two should be the same lenght : "))
#Initial Parents need to be printed
print("parent1:", parent1)
print("parent2:", parent2)
#This will print a variety of children all that should be a mix of both
for i in range(x):
    print("Children", ''.join(random.sample(parent1, random.randint(x,x))))
for i in range(x):
    print("Children Set 2", ''.join(random.sample(parent2, random.randint(x,x))))
