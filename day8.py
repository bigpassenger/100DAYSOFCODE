# from math import ceil
# def paincalcu(height, width, cover):
#     can = (height * width)/cover
#     print(f"you'll need {ceil(can)} cans of paint")
# height_i = int(input())
# width_i = int(input())
# cover_i = 5
# paincalcu(height=height_i, width = width_i,cover = cover_i)
#######################################################################
# def prime(num):
#     for i in range(1,num):
#         if num // i == 0 and num != i:
#             return False
# num = int(input())
# var = prime(num)
# if var == False:
#     print("your number isn't prime")
# elif var == None:
#     print("your number is a prime")
######################################################################
# alphabet = ['a','b','c' ,'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']*2
# print(alphabet)
# def encode(text,shift):
#     str =''
#     for i in text:
#         shifted = alphabet.index(i) + shift
#         str = str +alphabet[shifted]
#     return str
# def decode(text,shift):
#     str =''
#     for i in text:
#         shifted = alphabet.index(i) - shift
#         str = str +alphabet[shifted]
#     return str

# while True:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input('type your message:\n').lower()
#     shift = int(input('enter the shift number:\n'))
#     if direction == 'encode':
#         print(encode(text,shift))
#     elif direction == 'decode':
#         print(decode(text,shift))
#     else:
#         continue