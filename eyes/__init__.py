from eyes import Eyes

if __name__ == '__main__':
    try:
        print(Eyes.banner())
        print(Eyes.menu())
        print('')
        Eyes.eyes()
    except KeyboardInterrupt:
        print("\nBye")
        exit(0)
else:
    from api import API
