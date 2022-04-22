import os
from dotenv import load_dotenv
load_dotenv()

def number():
    var1 = os.getenv("ID")
    var2 = os.getenv("TOKEN")
    print(var1, var2)





if __name__ == "__main__":
    number()










