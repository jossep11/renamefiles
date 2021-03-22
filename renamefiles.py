import os
import random

used_random = []

path = os.chdir("C:\\Users\\JP\\Music\\trap en español")

for filename in os.listdir():
    n = random.randint(0, len(os.listdir()))
    while n in used_random:
        n = random.randint(0, len(os.listdir()))
    used_random.append(n)
    os.rename(filename, f"sup{n}_.mp3")
