# page\_fault\_utilities

# Module Groups

-------------

Contains the PageFaultException and NoPageFaultsAllowed classes.   where are these used?

- src/mongo/db/pagefault.cpp   (mongod, tools)
- src/mongo/db/pagefault.h

-------------

Code to go in and touch pages so that they are brought into memory.   who calls these?

- src/mongo/db/prefetch.cpp   (mongod, tools)
- src/mongo/db/prefetch.h
