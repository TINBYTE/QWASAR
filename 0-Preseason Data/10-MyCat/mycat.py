import sys

def main():
    if len(sys.argv) < 2:
        return
    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                print(f.read(), end='')
        except Exception as e:
            pass

if __name__ == "__main__":
    main()
