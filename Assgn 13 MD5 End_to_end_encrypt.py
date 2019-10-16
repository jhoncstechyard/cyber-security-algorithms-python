# Python 3 code to demonstrate the
# working of MD5 (byte - byte)

import hashlib

# encoding GeeksforGeeks using md5 hash
# function
result = hashlib.md5(b'GeeksforGeeks')

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.digest())

# initializing string
str = "GeeksforGeeks"

# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())