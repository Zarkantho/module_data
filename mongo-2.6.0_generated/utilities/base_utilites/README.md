# Base Utilites
Core server utilities that can be safely used everywhere without pulling in other dependencies.  These are things like cross platform counters and string to number conversion.


-------------

## Disallow Copying
Use this in a class to explicitly disallow copying of the class. This can prevent bugs where you  were accidentally copying a class that was not safe to copy.

#### Files
- src/mongo/base/disallow\_copying.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Atomic Counter
64 bit atomic counter

#### Files
- src/mongo/base/counter.h   (mongod, tools)
- src/mongo/base/counter\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Owned Vector
Vector and map that delete pointers to elements on destruction. "owning" the memory means you are  responsible for deleting it.

#### Files
- src/mongo/base/owned\_pointer\_map.h   (mongod, tools, mongos)
- src/mongo/base/owned\_pointer\_map\_test.cpp   ()
- src/mongo/base/owned\_pointer\_vector.h   (mongod, tools, mongos)
- src/mongo/base/owned\_pointer\_vector\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Error Handling Utilities
These are the general error codes for MongoDB.  Error codes have some semantic meaning associated with them.  A Status is a holder for an error code and extra error information, such as a message.  A StatusWith is an object that can either be an error Status or hold an actual value, which means we can still use return to return data from a function rather than passing in pointers as return parameters.

#### Files
- src/mongo/base/status-inl.h   (mongod, tools, mongos)
- src/mongo/base/status.cpp   (mongod, tools, mongos)
- src/mongo/base/status.h   (mongod, tools, mongos)
- src/mongo/base/status\_test.cpp   ()
- src/mongo/base/status\_with.h   (mongod, tools, mongos)
- src/mongo/base/error\_codes.err   (mongod, tools, mongos)
- src/mongo/base/generate\_error\_codes.py   (mongod, tools, mongos)
- build/darwin/ssl/mongo/base/error\_codes.h   (mongod, tools, mongos)
- build/darwin/ssl/mongo/base/error\_codes.cpp   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Number To String Conversion
Cross platform utilities to convert numbers to strings

#### Files
- src/mongo/base/parse\_number.cpp   (mongod, tools, mongos)
- src/mongo/base/parse\_number.h   (mongod, tools, mongos)
- src/mongo/base/parse\_number\_test.cpp   ()

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## StringData
The StringData class is a wrapper around a char* that can be constructed from either std::string or a char* without copying the buffer.  This is because a StringData doesn't free the buffer, so unlike std::string it doesn't need to have its own copy.  Is this in function arguments to avoid making an implicit copy when that is not intended.

#### Files
- src/mongo/base/string\_data-inl.h   (mongod, tools, mongos)
- src/mongo/base/string\_data.cpp   (mongod, tools, mongos)
- src/mongo/base/string\_data.h   (mongod, tools, mongos)
- src/mongo/base/string\_data\_test.cpp   ()

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)
