"""This file contains the core API for eyes.py."""
import socket
import requests

SHODAN_KEY = None

class API:
    """This class contains the core API for for the eyes.py package.
    Every method within API() is a classmethod, eg. `API.<classmethod>()'
    """

    @classmethod
    def whois(self, target):
        """Takes the user specified domain or IP address and requests a WHOIS report."""
        whois = 'http://api.hackertarget.com/whois/?q=' + target
        return requests.get(whois).text


    @classmethod
    def dns(self, target):
        """Takes the user specified domain or IP address and performs a Cloudflare detection scan."""
        dns = 'http://api.hackertarget.com/dnslookup/?q=' + target
        req = requests.get(dns)
        res = None
        if 'cloudflare' in req.text:
            res = "\n**Cloudflare detected**"
        else:
            res = f"{target} is *not* protected by Cloudflare"

        return res


    @classmethod
    def zonetransfer(self, target):
        """Takes the user specified domain or IP address and performs a zone transfer scan."""
        zone = 'http://api.hackertarget.com/zonetransfer/?q=' + target
        return requests.get(zone).text


    @classmethod
    def portscan(self, target):
        """Takes the suer specified domain or IP address and performs a port scan."""
        ports = 'http://api.hackertarget.com/nmap/?q=' + target
        return requests.get(ports).text


    @classmethod
    def getheader(self, target):
        """Takes the user specified domain or IP address and grabs the HTTP header."""
        header = 'http://api.hackertarget.com/httpheaders/?q=' + target
        return requests.get(header).text


    @classmethod
    def honeypot(self, target):
        """Takes the user specified IP address and performs a honeypot probability scan.
        Note, this requires a valid shodan.io key.
        """
        if not SHODAN_KEY:
            return "This feature requires a Shodan API key to be set in `eyes/api.py:4. Please do that."
        honey = f"https://api.shodan.io/labs/honeyscore/{target}?key={SHODAN_KEY}"
        phoney = requests.get(honey).text
        prob = None
        if '0.0' in phoney:
            prob = 'Honeypot Probability: 0%'
        elif '0.1' in phoney:
            prob = 'Honeypot Probability: 10%'
        elif '0.2' in phoney:
            prob = 'Honeypot Probability: 20%'
        elif '0.3' in phoney:
            prob = 'Honeypot Probability: 30%'
        elif '0.4' in phoney:
            prob = 'Honeypot Probability: 40%'
        elif '0.5' in phoney:
            prob = 'Honeypot Probability: 50%'
        elif '0.6' in phoney:
            prob = 'Honeypot Probability: 60%'
        elif '0.7' in phoney:
            prob = 'Honeypot Probability: 70%'
        elif '0.8' in phoney:
            prob = 'Honeypot Probability: 80%'
        elif '0.9' in phoney:
            prob = 'Honeypot Probability: 90%'
        elif '1.0' in phoney:
            prob = 'Honeypot Probability: 100%'

        return prob


    @classmethod
    def robots(self, target):
        """Takes the user specified domain or IP address and reads the contents of its robots.txt file."""
        robot = f"http://{target}/robots.txt"
        return requests.get(robot).text


    @classmethod
    def getlinks(self, target):
        """Takes the user specified domain or IP address and retrieves all links."""
        page = 'https://api.hackertarget.com/pagelinks/?q=http://' + target
        return requests.get(page).text

    @classmethod
    def iplocate(self, target):
        """Takes the user specified IP address and retrieves location information from its server."""
        geo = f"http://ipinfo.io/{target}/geo"
        return requests.get(geo).text


    @classmethod
    def traceroute(self, target):
        """Takes the user specified domain or IP address and performs a traceroute review."""
        trace = 'https://api.hackertarget.com/mtr/?q=' + target
        return requests.get(trace).text


    @classmethod
    def getip(target):
        """Takes the user specified domain name and returns its IP address."""
        ip_addr = socket.gethostbyname(target)
        return f"{target}'s IP address is {ip_addr}."


    @classmethod
    def about(self):
        """Prints an 'about the program' message."""
        return "This program was created by Noah Altunian, and was adapted " \
                "from github.com/naltun/eyes.sh, which was adapted from " \
                "github.com/s0md3v/ReconDog. It is licensed under the GNU GPLv2."
