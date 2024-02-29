import re
import sys

# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# https://youtu.be/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s:=re.search(r'src="https?://www\.youtube\.com/embed/(\w+)?"',s):
        return f"https://youtu.be/{s.group(1)}"
    

if __name__ == "__main__":
    main()