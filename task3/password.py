import secrets
import string
def create_pw(pw_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd = ''
    pw_strong = False
    while not pw_strong:
        pwd = ''.join(secrets.choice(alphabet) for i in range(pw_length))
        if (any(char in special_chars for char in pwd) and
            sum(char in digits for char in pwd) >= 2):
            pw_strong = True
    return pwd
if __name__ == '__main__':
    pw_length = int(input("Enter the desired password length: "))
    print(create_pw(pw_length))

