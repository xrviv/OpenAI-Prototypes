import hashlib

# Function to calculate MD5 hash of a file
def calculate_md5(file_path):
    with open(file_path, 'rb') as f:
        md5_hash = hashlib.md5()
        while chunk := f.read(4096):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

# Ask user to input the file location
file_path = input("Enter the file location: ")

# Ask user to input the MD5 checksum
downloaded_md5 = input("Enter the MD5 checksum: ")

# Calculate MD5 hash of the file
file_md5 = calculate_md5(file_path)

# Compare the MD5 hashes and print the result
if file_md5 == downloaded_md5:
    print('\033[92mMD5SUM Match\033[0m')  # Print in green font
else:
    print('MD5SUM Mismatch')
