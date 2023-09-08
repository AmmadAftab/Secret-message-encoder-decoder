# Secret-message-encoder-decoder
Randomized Message Coder and Decoder
This Python script allows users to either encode or decode a message using a randomized algorithm. The code is designed to provide a fun and unique way to obscure and reveal text.

How to Use:
Run the Script:

Execute the Python script in an environment with a Python interpreter installed.
Choose Operation:

Upon running, the user will be prompted to enter either 1 for encoding or 2 for decoding.
Encoding:

If 1 is chosen, the user is prompted to input the message they want to code.

The script will then apply a random encoding algorithm to each word in the input message. For words with three or more characters, it generates two random three-letter strings and reorders the word. For shorter words, they are left unchanged.

The final coded message is displayed.

Decoding:

If 2 is chosen, the user is prompted to input the message they want to decode.

The script will apply the reverse of the encoding algorithm. For words with three or more characters, it reverses the reordering process. For shorter words, they are reversed.

The final decoded message is displayed.

Example Usage:
Encoding:

Enter 1 to code or Enter 2 to decode: 1
Enter the message you want to code: Hello, world!
Coded message: lzkHe o,lrwd!
Decoding:

Enter 1 to code or Enter 2 to decode: 2
Enter the message you want to decode: lzkHe o,lrwd!
Decoded message: Hello, world!
Notes:
The code utilizes the Python random module for generating random strings, and string module for string manipulations.

For words with three or more characters, the encoding algorithm randomizes the position of the first and last character, while keeping the middle characters intact.

Decoding reverses this process.

Words with less than three characters are left unchanged.

Invalid choices (other than 1 or 2) prompt a message indicating an invalid input.

Author:
[AMMAD AFTAB]
[ammadaftab16@gmail.com]
https://github.com/AmmadAftab
Date:
9 Septembre 2023

License:
This code is released under the MIT License.
