import getpass
import bcrypt

if __name__ == "__main__":
    password = getpass.getpass("password: ")
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    print(hashed_password.decode())