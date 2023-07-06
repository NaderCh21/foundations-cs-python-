# # 1. Function to calculate factorial
# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     result = 1
#     for i in range(1, n + 1):
#       result *= i
#     return result


# # Example :
# number = int(input("Enter an integer: "))
# result = factorial(number)
# print(f"The factorial of {number} is: {result}")

# print()
# print("#----------------------------------------------------------#")


# # 2.Function to find divisors
# def find_divisors(n):
#   divisors = []
#   for i in range(1, n + 1):
#     if n % i == 0:
#       divisors.append(i)
#   return divisors


# # Example :
# number = int(input("Enter an integer: "))
# result = find_divisors(number)
# print(f"The divisors of {number} are: {result}")

# print("#----------------------------------------------------------#")


# # 3.Function to reverse a string
# def reverse_string(s):
#   reversed_str = ""
#   for i in range(len(s) - 1, -1, -1):
#     reversed_str += s[i]
#   return reversed_str


# # Example :
# string = input("Enter a string: ")
# result = reverse_string(string)
# print(f"The reversed string is: {result}")

# print("#----------------------------------------------------------#")


# # 4. Function to filter even numbers from a list
# def filter_even_numbers(numbers):
#   even_numbers = []
#   for num in numbers:
#     if num % 2 == 0:
#       even_numbers.append(num)
#   return even_numbers


# # Example :
# nums = input("Enter a list of numbers, separated by commas: ").split(",")
# numbers = [int(num) for num in nums]
# result = filter_even_numbers(numbers)
# print(f"The even numbers are: {result}")

# print("#----------------------------------------------------------#")


# # 5.Function to check for a strong password
# def check_strong_password(password):
#   if len(password) < 8:
#     return "Weak password"
#   has_uppercase = False
#   has_lowercase = False
#   has_digit = False
#   has_special_char = False
#   for char in password:
#     if char.isupper():
#       has_uppercase = True
#     elif char.islower():
#       has_lowercase = True
#     elif char.isdigit():
#       has_digit = True
#     elif char in ['#', '?', '!', '$']:
#       has_special_char = True
#   if has_uppercase and has_lowercase and has_digit and has_special_char:
#     return "Strong password"
#   else:
#     return "Weak password"


# # Example usage:
# password = input("Enter a password: ")
# result = check_strong_password(password)
# print(result)

# print("#----------------------------------------------------------#")


# # Bonus : Function to check for a valid IPv4 address
# def is_valid_ipv4_address(ip):
#   octets = ip.split(".")
#   if len(octets) != 4:
#     return False
#   for octet in octets:
#     if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
#       return False
#     if len(octet) > 1 and octet[0] == '0':
#       return False
#   return True


# # Example:
# ip_address = input("Enter an IP address: ")
# result = is_valid_ipv4_address(ip_address)
# if result:
#   print("Valid IPv4 address")
# else:
#   print("Invalid IPv4 address")
