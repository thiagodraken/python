from thumbnails import get_thumbnail
from flask import Flask

app = Flask(__name__)
get_thumbnail('https://blog.fotolia.com/br/files/2017/09/fotolia_117306153-.jpg', '300x300', crop='center')