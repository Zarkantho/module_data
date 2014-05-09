# Storage

Storage layer for MongoDB.  Includes structural metadata as well as code to access data files, metadata files, and the journal on disk

## Modules

### [Repair Database](repair\_database)
Implementation of the repair database command.

### [File Allocation](file\_allocation)
TODO: file\_allocation description

### [File Interface](file\_interface)
TODO: file\_interface description

### [Journaling](journaling)
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

### [Data Files](data\_files)
Non journaling related code for dealing with database data files

### [Page Fault Utilities](page\_fault\_utilities)
TODO: page\_fault\_utilities description

### [Storage Layer Structure](storage\_layer\_structure)
Structure of the storage layer.  Some of these files are for the persistent on disk representation, whereas some are for the in memory representation. TODO: Come up with better sections.  Split up btree info, persistent structure, and in memory structure into separate modules

