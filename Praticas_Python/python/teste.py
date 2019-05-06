from bs4 import BeautifulSoup #Import stuff
import requests
from flask import Flask
app = Flask(__name__)

def getImages(url):
    r  = requests.get(url) #Download website source

    data = r.text  #Get the website source as text

    soup = BeautifulSoup(data) #Setup a "soup" which BeautifulSoup can search

    links = []

    for link in soup.find_all('img'):  #Cycle through all 'img' tags
        imgSrc = link.get('src')   #Extract the 'src' from those tags
        links.append(imgSrc)    #Append the source to 'links'

    return links  #Return 'links'

@app.route('/<site>')
def page(site):
    image = getImages("http://" + site)[0] #Here I find the 1st image on the page
    if image[0] == "/":
        image = "http://" + site + image  #This creates a URL for the image
    return "<img src=%s></img>" % image  #Return the image in an HTML "img" tag

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  #Run the Flask webserver