# avro-pb-compare

This repository contains examples of avro and protobuf schemas, for comparison.

**helloWorld**
The helloWorld directory contains an example schema representing a User, with fields for username, list of favorite numbers, and optional favorite color.

**unionExample**
The unionExample directory contains examples contrasting the difference between avro's union type and protobuf's one of, with default values for each field. The example schema represents an article with a string title and a list of relatedArticleID, which can either be null (as default), a string, or an int. Note that when multiple schemas are defined in avro, a .avpr protocol file is used instead of a .avsc schema file.

**unionExampleFC**
The unionExampleFC directory contains a forward-compatible variant on the unionExample avro schema. 

