import urllib.request
# open a connection to a URL using urllib
from django.shortcuts import render
class dataview():
    webUrl  = urllib.request.urlopen('https://cricapi.com/api/matches?apikey=ekd2Fs920CRZE0MWqtB5c9Eg9oP2')
    data = webUrl.read()
object=dataview()

#get the result code and print it
print ("result code: " + str(object.webUrl.getcode()))

# read the data from the URL and print it
#data = object.webUrl.read()
print (object.data)
def postinput(request):
    return render(request,'ui.html')