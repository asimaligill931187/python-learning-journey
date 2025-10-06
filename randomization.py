import random
random_num=random.randint(1,100)
print(f"number is:{random_num} ")
# random float
random_float=random.random()*5
print(random_float)
# 
# 
# seed
print("seed is ")
print(random.seed(10))
print(random.random())


# 
# 
# 
import random

# Set a seed for reproducibility
random.seed(42)

print("Random float [0.0, 1.0):", random.random())
print("Random float [10, 20]:", random.uniform(10, 20))
print("Random integer [1, 100]:", random.randint(1, 100))
print("Random number from range(0, 10):", random.randrange(0, 10, 2))

names = ['Alice', 'Bob', 'Charlie', 'David']
print("Random choice:", random.choice(names))
print("Random 2 choices with replacement:", random.choices(names, k=2))
print("Random 2 unique samples:", random.sample(names, 2))

# Shuffle the list
random.shuffle(names)
print("Shuffled names:", names)

