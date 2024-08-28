import random
import string

def random_string_generator(size = 7, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_new(size = 7, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_numbers(size = 16, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_numbers_new(size = 16, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_string_generator_numbers_10(size = 10, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_numbers_18(size = 18, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_numbers_20(size = 20, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_numbers_22(size = 22, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_numbers_max_10(size = 10, chars = string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_20(size = 20, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_22(size = 20, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_30(size = 30, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_32(size = 32, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_50(size = 50, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_52(size = 52, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_28(size = 28, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_48(size = 48, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_31(size = 31, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_51(size = 51, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_string_generator_max_18(size = 18, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))


def generate_random_email(max_length=50):
    local_part_length = random.randint(1, max_length - 7)  # Subtracting length for '@domain.com'
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=local_part_length))
    domain_part = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
    email = f"{local_part}@{domain_part}.com"

    return email

def generate_random_email_new(max_length=15):
    local_part_length = random.randint(1, max_length - 7)  # Subtracting length for '@domain.com'
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=local_part_length))
    domain_part = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
    email = f"{local_part}@{domain_part}.com"

    return email

def generate_random_email_lessthen_45(max_length=45):
    local_part_length = random.randint(1, max_length - 7)  # Subtracting length for '@domain.com'
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=local_part_length))
    domain_part = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
    email = f"{local_part}@{domain_part}.com"

    # Ensure the total length does not exceed max_length
    if len(email) > max_length:
        email = email[:max_length]

    return email

def generate_random_email_lessthen_52(max_length=45):
    local_part_length = random.randint(1, max_length - 7)  # Subtracting length for '@domain.com'
    local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=local_part_length))
    domain_part = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 5)))
    email = f"{local_part}@{domain_part}.com"

    # Ensure the total length does not exceed max_length
    if len(email) > max_length:
        email = email[:max_length]

    return email