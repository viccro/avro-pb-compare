#! /usr/bin/env python

import helloWorld_pb2 as hw_pb2

{"username": "ben",  "favorite_nums": [0,256]}

user = hw_pb2.User()
user.username = "ben"
user.favorite_nums.extend([0,256])

#Another example
#user.username = "alyssaPH"
#user.favorite_nums.extend([1,1,2,3,5,7])
#user.opt_favorite_color = "lilac"

serializedUser = user.SerializeToString()

fw = open("output_protobuf", "wb")
fw.write(serializedUser)
fw.close()

fr = open("output_protobuf", "rb")

for line in fr:
  print line
fr.close()
