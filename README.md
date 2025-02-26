# img-scrape
Code for an image-pulling bot using Python.

Requirements:
  - datetime
  - bs4
  - PIL
  - os
  - urllib.parse
  - os
  - requests
  - Python

A little project used to put something in my GitHub account. Meant to show off some of my Computer Science oriented skills with Python programming, as well as my Data oriented skills with data scraping and organization. img-scrape pulls all images from a website entered by the user by gathering "img-src"s using the find_all() function in bs4 (BeautifulSoup). It uses requests to access data from the website entered. Besides bs4 and requests, it also uses Image from PIL, urlparse from urllib.parse, datetime, and os for the purposes of saving Image data, parsing urls, getting the name for a save folder, and creating that save folder in /dump, respectively. 

# How to use:

Please download the entire directory as images downloaded while using img-scrape.py will be downloaded to a generated folder within the /dump folder in the directory.

Upon running img-scrape.py, you will be prompted to enter a full url link. This means including scheme ("https://"), subdomain, domin and domain extension (e.g.: "www.google.com", "www.en.wikipedia.org"), and net location or path. The images found on the page entered will be added to a generated folder based on the time the program is ran within the /dump folder in the directory. In the case an error occurs, an error message will be displayed and an error log will be generated in the folder previously mentioned within the /dump/ folder. Please send this to me! 
