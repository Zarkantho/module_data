# base\_utilites

# Module Groups

-------------

Use this in a class to explicitly disallow copying of the class. This can prevent bugs where you  were accidentally copying a class that wasn't safe to copy.

- src/mongo/base/disallow\_copying.h

-------------

64 bit atomic counter

- src/mongo/base/counter.h
- src/mongo/base/counter\_test.cpp   ()

-------------

Vector and map that delete pointers to elements on destruction. "owning" the memory means you are  responsible for deleting it.

- src/mongo/base/owned\_pointer\_map.h
- src/mongo/base/owned\_pointer\_map\_test.cpp   ()
- src/mongo/base/owned\_pointer\_vector.h
- src/mongo/base/owned\_pointer\_vector\_test.cpp   ()

-------------

Status to return errors. StatusWith can return either an error or a value, so we don't have to  use return parameters as arguments to the function.

- src/mongo/base/status-inl.h
- src/mongo/base/status.cpp   (mongod, tools, mongos)
- src/mongo/base/status.h
- src/mongo/base/status\_test.cpp   ()
- src/mongo/base/status\_with.h
- src/mongo/base/error\_codes.err
- src/mongo/base/generate\_error\_codes.py

-------------

Number to string conversion   Why use these: is this somehow fast/safe? somehow JSON-aware?

- src/mongo/base/parse\_number.cpp   (cppclientdriver)
- src/mongo/base/parse\_number.h
- src/mongo/base/parse\_number\_test.cpp   ()

-------------

The StringData class is a wrapper around a char* that can be constructed from either std::string  and a char* without copying the buffer. This is because a StringData doesn't free the buffer, so  unlike std::string it doesn't need to have its own copy.   Why: use for speed? is this similar to other classes people might be   familiar with from elsewhere?

- src/mongo/base/string\_data-inl.h
- src/mongo/base/string\_data.cpp   (cppclientdriver)
- src/mongo/base/string\_data.h
- src/mongo/base/string\_data\_test.cpp   ()
