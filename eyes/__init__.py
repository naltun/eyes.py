from eyes import Eyes
from colorama import Style

if __name__ == '__main__':
    try:
        print(Eyes.banner())
        print(Eyes.menu())
        print('')
        Eyes.eyes()
    except KeyboardInterrupt:
        print("\nBye")
        print(Style.RESET_ALL)
        exit(0)
else:
    from api import API
