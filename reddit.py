import praw
import pandas as pd
import os
import re
# make sure to install nltk as well!
from textblob import TextBlob

## Read-only instance
reddit_read_only = praw.Reddit(client_id="",         # your client id
                               client_secret="",      # your client secret
                               user_agent="")        # your user agent Authorized instance
subreddit = reddit_read_only.subreddit("wallstreetbets")


#display the name of the subreddit
print("Display Name:", subreddit.display_name)

#display the title of the subreddit
print("Tilte:", subreddit.title)

#display the description of the subreddit

print("Description:", subreddit.description)

#scraping the top 10 post
for post in subreddit.hot(limit=50):
    print(post.title)
    print()


#scraping the top post of the current month
posts = subreddit.top(time_filter="all")

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }


for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post
    posts_dict["ID"].append(post.id)

    # The score of a post
    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)


# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts
#save post to a file
top_posts.to_csv("Top_Posts.csv", index=False)
top_posts = pd.DataFrame(posts_dict)


def my_function():

    global acronym_list, list_of_lists

    print("MATCHING SHIT")

    # Gets all sentences which contain 3-5 letter capiatlised words e.g. "TSM", "TSLJ"
    with open("Top_Posts.csv", 'r', encoding='utf-8') as f, open('output.txt', 'w', encoding='utf-8') as fw:
        text = f.read()
        result_string = ''
         # Split the text into sentences
        text2 = text.split(".")
        
        # Regular expression to match FULL CAPS 3-5 letter words
        pattern = r'\b[A-Z]{3,5}\b'
        
        for sentence in text2:
            # Find if matches in the sentence
            if re.search(pattern, sentence):
                # BULLSHIT SENTIMENT ANALYSIS
                blob = TextBlob(sentence)
                sentiment = blob.sentiment.polarity
                result_string += sentence.strip() + '. ' + str(sentiment)

                # Applies sentiment value to each match in sentence
                matches = re.findall(pattern, sentence)
                for match in matches:
                    try:
                        # if found in list
                        index = acronym_list.index(match)
                        list_of_lists[index].append(sentiment)
                    except:
                        # else add to lists
                        acronym_list.append(match)
                        index = len(acronym_list) - 1
                        list_of_lists.append([sentiment])
                    
                
        print(result_string)
        fw.write(result_string)

def avg_and_rank():
    global acronym_list, list_of_lists, acronym_values, acronym_accuracy

    for value_list in list_of_lists:
        total = 0.0
        accuracy = 0
        for value in value_list:
            total += value
            accuracy += 1
        try:
            total = total/len(value_list)
        except:
            total = 0.0
        acronym_values.append(total)
        acronym_accuracy.append(accuracy)

#GLOBALS
acronym_list = []
acronym_values = []
acronym_accuracy = []
list_of_lists = [[]]

my_function()
avg_and_rank()

#List of all acronyms and their scores
# Now, print each acronym and its corresponding list
for acronym, value, accuracy in zip(acronym_list, acronym_values, acronym_accuracy):
    print("Name: " + acronym + "    Value: " + str(value) + "   Accuracy: " + str(accuracy))            # Print the acronym