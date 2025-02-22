import sys

def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1] 
        greet(name)
    else:
        print("Usage: python b.py <name>")
