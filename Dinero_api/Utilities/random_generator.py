import random
import string

class Random():
    @staticmethod
    def generate_random_string(length=5):
        letters = string.ascii_letters
        ran_string = ''.join(random.choice(letters) for _ in range(length))
        return ran_string
        # return ran_string  # Return the generated string for potential use

    @staticmethod
    def generate_random_number(max_digits=1):
        ran_numbers =  ''.join(random.choice(string.digits) for _ in range(max_digits))
        return ran_numbers

    @staticmethod
    def generate_random_alphanumeric(length=5):
        letters = string.ascii_letters + string.digits
        ran_alpha_numeric = ''.join(random.choice(letters) for _ in range(length))
        return ran_alpha_numeric

    @staticmethod
    def generate_random_special_characters(length=5):
        special_characters = string.punctuation  # All special characters
        ran_special_char =  ''.join(random.choice(special_characters) for _ in range(length))
        return ran_special_char

    @staticmethod
    def generate_random_special_and_string_characters(length=5):
        special_and_char_characters = string.punctuation + string.ascii_letters
        ran_special_char_and_letter = ''.join(random.choice(special_and_char_characters) for _ in range(length))
        return ran_special_char_and_letter

    @staticmethod
    def generate_random_special_and_string_number(length=5):
        special_and_number_characters = string.punctuation + string.digits
        ran_special_char_and_number = ''.join(random.choice(special_and_number_characters) for _ in range(length))
        return ran_special_char_and_number



#
# # Example usage:
# random_instance = Random()
# random_string = random_instance.generate_random_string()  # Generates and prints an 8-character string
# random_number = random_instance.generate_random_number()  # Generates a 4-digit number
# random_alphanumeric = random_instance.generate_random_alphanumeric()
# random_special_char = random_instance.generate_random_special_characters()
# ran_special_char_and_letter = random_instance.generate_random_special_and_string_characters()
# ran_special_char_and_number = random_instance.generate_random_special_and_string_number()



