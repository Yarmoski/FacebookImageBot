import facebook
import os
import random
import sys
from PIL import Image
 
 #unique Facebook access token goes here
access_token = 'token goes here'

#create graph object
graph = facebook.GraphAPI(access_token)


#Randomly selects adjectives
adjective1 = random.choice(open("./adjectives.txt").read().split())
adjective2 = random.choice(open("./adjectives.txt").read().split())

#Randomly selects images
flashback_path ='./flashback/'
files = os.listdir(flashback_path)
index = random.randrange(0, len(files))
flashback_image = files[index]
trooper_path ='./trooper/'
files = os.listdir(trooper_path)
index = random.randrange(0, len(files))
trooper_image = files[index]

#Combines images
flashback = Image.open(flashback_path + flashback_image)
print(flashback.mode,flashback.size,flashback.format)
trooper = Image.open(trooper_path + trooper_image).convert(flashback.mode)
trooper = trooper.resize(flashback.size)
complete = Image.blend(flashback, trooper, 0.6)
complete.show()

#completed photos path
hangar_path = "./hangar/complete.png" 

complete.save(hangar_path)

#Post Caption
msg = "War. War never changes. Especially for " + trooper_image.split('.')[0] + "..."

# Creates post
post_id = graph.put_photo(image = open(hangar_path, "rb"), message= msg)['post_id']
print('Photo with post id: ' + post_id + ' has been successfully uploaded to facebook')

# Create comment on post
comment_msg = trooper_image.split('.')[0] + " is currently undergoing therapy. You can help out by following this link: " + "https://preview.tinyurl.com/sk96nxx"
graph.put_comment(object_id = post_id, message = comment_msg)
