############################ a script to make API requests and print the returned data #############################

# 'requests' is a module (or 'library') that lets us make API requests
import requests

APIkey = "523cf6228063676f022e1c9a8a2e4841" # Stick your API key in here as a string

APIparam1 = "51.501571,0.005531" # Put any parameters you need to specify for the API request in here
APIparam2 = "51.518561,-0.143799" # Delete this 3rd parameter if you don't need it

# Find out from your chosen API's documentation what the API request URL is, and stick your API parameters
requestURL = "https://api.tfl.gov.uk/Journey/JourneyResults/"+APIparam1+"/to/"+APIparam2+"?nationalSearch=False&timeIs=Arriving&journeyPreference=LeastTime&walkingSpeed=Average&cyclePreference=None&alternativeCycle=False&alternativeWalking=True&applyHtmlMarkup=False&useMultiModalCall=False&walkingOptimization=False&app_id=1a2ae856&app_key="+APIkey
                                                      #APIparam2+

# Make your API request!
APIresponse = requests.get(requestURL)

# Convert the response into a dictionary, so you can easily access the information you want
data = APIresponse.json()

# Pick out the information you want from the returned API data (remember the data type is a dictionary) and print a
# string to the command line with this data embedded in it (e.g. it is 12 degrees celsius in London today)

#print (data['journeys'])

journeys = data['journeys'][2]

#legInfo = data['journeys'][2]['legs'][3]['instruction']

#legInstruction = legInfo['summary']

#print legInstruction

journeyTime = journeys['duration']

startTime = journeys['startDateTime']

endTime = journeys['arrivalDateTime']

print endTime

print startTime

print 'This journey will take ' + str(journeyTime) + ' minutes'

#print 'You will arrive at' + 'arrivalDateTime'

#print 'summary' + '.This will take' + 'duration'

#print 'Next '
#arrivalTime = data[1]['journeys']

#print arrivalTime
#
# destination = data[13]['destinationName']
#
# stationName = data[6]['stationName']
#
# arrivalTime = data[15]['timeToStation']
#
# print platformName.split()[0]
#
# print platformName.split()[3]
#
# print 'The next ' + platformName.split()[0]+' train from '+ stationName +' on platform ' + platformName.split()[3] + ' will arrive in '

#print len(data)

#print str("The next northern line trains destination is ") + destination

#if len(direction)<7:
#    print "This train is heading North"
#else:
#    print "This train is heading South"

print requestURL

#print type(data)



#"https://api.tfl.gov.uk/Journey/JourneyResults/"SE3 8TL"/to/"N10 1LN"?nationalSearch=False&timeIs=Arriving&journeyPreference=LeastTime&walkingSpeed=Average&cyclePreference=None&alternativeCycle=False&alternativeWalking=True&applyHtmlMarkup=False&useMultiModalCall=False&walkingOptimization=False&app_id=1a2ae856&app_key=523cf6228063676f022e1c9a8a2e4841