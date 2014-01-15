# journaling

# Module Groups

-------------

Page aligned buffer builder   what sort of buffer? i don't understand ;(

- src/mongo/util/alignedbuilder.cpp   (mongod, tools)
- src/mongo/util/alignedbuilder.h

-------------

Journaling module   who calls/owns stuff in here? only used by mongod, correct?

- src/mongo/db/dur.cpp   (mongod, tools)
- src/mongo/db/dur.h
- src/mongo/db/dur\_commitjob.cpp   (mongod, tools)
- src/mongo/db/dur\_commitjob.h
- src/mongo/db/dur\_journal.cpp   (mongod, tools)
- src/mongo/db/dur\_journal.h
- src/mongo/db/dur\_journalformat.h
- src/mongo/db/dur\_journalimpl.h
- src/mongo/db/dur\_preplogbuffer.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.h
- src/mongo/db/dur\_stats.h
- src/mongo/db/dur\_writetodatafiles.cpp   (mongod, tools)
- src/mongo/db/durop.cpp   (mongod, tools)
- src/mongo/db/durop.h
- src/mongo/db/storage/durable\_mapped\_file.cpp   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.h

-------------

This is not actually used in our logging system. Just utilities to create files that you can  append to. One notable example of a system that uses this is our preallocation of journal files.  In fact, it isn't used in anything not journaling related right now.

- src/mongo/util/logfile.cpp   (mongod, tools)
- src/mongo/util/logfile.h
