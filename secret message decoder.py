import random
import string

# Ask if user wants to code or decode 
userChoice = input("Enter 1 to code or Enter 2 to decode: ")

if userChoice == "1":
    message = input("Enter the message you want to code: ")
    encode = message.split(" ")

    # ans is the variable to store final coded message
    ans = []

    for word in encode: 
        if (len(word) >= 3):
            # a and b are variables that can generate 3 random words
            a = random.choices(string.ascii_lowercase, k=3)
            b = random.choices(string.ascii_lowercase, k=3)
            c = ''.join(a) + word[1:] + word[0] + ''.join(b)
            ans.append(c)
        else:
            ans.append(word)

    # Join the words back into a single string
    coded_message = " ".join(ans)

    print(f"Coded message: {coded_message}")

elif userChoice == "2":
    message = input("Enter the message you want to decode: ")
    decode = message.split(" ")  # Split the message for decoding
    decoded_message = []  # Create a list to store the decoded words
    
    for word in decode:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            decoded_message.append(stnew)
        else:
            decoded_message.append(word[::-1])
    
    decoded_message = " ".join(decoded_message)  # Join the words back into a single string
    print(f"Decoded message: {decoded_message}")

else:
    print("Invalid choice. Please enter 1 to code or 2 to decode.")
