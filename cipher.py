alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction=="encode":
    def encrypt(shift,guess):
        cipher_text=""
        for letter in text:
            global encrypted
            x=alphabet.index(letter)
            encryption_shift=x+shift
            encrypted=alphabet[encryption_shift]
            cipher_text +=alphabet[encryption_shift]
        print(f"Encoded Text:{cipher_text}") 
    encrypt(shift,guess=text)
else:
    print("plz Enter correct direction")  
    
    
    
    
    
      
 # decrypt
if direction=="decode":
    def decrypt(shift,guess):
        decryoted=""
        for letter in text:
            x=alphabet.index(letter)
            encryption_shift=x-shift
            decryoted=alphabet[encryption_shift]
        print(f"Decrypted TEXT: {decryoted}")
    decrypt(shift,guess=encrypted)
