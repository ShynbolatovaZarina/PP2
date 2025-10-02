from tasks import grams_to_ounces, reverse_words, filter_prime, sphere_volume

# Пример использования нескольких функций из tasks.py

print("1) 100 grams in ounces:")
print(grams_to_ounces(100))

print("\n2) Reverse words:")
sentence = "We are ready"
print(f"Original: {sentence}")
print(f"Reversed: {reverse_words(sentence)}")

print("\n3) Filter prime numbers from a list:")
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)
print("Primes:", filter_prime(numbers))

print("\n4) Sphere volume with radius 3:")
print(sphere_volume(3))
