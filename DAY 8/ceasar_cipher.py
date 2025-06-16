import logo
print(logo.art)
alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
# text = input("Enter our message: \n").lower()
# shift = int(input("Type the shift number: \n"))

# def encrypt(original_text,shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabets.index(letter) + shift_amount
#         shifted_position  %= len(alphabets)
#         cipher_text += alphabets[shifted_position]
#     print(cipher_text) 
    
# def decrypt(original_text, shift_amount):
#     plain_text = ""
#     for letter in original_text:
#         shifted_position = alphabets.index(letter) - shift_amount
#         shifted_position %= len(alphabets)
#         plain_text += alphabets[shifted_position]
#     print(f"Plain text is {plain_text}")     
 
def ceasar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in original_text:
        if letter not in alphabets:
            output_text += letter
        
        shifted_position = alphabets.index(letter) + shift_amount
        shifted_position %= len(alphabets)
        output_text += alphabets[shifted_position]
    print(f"Here is {encode_or_decode}d message: {output_text}")  
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Enter our message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    
    ceasar(text,shift,direction)
    
    restart= input("Type 'yes' if you want to go again. otherwise type 'no'. \n").lower()
    if restart == "no":
        should_continue = False
        print("Ok Bye")
# encrypt(text,shift)    
# decrypt(text,shift)

# ceasar(text,shift,direction)
