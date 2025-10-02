import math
import itertools
import random

def grams_to_ounces(grams):
    return grams / 28.3495231

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve_chickens_rabbits(num_heads, num_legs):
    rabbits = (num_legs - 2 * num_heads) // 2
    chickens = num_heads - rabbits
    return chickens, rabbits

def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    return [n for n in numbers if is_prime(n)]

def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0,0,7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

def histogram(nums):
    for num in nums:
        print('*' * num)

def guess_number_game():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses = 0
    guess = 0
    
    while guess != number:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
    
    print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
