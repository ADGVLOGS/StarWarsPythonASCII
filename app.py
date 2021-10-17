# Ashlin Darius Govindasamy 2021

import time
import os
from urllib.request import Request, urlopen

def ClearScreen():
        os.system('cls' if os.name == 'nt' else 'clear')

def FetchMovie():
        print('Downloading Star Wars ASCII Movie from adgstudios.co.za')
        url='https://adgstudios.co.za/sw1.txt'
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode('utf-8')
        with open("sw1.txt", "w") as text_file:
                text_file.write(webpage)

if os.path.exists("sw1.txt") == False:
        FetchMovie()
        ClearScreen()

def RenderMovieASCII():
	 try:
	        with open("sw1.txt") as file_in:
	            lines = []
	            for line in file_in:
	                lines.append(line)

	        for x in range(len(lines)):
	            if lines[x].strip('\n').isnumeric():
	                time.sleep(0.5)
	                ClearScreen()
	            else:
	                print(lines[x])

	 except Exception as e:
	        print('An error as occured:',e)

RenderMovieASCII()
