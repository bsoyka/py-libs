import json
import random
import os

os.chdir("templates")

with open("main.json") as file:
    stories = json.load(file)

story = random.choice(stories)

with open(story) as file:
    story_data = json.load(file)

with open(story_data["text"]) as file:
    story_text = file.read()

words = ()

for part_of_speech in story_data["formatting"]:
    words += (input("%s: " % part_of_speech),)

finished_story = story_text.format(*words)

print(story_data["title"])
print()
print(finished_story)
