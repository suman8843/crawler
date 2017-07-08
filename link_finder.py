from html.parser import HTMLParser
from urllib import parse
from general import add_cve


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        cve_db = 'Exploit-DB/cve_db.txt'
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    #url = parse.urljoin(self.base_url, value)
                    url = value
                    print(url)
                    if 'www.exploit-db.com/exploits/' in url:
                        self.links.add(url)
                    if 'https://www.exploit-db.com/search/?action=search&cve=' in url:
                        add_cve('Exploit-DB', url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
