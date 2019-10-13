# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:40:57 2019

@author: Chiu Sing Yan
"""

import bs4
import urllib.request
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#change target url of lecture video page here
start_url = "https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-004-computation-structures-spring-2017/c9/c9s2/"

#Open the target url and parse the html using BeautifulSoup4's html parser
def parseHTML(url):
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, "html.parser")

#Find all links with .mp4 and download the mp4 video, if "continue button" exists, open the link referenced by the button and repeat the process
def find_mp4_links(url):
    page_soup = parseHTML(url)
    apop_tags = page_soup.findAll("a",{"class":"poplink"})

    #find all .mp4 links and download them in the list of "a tags" with class "poplink"
    for apop_tag in apop_tags:
        if ".mp4" in apop_tag["href"]:
            print ("Downloading:")
            print (apop_tag["href"]+ "\n")
            mp4_url = apop_tag["href"]
            urlsplit = mp4_url.split("/")
            filename = urlsplit[len(urlsplit)-1]
            urllib.request.urlretrieve(apop_tag["href"], filename)

    #find continue button and "click" on it - retrieve the link and open the link, relaunch findmp4_links() with new url
    continue_btns = page_soup.findAll("li",{"id":"continue_btn"})
    if len(continue_btns)>0:
        a_tags = continue_btns[0].findAll("a")
        print ("Opening link:")
        print (a_tags[0]["href"]+ "\n")
        new_url = "https://ocw.mit.edu" + a_tags[0]["href"]
        find_mp4_links(new_url)
    else:
        print ("All done!\n")
        return

find_mp4_links(start_url)
