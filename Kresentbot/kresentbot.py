import praw
import os
import pdb
import re
import random
min = 1
max = 6

#Introductory text

name = input("Please input your name here: ")
print("Hello,", name, "this is the Kresent bot, a bot that surfs the chosen subreddits and fetches top 6 hot posts from subreddit1 and replies to the posts having a specific title posted on subreddit2!")


reddit = praw.Reddit('bot1')
print("We will now roll the dice for a random number")
dice_roll = random.randint(min, max)
yeet = None
if dice_roll == 1:
    yeet = 1
elif dice_roll == 2:
    yeet = 2
elif dice_roll == 3:
    yeet = 3
elif dice_roll == 4:
    yeet = 4
elif dice_roll == 5:
    yeet = 5
else:
    yeet = 6

fetched_posts_scores = []

#Each reddit post has unique id
if os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

#Now we get the posts from a subreddit
#This is subreddit for fetching results
subreddit1 = reddit.subreddit("ubcengineering")
#This one fetches the results of top 5 hot posts in a subreddit
for submission in subreddit1.hot(limit = 6):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
    fetched_posts_scores.append(submission.score)

if yeet == 1:
    yeet = fetched_posts_scores[0]
if yeet == 2:
    yeet = fetched_posts_scores[1]
if yeet == 3:
    yeet = fetched_posts_scores[2]
if yeet == 4:
    yeet = fetched_posts_scores[3]
if yeet == 5:
    yeet = fetched_posts_scores[4]
if yeet == 6:
    yeet = fetched_posts_scores[5]

#print(fetched_posts_scores)


print("---------------------------------------------------------\n")
print("The post which is going to be displayed has a score of: ", yeet)
for sub in subreddit1.hot(limit = 6):
    if sub.score == yeet:
        print("Title of yeeted post: ", sub.title)
        print("Description of the yeeted post: ", sub.selftext)
    else:
        continue


#This is subreddit for replying to posts
subreddit2 = reddit.subreddit("pythonforengineers")
#This replies to to top 2 posts which have the corresponding

for post in subreddit2.hot(limit = 3):
    if post.id not in posts_replied_to:
        if re.search("Wassup", post.title, re.IGNORECASE):
            post.reply("I want to as well ;)")
            print("Bot replying to : ", post.title)
            #store the current id in the list
            posts_replied_to.append(post.id)




#Writing the list fully updated
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
