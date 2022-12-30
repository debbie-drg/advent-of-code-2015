import sys
from hashlib import md5

def password(secret_key: str, number_leading: int):
    index = 0
    leading = "0" * number_leading
    while True:
        index += 1
        current_hash = md5((secret_key + str(index)).encode()).hexdigest()
        if current_hash[0:number_leading] == leading:
            return index

if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = "input.txt"
    secret_key = open(file_name).read().strip()

    print(f"The passowrd is {password(secret_key, 5)}.")
    print(f"If instead we use 6 zeroes, it's {password(secret_key, 6)}.")
