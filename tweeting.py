import tweepy
import schedule
import time
from auth import consumer_key, consumer_secret, key, secret
from time import strftime, localtime

auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
auth.set_access_token(key, secret)

api=tweepy.API(auth)
#All the code relating to twitter lies here. Before you make your own changes,
#make sure you've added your own API keys.

#positive and negative reflect the possible responses to vote with.
#These can be changed as needed/desired.
positive = 'yes', 'yep', 'yepp', 'yeppers', 'yup', 'yupp', 'yuuup', 'ye', 'yee', 'ofc', 'yass'
negative = 'no', 'nope', 'nop', 'not on your nelly', 'no way', 'not a chance', 'hell no', 'no please', 'nu', 'nein'
#where is the image we're uploading going to be at? this case: it's nested. heavily.
photo ='C:/Users/Sean/Downloads/ExtraExtra/PolyBridgeGIFs/pb1.gif'

def startPeriod(): #this is the tweet that signifies the start of the voting period.
    timeNow = strftime('%a, %b %d %Y', localtime())
    global timeStartPeriod
    timeStartPeriod = strftime('%Y-%m-%d', localtime())
    #Your message. We need this to update every time we tweet, hence why it's here.
    #If you don't change anything (add/remove search terms), keep the piplant.cu.cc link, it's there to help users on what they can tweet.
    message = "It's {0} now! Last watered on DOW. Vote using #waterbecky and a word like YES or NO! Learn more @ piplant.cu.cc".format(timeNow)
    api.update_with_media(filename=photo, status=message)
    print(message)

def pollPeriod(): #this is the hard part: searching for relevant tweets, comparing the users of found tweets to sets to ensure they don't get counted for multiple votes, etc.
    #the basis of pollPeriod(). if yes>no, we water. if no>yes, we don't. if yes=no, we issue a tiebreaker.
    yes=0
    no=0
    #sets an end time should tweepy's since and until tags work correctly
    timeEndPeriod = strftime('%Y-%m-%d', localtime())
    ignoreUserY = set()
    ignoreUserN = set()

    print('Yes from:')
    for votes in positive:
        votesPos = api.search(q='waterbecky {}'.format(votes))
        for content in votesPos:
            #print(content.author._json['screen_name'])
            username = content.author._json['screen_name']
            if username not in ignoreUserY:
                print(username)
                ignoreUserY.add(username)
                yes += 1
            else:
                yes = yes
    print('No from:')
    for votes in negative:
        votesNeg = api.search(q='watertaila {}'.format(votes))
        for content in votesNeg:
            #print(content.author._json['screen_name'])
            username = content.author._json['screen_name']
            if username not in ignoreUserN:
                print(username)
                ignoreUserN.add(username)
                no += 1
            else:
                no = no

    print()
    print('=====Total Votes=====')
    print('{} to water.'.format(yes))
    print('{} to not water.'.format(no))

    if yes > no:
        print("\nWe're watering today!")
        api.update_states(status="We had more votes to water than to not. We're watering today!")
    if yes < no:
        print("\nWe're not watering today!")
        api.update_status(status="We had more votes to not water than to. We're not watering today!")
    if yes == no:
        print("\nWe had equal votes today.")
        random.seed(version=2)
        tiebreaker = random.randrange(0, 1)
        if tiebreaker == 1:
            print("\nWe're watering today!")
            api.update_states(status="We had more votes to water than to not. We're watering today!")
        if tiebreaker == 0:
            print("\nWe're not watering today!")
            api.update_status(status="We had more votes to not water than to. We're not watering today!")


schedule.every().day.at("03:00").do(pollPeriod)
schedule.every().day.at("07:00").do(startPeriod)
schedule.every().day.at("15:27").do(startPeriod)
schedule.every().day.at("15:25").do(pollPeriod)

while True:
    schedule.run_pending()
    time.sleep(1)
