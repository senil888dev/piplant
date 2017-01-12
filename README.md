# What is the PiPlant?
PiPlant is a Python 3.5.2 script with a sole purpose - allow anyone on Twitter (yes, ANYONE) to vote whether or not they want to water the plant or not on any particular day, then relay that information to the Pi for information processing (or, "do we water today or not").
***
# How can I interact with it?
Currently, interacting with PiPlant is, well, out of the question. Due to frustrations with both the Tweepy and Twython wrappers, I decided to re-write the code once more, this time using python-twitter. It supports the same search queries and formats that the Twitter APIs natively use, no magic required. Once the twitter side is functional, you can tweet out to a particular hashtag, using a "positive" or "negative" word to convey whether you want to water the plant or not for that day.

The current list of positive words are: 'yes', 'yep', 'yepp', 'yeppers', 'yup', 'yupp', 'yuuup', 'ye', 'yee', 'yes please', 'hell yes', 'ofc', 'yass'

The current list of negative words are: 'no', 'nope', 'nop', 'not on your nelly', 'no way', 'not a chance', 'hell no', 'no please', 'nu', 'nein'
***
# When can I download the code myself?
If you want to replicate this project, the hardest part is the twitter side of things - which is my current focus for everything. Once the twitter side of things is complete, it's a matter of running code to work on either a Raspberry Pi + Camera module for taking photos, or running code to work on any PC you own with your own watering system.
***
# Why bother with a website if it's not finished yet?
Mostly because this way it's another step gone for when I do finish the project and get it operational. This link is also in the daily tweet as a kind of "Learn more about this plant here". Part of the testing is a few week-long test runs to make sure the system is capable of recovering if there's heavy load, and can handle loads of who-knows-how-many-people tweeting it.
***
# Do you have any other projects?
I do. Monita, a face for a Jasper client, is slowly being worked on. And by slowly, I mean I haven't started because it's a Pi-exclusive system that has parts I don't have (re: all of them). You can learn more about Monita at senil888dev.github.io/monita-assistant
