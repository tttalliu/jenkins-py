import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
    names = sys.argv[1:]
    for name in names:
        greet(name)
    else:
        print("Write name")
