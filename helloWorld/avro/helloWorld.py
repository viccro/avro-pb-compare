#!/usr/bin/env python

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

#Read in the helloWorld schema from the JSON
schema = avro.schema.parse(open("helloWorld.avsc", "rb").read())

#To use the IDL file, compile first using maven plugin

writer = DataFileWriter(open("output.avro", "wb"), DatumWriter(), schema)
writer.append({"username": "ben",  "favorite_nums": [0,256]})

#Another example
#writer.append({"username": "alyssaPH", "favorite_nums" : [1,1,2,3,5,7], "opt_favorite_color": "lilac"})

writer.close()

reader = DataFileReader(open("output.avro", "rb"), DatumReader())

for user in reader:
    print user
    reader.close()
