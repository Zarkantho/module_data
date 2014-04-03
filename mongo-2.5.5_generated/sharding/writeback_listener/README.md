# Writeback Listener
The Writeback listener is a legacy class to handle the case where unacknowledged writes went to the wrong shard.
Well, in the dark ages before 2.6, none of our writes would get a direct response.  This means that we have to call getLastError to figure out what happened to the write.
Now consider the case of a mongos sending a write to a shard.  What can go wrong?  Well, the mongos may send the write to a chunk that has already moved.  At that point there are two options:
1.  The mongos must keep the write around, so that next time it calls getLastError it can see that something went wrong and send the write to the correct shard. 2.  The mongod must queue the incorrect writes, and the mongos must ask: "dude, have I screwed up recently"
We took option 2.


What the mongoD has to do:
When a mongod recieves any operation, it calls the "handlePossibleShardedMessage" function. This does a couple things:
1.  Checks whether the operation had the correct shard version 2.  Checks whether the operation is one that recieves a response a. If it does, it just puts the appropriate error status in the response b. If it does not, it puts it in a "writeback queue" specific to that mongos
This function is in the ironically named "d\_logic.cpp".
The writeback queue where these actually get stored is in d\_writeback.cpp.


What the mongoS has to do:
So now the writes are sitting in this queue on the wrong mongod.  How do we get them to the right place?  This is the job of the WriteBackListener thread.  Each mongos spawns one WriteBackListener for every shard.  This is the thing that runs in the background and runs the "writebacklisten" command to poll the shards for writebacks.  When a writeback gets queued on that shard because of a write from that mongos, the "writebacklisten" command returns the writes that need to be reapplied, and the WriteBackListener tries to send them to the correct shard.
When the mongos calls "getLastError", it gets an ID for the operation that needs to be reapplied.  The mongos then will wait to reply to a "getLastError" from the user until the WriteBackListener thread has applied up to the operation corresponding to that ID (note the IDs are strictly increasing per writeback queue).
The writeback listener thread is here in "writeback\_listener.cpp".
So how do write commands help?  Well, now that every write recieves a response, we get an error back immediately when we send a write to the wrong shard, rather than having to queue the writes.
The even better news is that when a 2.6 mongos is connecting to a 2.4 shard, the write commands are emulated by a block of code that does a safe write using the legacy "getLastError" call.  This means it gets handled just as if we sent a command and got a response immediately (and thus can retry our write), which means that in 2.6 the WriteBackListener does nothing but log!


-------------

## Mongos Writeback Listener Thread
Thread on mongos that polls the shards for writebacks and sends any queued writebacks to the correct shard

#### Files
- src/mongo/s/writeback\_listener.cpp   (mongos)
- src/mongo/s/writeback\_listener.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongod WriteBack Queue and writebacklisten Command
Queue where mongod stores writebacks and command that the writebacklistener on mongos calls to poll the shard

#### Files
- src/mongo/s/d\_writeback.cpp   (mongod, tools)
- src/mongo/s/d\_writeback.h   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Mongod WriteBack Checks
Code to check if an operation should result in a writeback being queued on the shard

#### Files
- src/mongo/s/d\_logic.cpp   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
