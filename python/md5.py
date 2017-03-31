import hashlib

password = raw_input("Enter a string to hash: ")
print hashlib.md5(password).hexdigest()
