# MIT Lecture Video Scraper
I created this Python script to automatically download lecture videos from courses on the MIT OpenCourseWare website (https://ocw.mit.edu/index.htm).

## Motivation
The MIT OpenCourseWare website provides lecture videos of various MIT courses. All videos are free to download, but one need to go through many clicks in order to download all videos of a certain course. This Python script serves to automate this process by using the BeautifulSoup (a library for pulling data out of HTML and XML) and urllib libraries.

## Dependencies
This script requires the Anaconda environment which can be downloaded here: https://www.anaconda.com/distribution/

## Instruction for Windows
1. Put Videoscraper.py in your target video directory.
2. Open Videoscraper.py in any code editor and revise the value of start_url to the url of the lecture video page of your desired course. For example:
```
start_url = "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c9/c9s2/"
```
3. Save Videoscraper.py.
4. Launch an Anaconda command prompt.
5. Run the script with the command:
```
python videoscraper.py
```
6. Videos will be downloaded to the same directory as Videoscraper.py.
