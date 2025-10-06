
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters=int(input("How many letters you want in your passowrd?"))

nr_numbers=int(input("How many letters you want in your passowrd?"))

nr_symbols=int(input("How many letters you want in your passowrd?"))

letters_list=random.choices(letters, k=nr_letters)
numbers_list=random.choices(numbers, k=nr_numbers)
symbols_list=random.choices(symbols, k=nr_symbols)

final_letters=letters_list
final_numbers=numbers_list
final_symbols=symbols_list

password=final_letters+final_numbers+final_symbols
random.shuffle(password)

Final_password=""
    
for number in password:
    Final_password+=number

print(f"your password is:{Final_password}")


