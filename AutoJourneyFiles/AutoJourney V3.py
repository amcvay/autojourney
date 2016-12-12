import requests

# Importing geo-location converter

from geopy.geocoders import Nominatim

# Getting the local time

import time

from time import gmtime, strftime

# Defining the two counters for use in sending an email once and stopping the loop from running

count = 0

stop = 0

# The While Loop to keep checking if the user is late

while True:

    # Getting the local time

    localTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # print localTime

    # Splitting Local Date and Time up then creating a variable for each

    localTimeSplit = localTime.split(" ", 1)

    localDate = localTimeSplit[0]

    # The Request for Calendar Data

    calAPIkey = "AIzaSyA4kX09MngnaOeO2BtQescqIOB_YCjEGlI"

    calAPIparam1 = 'autojourney1@gmail.com'

    calrequestURL = "https://www.googleapis.com/calendar/v3/calendars/" + calAPIparam1 + "/events?alwaysIncludeEmail=true&orderBy=startTime&showDeleted=false&showHiddenInvitations=true&singleEvents=true&timeMin=" + localDate + "T00%3A00%3A00%2B00%3A00&key=" + calAPIkey

    # print calrequestURL

    # The Google Calendar API Response

    calAPIresponse = requests.get(calrequestURL)

    calData = calAPIresponse.json()

    # Grabbing the JSON data

    events = calData['items'][0]

    eventName = events['summary']

    eventLocation = events['location']

    eventStart = events['start']['dateTime']

    eventEnd = events['end']['dateTime']

    # Converting address into geolocation

    #geolocator = Nominatim()

    #geoLocation = geolocator.geocode(str(eventLocation))



    #print((geoLocation.latitude, geoLocation.longitude))



    # The request for Travel Data

    traAPIkey = "523cf6228063676f022e1c9a8a2e4841"  # Stick your API key in here as a string

    traAPIparam1 = "51.501571,0.005531"  # Put any parameters you need to specify for the API request in here
    traAPIparam2 = "51.5185610,-0.1437990"

    # Find out from your chosen API's documentation what the API request URL is, and stick your API parameters
    traRequestURL = "https://api.tfl.gov.uk/Journey/JourneyResults/" + traAPIparam1 + "/to/" + traAPIparam2 + "?nationalSearch=False&timeIs=Departing&journeyPreference=LeastTime&walkingSpeed=Average&cyclePreference=None&alternativeCycle=False&alternativeWalking=True&applyHtmlMarkup=False&useMultiModalCall=False&walkingOptimization=False&app_id=1a2ae856&app_key=" + traAPIkey
    # APIparam2+

    # Makes the TFL API request
    traAPIresponse = requests.get(traRequestURL)

    # Converts the TFL API Response into a dictionary

    traData = traAPIresponse.json()

    #print traRequestURL

    # Grabbing the specific pieces of information we need from the TFL API

    journeys = traData['journeys'][0] # Entering the DATA scope

    journeyTime = journeys['duration'] # How long the journey will take

    journeyArrival = journeys['arrivalDateTime'] # The time the user will arrive at their location

    # Printing the Information we need

    # print journeyTime
    #
    # print journeyArrival
    #
    # print eventName
    #
    # print eventLocation
    #
    # print eventStart

    # A split to get the arrival time of the current journey without the date

    stringJourneyArrival = str(journeyArrival)

    splitJourneyArrival = stringJourneyArrival.split('T')

    # The function to send an email through mailgun

    def send_simple_message():
        return requests.post(
            "https://api.mailgun.net/v3/sandbox7875eda4e7e645bf99c2d899559aac32.mailgun.org/messages",
            auth=("api", "key-acae674cc60339a3b290916594fb0f2a"),
            data={"from": "<mailgun@sandbox7875eda4e7e645bf99c2d899559aac32.mailgun.org>",
                  "to": ["a.mcvay@students.rave.ac.uk"],
                  "subject": "Sorry!",
                  "text": "Sorry this person is going to be late to " + eventName + " and will arrive at " + splitJourneyArrival[1] + ". We are very sorry about this :("})


    # An if statement to check if journey arrival time is earlier than the event start time

    if journeyArrival < eventStart:

        if (stop < 1):

            stop = stop + 1

            print 'You are on time!'

            print 'Your event at ' + str(eventLocation).split(',')[0] + ', ' + str(eventLocation).split(',')[1] + ' will start at ' + str(eventStart).split('T')[1].strip('Z') + '. Your journey will take ' + str(journeyTime) + ' minutes and if you leave now you will arrive at ' + str(journeyArrival).split('T')[1]

    # An if statement to check if journey arrival time is later than the event start time

    if journeyArrival > eventStart:

        # A count to ensure the email and message on send once

        if (count < 1):

            count = count + 1

            print 'You are going to be late and will arrive at ' + splitJourneyArrival[1].strip('Z') + ' I have emailed the person you are meeting for you :)'

            send_simple_message()

        # A count so if you've sent an email and received a later message but the arrival time changes, it will let you know that you are now on time

        if journeyArrival < eventStart:

            if (count < 2):

                count = count + 1

                print 'You are now on time :)'


    # Makes the while loop run every 10 seconds to check if the user is late

    time.sleep(10)