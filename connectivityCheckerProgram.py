#site connectivity checker

#import urllib
#use urllib.request to get the data from the url
#write a function that takes a url
#returns a reponse

import urllib.request as urllib

def main(url):
    print("Checking connectivity  ")
    response=urllib.urlopen(url)
    print("Connected to " + url + "successfully")
    print("The response code was" + response.getcode())
print("This is a site connectivity checker program")
url_input=print("Input the Url of the site you want to check: ")
main(url_input)