# Writeback Listener


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
