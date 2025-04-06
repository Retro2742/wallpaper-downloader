import requests
import sys
from bs4 import BeautifulSoup
from datetime import date, timedelta

def main():
    

    #Setting up all variables
    archives = []
    sources = []
    check = []
    n = 0
    

    #Getting a list of all the archives of wallpapers
    print("Gathering all archives!")
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


    #Checker function to check the start date
    date1 = archives[0].removeprefix("https://bingwallpaper.anerg.com/archive/us/")
    year = int(date1[0:4])
    month = int(date1[4:6])
    check1 = requests.get(archives[0])
    soupcheck = BeautifulSoup(check1.content, "html.parser")
    containercheck = soupcheck.find_all("div", class_="col-md-6 col-lg-4 col-xl-3")
    for containcheck in containercheck:
        linkcheck = containcheck.find("a")
        check.append(f"https://bingwallpaper.anerg.com{linkcheck.get("href")}")
    day = int(len(check))
    start = date(year, month, day)


    #Getting a list of all the images
    print("Gathering every image!")
    for archive in archives:
        page1 = requests.get(archive)
        soup1 = BeautifulSoup(page1.content, "html.parser")
        container1 = soup1.find_all("div", class_="col-md-6 col-lg-4 col-xl-3")
        for contain1 in container1:
            link1 = contain1.find("a")
            y = f"https://bingwallpaper.anerg.com{link1.get("href")}"
            sources.append(y)


    #Getting every image source
    print("Downloading all images now!")
    for source in sources:
        page2 = requests.get(source)
        soup2 = BeautifulSoup(page2.content, "html.parser")
        result = soup2.find("img", class_="img-fluid rounded")
        image = result["src"]
        title = start - timedelta(n)
        with open(f"{title}-{source.removeprefix("https://bingwallpaper.anerg.com/detail/us/")}.jpg", "wb") as file:
            file.write(requests.get(image).content)
        n += 1


if __name__ == "__main__":
    main()
