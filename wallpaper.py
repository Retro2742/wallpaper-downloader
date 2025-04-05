import requests
import sys
from bs4 import BeautifulSoup

def main():
    archives = []
    sources = []
    n = 1
    URL = "https://bingwallpaper.anerg.com/"
    page = requests.get(URL)
    if page.status_code != 200:
        sys.exit("Couldn't connect to the site.")
    soup = BeautifulSoup(page.content, "html.parser")
    container = soup.find_all("div", class_="col-3 col-lg-2 col-xl-1 py-1")
    for contain in container:
        link = contain.find("a")
        x = f"https://bingwallpaper.anerg.com{link.get("href")}"
        archives.append(x)
    for archive in archives:
        page1 = requests.get(archive)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        container1 = soup1.find_all("div", class_="col-md-6 col-lg-4 col-xl-3")
        for contain1 in container1:
            link1 = contain1.find("a")
            y = f"https://bingwallpaper.anerg.com{link1.get("href")}"
            sources.append(y)
    for source in sources:
        page2 = requests.get(source)
        soup2 = BeautifulSoup(page2.content, "html.parser")
        result = soup2.find("img", class_="img-fluid rounded")
        image = result["src"]
        with open(f"wallpaper {n}.jpg", "wb") as file:
            file.write(requests.get(image).content)
        n += 1

if __name__ == "__main__":
    main()