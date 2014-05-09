# Sharding

Code related specifically to sharding support in MongoDB.  See http://docs.mongodb.org/manual/sharding/ for a high level description.

## Modules

### [Writeback Listener](writeback\_listener)
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

### [Chunk Management](chunk\_management)
Commands and utilities to manage chunks in a sharded cluster

### [Config Server Schema](config\_server\_schema)
Schema for all sharding related collections on the config server.  All direct config server access should use these classes.

### [Balancer](balancer)
The balancer is a background job that runs on each mongos and is responsible for ensuring that the data is evenly distributed in a sharded cluster.  The balancer operates in "balancing rounds" during which it must take out a distributed lock on the config servers.

### [Mongod Sharding Metadata](mongod\_sharding\_metadata)
Classes to manage and store sharding related metadata on mongod

### [Cluster Locking](cluster\_locking)
Locking that is specific to a sharded cluster

### [Config Metadata Upgrade](config\_metadata\_upgrade)
Code to handle the versioning and upgrading of metadata on the config servers

### [Routing](routing)
Code to deal with routing operations in a sharded cluster

### [Cluster Metadata Management](cluster\_metadata\_management)
Helpers and wrappers to manage cluster metadata.  These exist so that operations requiring cluster metadata do not have to have code to directly query the config servers.

### [Metadata Versioniong](metadata\_versioning)
Since a sharded cluster is distributed, mongos and mongod both have to cache metadata from the config servers.  Because of this, there is a need to keep track of metadata version information and make decisions based on the last version that was seen.

### [Mongos Commands](mongos\_commands)
General commands available on mongos, run using db.$cmd.findOne(...)

### [Shard Abstraction](shard\_abstraction)
Classes abstracting the idea of a shard in a sharded cluster

### [Build Stubs](build\_stubs)
Stubs not related to sharding but needed to make mongos link

