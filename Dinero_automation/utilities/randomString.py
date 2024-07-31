import random
import string

def random_string_generator(size = 5, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_30(size = 30, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_50(size = 50, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_28(size = 28, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_48(size = 48, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_31(size = 31, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_51(size = 51, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))