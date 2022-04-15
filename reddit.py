import praw
import pandas as pd
import os
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
posts = subreddit.top("all")

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
top_posts.to_csv("Top_Posts.csv", index=True)
top_posts = pd.DataFrame(posts_dict)


def my_function():


  with open("Top_Posts.csv",'r') as f, open('output.txt','w') as fw:
      text = f.read()
      result_string = ''

      words = ["YOLO", "Musk","GME", "tsla"]
      text2 = text.split(".")
      for itemIndex in range(len(text2)):
          for word in words:
              if word in text2[itemIndex]:
                  if text2[itemIndex][0] ==' ':
                      print(text2[itemIndex][1:])
                      result_string += text2[itemIndex][1:]+'. '
                      break
                  else:
                      print(text2[itemIndex])
                      result_string += text2[itemIndex]
                      break
      print(result_string)
      fw.write(result_string)

my_function()
