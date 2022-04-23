import os
from dotenv import load_dotenv
load_dotenv()


def number():
    _var1 = os.getenv("NAME")
    _var2 = os.getenv("TOKEN")
    _var3 = os.getenv("ID")
    print(f"{_var1}\n",f"{_var2}\n", f"{_var3}\n")
    print(os.environ)
    print("some issues added")
    print("next commit")
    print("testing git pull on master")



if __name__ == "__main__":
    number()










