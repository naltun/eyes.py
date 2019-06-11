"""This file contains the API for the Eyes class, which
is used for creating the CLI environment for eyes.py.
"""
from colorama import init, Fore, Style
from .api import API

# filter ANSI escape sequences from any STDOUT/STDERR and replace with Win32 calls
# this will have no effect if running this package on other platforms
init()

class Eyes:
    """This class holds the CLI API. All methods for prompting for
    and processing user input exists here.
    """

    # banner created with figlet.js (github.com/patorjk/figlet.js)
    @classmethod
    def banner(cls):
        """Prints the banner logo for eyes.py"""
        return Fore.LIGHTGREEN_EX + "______\n" \
            "|  ___|\n" \
            "| |__ _   _  ___  ___\n" \
            "|  __| | | |/ _ \\/ __|\n" \
            "| |__| |_| |  __/\\__ \\\n" \
            "\\____/\\__, |\\___||___/ " + Fore.WHITE + "v" + Fore.LIGHTRED_EX + "0.1beta" + Fore.LIGHTGREEN_EX + "\n" \
            "       __/ |\n" \
            "       |___/\n"


    @classmethod
    def menu(cls):
        """Prints the menu for interacting with eyes.py"""
        return Fore.WHITE + "1. Whois Lookup\n" \
            "2. DNS Lookup + Cloudflare Detector\n" \
            "3. Zone Transfer\n" \
            "4. Port Scan\n" \
            "5. HTTP Header Grabber\n" \
            "6. Honeypot Detector\n" \
            "7. Robots.txt Scanner\n" \
            "8. Link Grabber\n" \
            "9. IP Location Finder\n" \
            "10. Traceroute\n" \
            "11. Domain-to-IP Lookup\n" \
            "12. About program\n" \
            "13. Exit program"


    @classmethod
    def eyes(cls):
        """The features of eyes.py get called here"""
        choice = input('What do you want to do? ')

        if choice == '1':
            target = input('Enter a domain or IP address: ')
            print(API.whois(target))
            Eyes.display()

        elif choice == '2':
            target = input('Enter a domain: ')
            print(Fore.LIGHTRED_EX + API.dns(target))
            Eyes.display()

        elif choice == '3':
            domain = input('Enter a domain: ')
            print(API.zonetransfer(domain))
            Eyes.display()

        elif choice == '4':
            target = input('Enter a domain or IP address: ')
            print(API.portscan(target))
            Eyes.display()

        elif choice == '5':
            target = input('Enter a domain or IP address: ')
            print(API.getheader(target))
            Eyes.display()

        elif choice == '6':
            target = input('Enter IP address: ')
            print(API.honeypot(target))
            Eyes.display()

        elif choice == '7':
            answer = input('This feature makes a direct call to the target -- would you like to continue? [Y/n] ')
            if answer == 'y':
                target = input('Enter a domain (without protocol): ')
                print(API.robots(target))
                Eyes.display()
            elif answer == 'n':
                print('Going back to menu...')
                Eyes.display()
            else:
                print('Your choice is invalid.')
                Eyes.display()

        elif choice == '8':
            target = input('Enter URL (without protocol): ')
            print(API.getlinks(target))
            Eyes.display()

        elif choice == '9':
            target = input('Enter IP address: ')
            print(API.iplocate(target))
            Eyes.display()

        elif choice == '10':
            target = input('Enter a domain or IP address: ')
            print(API.traceroute(target))
            Eyes.display()

        elif choice == '11':
            target = input('Enter a domain: ')

            Eyes.display()

        elif choice == '12':
            print(API.about())
            Eyes.display()

        elif choice == '13':
            print('Bye')
            print(Style.RESET_ALL)
            exit(0)

        else:
            print('Your choice is invalid.')
            Eyes.display()


    @classmethod
    def display(cls):
        """Outputs the Eyes menu as well as prompt the user for menu item selection."""
        print("\n" + Eyes.menu() + "\n")
        print("\n" + Eyes.eyes())
