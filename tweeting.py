import tweepy
import schedule
import time
from auth import consumer_key, consumer_secret, key, secret
from time import strftime, localtime

auth = tweepy.OAuthHandler(consumer_key,  consumer_secret)
auth.set_access_token(key, secret)

api=tweepy.API(auth, wait_on_rate_limit=True)
#All the code relating to twitter lies here. Before you make your own changes,
#make sure you've added your own API keys.

#positive and negative reflect the possible responses to vote with.
#These can be changed as needed/desired.
positive = 'yes', 'yep', 'yepp', 'yeppers', 'yup', 'yupp', 'yuuup', 'ye', 'yee', 'ofc', 'yass '
negative = 'no', 'nope', 'nop', 'not on your nelly', 'no way', 'not a chance', 'hell no', 'no please', 'nu', 'nein'
#where is the image we're uploading going to be at? this case: it's nested. heavily.
photo ='C:/Users/Sean/Downloads/ExtraExtra/PolyBridgeGIFs/pb1.gif'

def startPeriod(): #this is the tweet that signifies the start of the voting period.
    timeNow = strftime('%a, %b %d %Y', localtime())
    global timeStartPeriod
    timeStartPeriod = strftime('%Y-%m-%d', localtime())
    #Your message. We need this to update every time we tweet, hence why it's here.
    #If you don't change anything, keep the piplant.cu.cc link, it's there to help users on what they can tweet.
    message = "It's {} now! Last watered on DOW. Vote using #waterbecky and a word like YES or NO! Learn more @ piplant.cu.cc".format(timeNow)
    api.update_with_media(filename=photo, status=message)
    print(message)

def pollPeriod(): #this is the hard part: searching for relevant tweets, comparing the users of found tweets to sets to ensure they don't get counted for multiple votes, etc.
    #the basis of pollPeriod(). if yes>no, we water. if no>yes, we don't. if yes=no, we issue a tiebreaker.
    yes=0
    no=0
    #Two sets that ignore users after we record that yes, they voted today.
    ignoreUsersY = set() 
    ignoreUsersN = set()
    #sets an end time should tweepy's since and until tags work correctly
    timeEndPeriod = strftime('%Y-%m-%d', localtime())

    print('Yes from:')
    #something is wonky about doing setting users = content.author._json['screen_name']
    #more research and testing needs to be done to figure this out.
    for voteY in positive:
        votesPositive = api.search(q='#waterbecky {}'.format(voteY))
        for content in votesPositive:
            #user = content.author._json['screen_name']
            #print(user)
            print(content.author._json['screen_name'])
            #if user not in ignoreUsersY:
              #  print(content.author._json['screen_name'])
               # ignoreUsersY.add(content.author._json['screen_name'])
               # yes += 1
            #else:
              #  yes = yes
            
    print('No from:')
    #something is wonky about doing setting users = content.author._json['screen_name']
    #more research and testing needs to be done to figure this out.
    for voteN in negative:
        votesNegative = api.search(q='#waterbecky {}'.format(voteN))
        for content in votesNegative:
            user = content.author._json['screen_name']
            print(user)
            #print(content.author._json['screen_name'])
            #if user not in ignoreUsersN:
             #   print(content.author._json['screen_name'])
             #   ignoreUsersN.add(content.author._json['screen_name'])
             #   no += 1
            #else:
              #  no = no
    print()
    print('===Total Votes===')
    print('{} to water.'.format(yes))
    print('{} to not water.'.format(no))

startPeriod()
pollPeriod()

        
