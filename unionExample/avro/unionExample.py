#!/usr/bin/env python

import avro.protocol
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

#Read in the helloWorld schema from the JSON
schema = avro.protocol.parse(open("unionExample.avpr", "rb").read())
