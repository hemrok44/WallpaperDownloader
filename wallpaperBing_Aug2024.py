#! python3
# Wall paper Updater - Bing.com

import os, requests, bs4, cssutils, ctypes, string

url = "https://www.bing.com"        #starting URL
os.makedirs('BingWallpaper',  mode=0o777, exist_ok=True)  #store Wallpapaer in ./Bing wallpaper

# Download the page
res = requests.get(url)
res.raise_for_status()
# Find the URL of the wallpaper image
soup = bs4.BeautifulSoup(res.text, "html.parser")
imgTag = soup.find_all("link",limit=2)
if imgTag == []:
    print("Could Not Find image")
else:
    #downloaded tag example : [<div class="img" style="background-image: url(/th?id=OHR.RedRobin_EN-IN2250251453_1920x1080.jpg&amp;rf=LaDigue_1920x1080.jpg);"></div>]
    imgURL = imgTag[1].get("href")  
    #style = cssutils.parseStyle(imgStyle)  # parsing the found tag to select the internal backgroud-image property of the style selector
    #imgURL = style['background-image'] 
    #imgURL = imgURL.replace('url(', '').replace(')', '')   # removing extra data to obtain the url of the image
    # downloading the image
    #imgURL = print(imgStyle)
    imgRes = requests.get("https://www.bing.com"+imgURL)  
    # saving image to hard disk
    filename = ''.join((filter(lambda i: i not in string.punctuation, imgURL[11:20])))   # Extracting name from URL and removing punctuations from the name
    imageFile = open('BingWallpaper\\'+filename+'.jpg','wb')  # Saves the image to the folder BingWallpaper with the above filename and extension .jpg
    for chunk in imgRes.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    current_dir = os.path.abspath(os.getcwd())
    wallpaper_path = ""
    if current_dir.endswith("\\"):
        wallpaper_path = current_dir+"BingWallpaper\\"+filename+".jpg"
    else:
        wallpaper_path = current_dir+"\\BingWallpaper\\"+filename+".jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0,wallpaper_path, 0)
    print("Greaaatt Successs")
