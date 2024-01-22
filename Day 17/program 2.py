"""Define a class for YouTube video.
decide the properties and functions based on the questions below.

List all the videos recorded by author "Kannan"
List all the videos with more than 1K views
Change the author of all the videos recorded by "Kannan" to "Kannan D."
20 students watched Kannan's "Intro to Python" video today. Update the videos views and print
the total views for this video."""


class youtube_video:                              # Define the youtube_video class
    def __init__(self, author, views, title):
        self.author = author
        self.views = views
        self.title = title


Videos = []             # Create a list to store videos

# Create instances of youtube_video and add them to the Videos list
video1 = youtube_video("hari", 300, "Hello world in Python")
video2 = youtube_video("kannan", 1000, "Intro to Python")
video3 = youtube_video("saravana", 3000, "Python for beginners")
video4 = youtube_video("kannan", 1500, "OOPs Using Python")
video5 = youtube_video("kannan", 250, "Python for Data Science")

Videos.append(video1)
Videos.append(video2)
Videos.append(video3)
Videos.append(video4)
Videos.append(video5)

# Display videos recorded by author "kannan"
print("Video recorded by author Kannan")
for video in Videos:
    if video.author == "kannan":
        print(f'{video.title} is recorded by {video.author}')

print()

print("Videos with more than 1K views")    # Display videos with more than 1K views
for video in Videos:
    if video.views >= 1000:
        print(f'{video.title} has {video.views} views')
print("\n\n\n")


for video in Videos:                   # Change the author name from "kannan" to "kannan D."
    if video.author == "kannan":
        video.author = "kannan D."

print()

for video in Videos:          # Display updated video information
    print(f'Title: {video.title}, Author: {video.author}, Views: {video.views}')

# Update views for the video
for video in Videos:
    if video.author == "kannan D." and video.title == "Intro to Python":
        video.views += 20

print()

for video in Videos: # Display updated video information
    print(f'Title: {video.title}, Author: {video.author}, Views: {video.views}')
