import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate_ipv4(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False
    return all(0 <= int(i) <= 255 for i in ip.split("."))

if __name__ == "__main__":
    main()