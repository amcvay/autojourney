import requests

#Importing geo-location converter

from geopy.geocoders import Nominatim

#Getting the local time

from time import gmtime, strftime

localTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

print localTime

localTimeSplit = localTime.split(" ",1)

localDate = localTimeSplit[0]



#The Request for Calendar Data

calAPIkey = "AIzaSyA4kX09MngnaOeO2BtQescqIOB_YCjEGlI"

calAPIparam1 = 'autojourney1@gmail.com'

calrequestURL = "https://www.googleapis.com/calendar/v3/calendars/" + calAPIparam1 + "/events?alwaysIncludeEmail=true&orderBy=startTime&showDeleted=false&showHiddenInvitations=true&singleEvents=true&timeMin=" + localDate + "T00%3A00%3A00%2B00%3A00&key=" + calAPIkey

print calrequestURL

calAPIresponse = requests.get(calrequestURL)

calData = calAPIresponse.json()



#Grabbing the JSON data

events = calData['items'][0]

eventName = events['summary']

eventLocation = events['location']

eventStart = events['start']['dateTime']

eventEnd = events['end']['dateTime']



#Converting address into geolocation

#geolocator = Nominatim()

#geoLocation = geolocator.geocode()

#print((geoLocation.latitude, location.longitude))



#The request for Travel Data

traAPIkey = "523cf6228063676f022e1c9a8a2e4841" # Stick your API key in here as a string

traAPIparam1 = "51.501571,0.005531" # Put any parameters you need to specify for the API request in here
traAPIparam2 = "51.5185610,-0.1437990"

# Find out from your chosen API's documentation what the API request URL is, and stick your API parameters
traRequestURL = "https://api.tfl.gov.uk/Journey/JourneyResults/"+traAPIparam1+"/to/"+traAPIparam2+"?nationalSearch=False&timeIs=Departing&journeyPreference=LeastTime&walkingSpeed=Average&cyclePreference=None&alternativeCycle=False&alternativeWalking=True&applyHtmlMarkup=False&useMultiModalCall=False&walkingOptimization=False&app_id=1a2ae856&app_key="+traAPIkey
                                                      #APIparam2+

# Make your API request!
traAPIresponse = requests.get(traRequestURL)

# Convert the response into a dictionary, so you can easily access the information you want
traData = traAPIresponse.json()

print traRequestURL

journeys = traData['journeys'][0]

journeyTime = journeys['duration']

journeyArrival = journeys['arrivalDateTime']



#Printing the Information we need

print journeyTime

print journeyArrival

print eventName

print eventLocation

print eventStart    

if journeyArrival > eventStart:

    print 'You are going to be late'