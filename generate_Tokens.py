# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:47:32 2023

@author: khoso
"""
import secrets

# Create 20 files with 5,000 tokens each
for i in range(20):
    with open(f"tokens_{i}_5000.txt", "w") as f:
        for j in range(5000):
            token = secrets.token_hex(16)
            f.write(token + "\n")

# Create 20 files with 10,000 tokens each
for i in range(20):
    with open(f"tokens_{i}_10000.txt", "w") as f:
        for j in range(10000):
            token = secrets.token_hex(16)
            f.write(token + "\n")


import secrets
import string

# Define the length of the tokens and the number of tokens to generate
TOKEN_LENGTH = 12
NUM_TOKENS = 300

# Define the set of characters to use for generating the tokens
TOKEN_CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits

# Generate the tokens
tokens = []
while len(tokens) < NUM_TOKENS:
    token = ''.join(secrets.choice(TOKEN_CHARS) for i in range(TOKEN_LENGTH))
    if token not in tokens:
        tokens.append(token)

# Print the tokens
print(tokens)
