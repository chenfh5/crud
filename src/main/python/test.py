import os
import sys

import django


def main():
    print("Hello, World!")
    print(sys.version)
    print(os.getcwd())
    print(django.VERSION)
    print(django.get_version())


if __name__ == "__main__":
    main()
