import os
# get path of this file
path = os.path.dirname(os.path.realpath(__file__))

# get all files in /video
FILES = [file for file in os.listdir(path + '/video') if file.endswith('.mp4')]

print(FILES)