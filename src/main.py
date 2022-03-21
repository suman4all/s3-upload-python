import os
from dotenv import load_dotenv


load_dotenv()


def main():
    print(os.getenv('LOGLEVEL'))
    print("hello world")

main()
