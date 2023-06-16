# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
# text is the attribute of the response object r.
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
# after the execution of the bellow step you can access the specific portion of strings.
# that is title,h1,h2 and so many tags ant its strings.
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
# prettify()  It adds indentation/insert spac at the 
# begining each line and line breaks to the document structure,
#  making it more human-readable and visually organized.
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)