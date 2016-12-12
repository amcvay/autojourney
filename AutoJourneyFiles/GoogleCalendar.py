############################ a script to make API requests and print the returned data #############################

# 'requests' is a module (or 'library') that lets us make API requests

import requests

from time import gmtime, strftime

localTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

print localTime

localTimeSplit = localTime.split(" ",1)

localDate = localTimeSplit[0]

#localHour = localTimeSplit[1]

#localMinute =

#localSecond =

#print localHour

#"T" + localHour + "%3A" + localMinute + "%3A" + localSecond + "%2B00%3A00"
#2016-11-22T16:46:27+00:00

APIkey = "AIzaSyA4kX09MngnaOeO2BtQescqIOB_YCjEGlI"

APIparam1 = 'autojourney1@gmail.com'

requestURL = "https://www.googleapis.com/calendar/v3/calendars/" + APIparam1 + "/events?alwaysIncludeEmail=true&orderBy=startTime&showDeleted=false&showHiddenInvitations=true&singleEvents=true&timeMin=" + localDate + "T00%3A00%3A00%2B00%3A00&key=" + APIkey

print requestURL

APIresponse = requests.get(requestURL)



# Convert the response into a dictionary, so you can easily access the information you want
data = APIresponse.json()

#print data

events = data['items'][0]

eventName = events['summary']

eventLocation = events['location']

eventStart = events['start']['dateTime']

eventEnd = events['end']['dateTime']


print eventName

print eventLocation

print eventStart

print eventEnd

splitDateTime = str(eventStart)
#
# def finalTime(splitDateTime):
#
#     a.split("T")
#     b.split("-")
#
# finalTime(splitDateTime)
#
# print finalTime()

#timeSplitList = splitDateTime.split("T")

#finalTime = splitDateTime.split("-")

#finalTimeSplit = timeSplitList.split("-")

#print timeSplitList[1]

#print finalTime



