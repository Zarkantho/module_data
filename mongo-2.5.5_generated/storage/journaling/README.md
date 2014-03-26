# Journaling

# Module Groups

-------------

# Page Aligned Buffer
Page aligned buffer builder

## Files
- src/mongo/util/alignedbuilder.cpp   (mongod, tools)
- src/mongo/util/alignedbuilder.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

# TODO: Name this group
Journaling module   who calls/owns stuff in here? only used by mongod, correct?

## Files
- src/mongo/db/dur.cpp   (mongod, tools)
- src/mongo/db/dur.h   (mongod, tools, mongos)
- src/mongo/db/dur\_commitjob.cpp   (mongod, tools)
- src/mongo/db/dur\_commitjob.h   (mongod, tools)
- src/mongo/db/dur\_journal.cpp   (mongod, tools)
- src/mongo/db/dur\_journal.h   (mongod, tools)
- src/mongo/db/dur\_journalformat.h   (mongod, tools)
- src/mongo/db/dur\_journalimpl.h   (mongod, tools)
- src/mongo/db/dur\_preplogbuffer.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.h   (mongod, tools)
- src/mongo/db/dur\_stats.h   (mongod, tools)
- src/mongo/db/dur\_writetodatafiles.cpp   (mongod, tools)
- src/mongo/db/durop.cpp   (mongod, tools)
- src/mongo/db/durop.h   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.cpp   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

# TODO: Name this group
This is not actually used in our logging system. Just utilities to create files that you can  append to. One notable example of a system that uses this is our preallocation of journal files.  In fact, it isn't used in anything not journaling related right now.

## Files
- src/mongo/util/logfile.cpp   (mongod, tools)
- src/mongo/util/logfile.h   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
