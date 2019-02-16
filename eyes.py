#!/usr/bin/env python3

import requests
import socket

class Eyes:
    
    # banner created with figlet.js (github.com/patorjk/figlet.js)
    @classmethod
    def banner(self):
        """Prints the banner logo for eyes.py"""
        print("______\n"
            "|  ___|\n"
            "| |__ _   _  ___  ___\n"
            "|  __| | | |/ _ \\/ __|\n"
            "| |__| |_| |  __/\\__ \\\n"
            "\\____/\\__, |\\___||___/ v0.1beta\n"
            "       __/ |\n"
            "       |___/")
    
    @classmethod
    def menu(self):
        """Prints the menu for interacting with eyes.py"""
        print("1. Whois Lookup\n"
            "2. DNS Lookup + Cloudflare Detector\n"
            "3. Zone Transfer\n"
            "4. Port Scan\n"
            "5. HTTP Header Grabber\n"
            "6. Honeypot Detector\n"
            "7. Robots.txt Scanner\n"
            "8. Link Grabber\n"
            "9. IP Location Finder\n"
            "10. Traceroute\n"
            "11. Domain-to-IP Lookup\n"
            "12. About program\n"
            "13. Exit program")

    @classmethod
    def eyes(self):
        """The features of eyes.py get called here"""
        choice = input('What do you want to do? ')

        if choice == '1':
            target = input('Enter a domain or IP address: ')
            whois = 'http://api.hackertarget.com/whois/?q=' + target
            req = requests.get(whois)
            print(req.text)
            Eyes.display()

        elif choice == '2':
            target = input('Enter a domain: ')
            dns = 'http://api.hackertarget.com/dnslookup/?q=' + target
            req = requests.get(dns)
            print('')
            if 'cloudflare' in req.text:
                print('**Cloudflare detected**')
            else:
                print("{} is *not* protected by Cloudflare".format(target))
            Eyes.display()

        elif choice == '3':
            domain = input('Enter a domain: ')
            zone = 'http://api.hackertarget.com/zonetransfer/?q=' + domain
            req = requests.get(zone)
            print(req.text)
            Eyes.display()
        
        elif choice == '4':
            target = input('Enter a domain or IP address: ')
            ports = 'http://api.hackertarget.com/nmap/?q=' + target
            req = requests.get(ports)
            print(req.text)
            Eyes.display()
        
        elif choice == '5':
            target = input('Enter a domain or IP address: ')
            header = 'http://api.hackertarget.com/httpheaders/?q=' + target
            req = requests.get(header)
            print(req.text)
            Eyes.display()

        elif choice == '6':
            target = input('Enter IP address: ')
            honey = 'https://api.shodan.io/labs/honeyscore/{}?key='.format(target)
            phoney = requests.get(honey).text
            if '0.0' in phoney:
                print('Honeypot Probability: 0%')
            elif '0.1' in phoney:
                print('Honeypot Probability: 10%')
            elif '0.2' in phoney:
                print('Honeypot Probability: 20%')
            elif '0.3' in phoney:
                print('Honeypot Probability: 30%')
            elif '0.4' in phoney:
                print('Honeypot Probability: 40%')
            elif '0.5' in phoney:
                print('Honeypot Probability: 50%')
            elif '0.6' in phoney:
                print('Honeypot Probability: 60%')
            elif '0.7' in phoney:
                print('Honeypot Probability: 70%')
            elif '0.8' in phoney:
                print('Honeypot Probability: 80%')
            elif '0.9' in phoney:
                print('Honeypot Probability: 90%')
            elif '1.0' in phoney:
                print('Honeypot Probability: 100%')
            else:
                print('Something may have gone wrong checking honeypot probability.')
            
            Eyes.display()
        
        elif choice == '7':
            answer = input('This feature makes a direct call to the target -- would you like to continue? [Y/n] ')
            if answer == 'y':
                target = input('Enter a domain (without protocol): ')
                robot = 'http://{}/robots.txt'.format(target)
                req = requests.get(robot)
                print(req.text)
                Eyes.display()
            elif answer == 'n':
                print('Going back to menu...')
                Eyes.display()
            else:
                print('Your choice is invalid.')
                Eyes.display()

        elif choice == '8':
            target = input('Enter URL (without protocol): ')
            page = 'https://api.hackertarget.com/pagelinks/?q=http://' + target
            req = requests.get(page)
            print(req.text)
            Eyes.display()

        elif choice == '9':
            target = input('Enter IP address: ')
            geo = 'http://ipinfo.io/{}/geo'.format(target)
            req = requests.get(geo)
            print(req.text)
            Eyes.display()
        
        elif choice == '10':
            target = input('Enter a domain or IP address: ')
            trace = 'https://api.hackertarget.com/mtr/?q=' + target
            req = requests.get(trace)
            print(req.text)
            Eyes.display()

        elif choice == '11':
            target = input('Enter a domain: ')
            ipAddr = socket.gethostbyname(target)
            print("{}'s IP address is {}.".format(target, ipAddr))
            Eyes.display()
        
        elif choice == '12':
            print("This program was created by Noah Altunian, and was adapted " \
                "from github.com/naltun/eyes.sh, which was adapted from " \
                "github.com/s0md3v/ReconDog. It is licensed under the GNU GPLv2.")
        
        elif choice == '13':
            print('Bye')
            exit(0)
        
        else:
            print('Your choice is invalid.')
            Eyes.display()

    @classmethod
    def display(self):
        print('')
        Eyes.menu()
        print('')
        Eyes.eyes()

if __name__ == '__main__':
    Eyes.banner()
    Eyes.menu()
    print('')
    Eyes.eyes()
