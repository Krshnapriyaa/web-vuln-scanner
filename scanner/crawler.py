import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, base_url, max_pages=50, allowed_domain=None):
        self.base = base_url
        self.visited = set()
        self.to_visit = [base_url]
        self.max_pages = max_pages
        self.allowed_domain = allowed_domain or urlparse(base_url).netloc

    def get_links(self, url, resp_text):
        soup = BeautifulSoup(resp_text, "lxml")
        links = set()
        for a in soup.find_all("a", href=True):
            href = a['href']
            full = urljoin(url, href)
            parsed = urlparse(full)
            if parsed.netloc == self.allowed_domain:
                full = full.split('#')[0]
                links.add(full)
        return links

    def crawl(self):
        results = []
        while self.to_visit and len(self.visited) < self.max_pages:
            url = self.to_visit.pop(0)
            if url in self.visited:
                continue
            try:
                r = requests.get(url, timeout=8)
                if r.status_code != 200:
                    self.visited.add(url)
                    continue
                self.visited.add(url)
                results.append((url, r.text))
                links = self.get_links(url, r.text)
                for l in links:
                    if l not in self.visited and l not in self.to_visit:
                        self.to_visit.append(l)
            except Exception:
                self.visited.add(url)
        return results
