# Journaling
System to ensure that our writes are durable even in the event of unexpected crashes.

Before we start writing an operation to disk, we write a persistent log entry to the journal with what we are about to do.  Then, if a crash occurs in the the middle of our operation when our state is corrupt, we can replay all the operations in the journal to ensure we are back to a valid state on restart.

Our storage system is based on memory mapped files, which means that we write to memory that is mapped using MAP\_SHARED and the changes get persisted back to disk by the OS.

However, just one map is not sufficient.  This is because the journal entry has to be written before we start writing to the actual data files but we also do not want the time before we see the results of the operation to be gated by the time it takes to write the journal to disk.  To solve this problem, we map the file a second time using MAP\_PRIVATE, which signals that changes to that range should not get persisted back to disk.

From the perspective of a client operation using the journal, the sequence of actions is as follows.

First the operation uses the private view to serve the part of the operation that does not require a write.  Clients operations exclusively interact with the private view throughout the entire lifetime of the operation.

Next, the operation notifies the journal of intent to write, including where and how much. This gets put into the in memory representation of the journal operations that need to be applied.

Finally, the operation applies its changes to the private view and is now free to return to the client as soon as the appropriate write concern is satisfied.

The other component of this system is the journaling thread.  This thread is responsible for actually writing the changes back to disk.  It has the following stages.

PREPLOGBUFFER - Convert from the in memory datastructures into the actual buffer that will be written out to the journal.

WRITETOJOURNAL - Write the prepared buffer sequentially to the journal.

WRITETODATAFILES - Write to the data files in the shared view, which means they could get written back to disk automatically or after an fsync.

REMAPPRIVATEVIEW - Remap the private view of the data files.  This is to ensure that any pages that were copied on write and are not backed by any files or needed any more can get reclaimed by the OS.

Here is a visual representation of the work done by the journal thread. https://docs.google.com/a/10gen.com/drawings/d/1TklsmZzm7ohIZkwgeK6rMvsdaR13KjtJYMsfLr175Zc


-------------

## Page Aligned Buffer
Page aligned buffer builder

#### Files
- src/mongo/util/alignedbuilder.cpp   (mongod, tools)
- src/mongo/util/alignedbuilder.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Write Intents
In memory classes that store operations from clients that need to be journaled that have not yet been serialized into journal entries.

#### Files
- src/mongo/db/dur\_commitjob.cpp   (mongod, tools)
- src/mongo/db/dur\_commitjob.h   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Journal Entry Serialization
Stage of journaling that takes the in memory representation of operations that need to be journaled and processes them to create the actual buffers that get written back to the journal files.  Also handles merging of overlapping entries.

#### Files
- src/mongo/db/dur\_preplogbuffer.cpp   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Journal File Management
Used to manage the journal files, including allocation and appending data.  Actually writes the data to the on disk journal files.

#### Files
- src/mongo/db/dur\_journal.cpp   (mongod, tools)
- src/mongo/db/dur\_journal.h   (mongod, tools)
- src/mongo/db/dur\_journalimpl.h   (mongod, tools)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Persistent Data File Writes
Stage of journaling that actully applies the journal operations to the shared view of the data files, logically writing the changes back to disk.  Journal files only get deleted when the changes have actually been written to disk.

#### Files
- src/mongo/db/dur\_writetodatafiles.cpp   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Journaled Non Write Operations
Operations that need to be journaled that are not writes, such as data file creation.

#### Files
- src/mongo/db/durop.cpp   (mongod, tools)
- src/mongo/db/durop.h   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Journaling Main
Top level interface to the journaling system as well as the journal commit thread.  This interface can be transparently swapped out with a class that does not actually do the journaling in the case where journaling is disabled.

#### Files
- src/mongo/db/dur.cpp   (mongod, tools)
- src/mongo/db/dur.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Journal Format
On disk format of all journaling related objects.

#### Files
- src/mongo/db/dur\_journalformat.h   (mongod, tools)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Journal Recovery
Code to actually apply the journal operations when the system is recovering.  Note that currently this is also used during normal operation when writing to the persistent representation of the datafiles.

#### Files
- src/mongo/db/dur\_recover.cpp   (mongod, tools)
- src/mongo/db/dur\_recover.h   (mongod, tools)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Journal Stats
Statistics about our journal operation.

#### Files
- src/mongo/db/dur\_stats.h   (mongod, tools)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Journaling Memory Map Management
Classes to make it easier to manage and keep track of the private and shared "views" of a file needed by the journaling system.  This also handles remapping the private view to allow the OS to free the pages that are no longer needed.

#### Files
- src/mongo/db/storage/durable\_mapped\_file.cpp   (mongod, tools)
- src/mongo/db/storage/durable\_mapped\_file.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Append Only File
Used by journaling system to write our prepared buffers to the journal files.

#### Files
- src/mongo/util/logfile.cpp   (mongod, tools)
- src/mongo/util/logfile.h   (mongod, tools)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)
