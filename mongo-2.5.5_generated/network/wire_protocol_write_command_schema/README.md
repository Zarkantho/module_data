# wire\_protocol\_write\_command\_schema

# Module Groups

-------------

# Group Description
Schema for the responses to write commands.

## Files
- src/mongo/s/write\_ops/batched\_command\_response.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_response.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_response\_test.cpp   ()

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
This contains the interface for dealing with the schema of the various write commands.  Note that this class does not actually contain the schema, but instead just multiplexes between the various write command types, calling straight through to the classes for each type when appropriate.

## Files
- src/mongo/s/write\_ops/batched\_command\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_command\_request.h   (mongod, tools, mongos)

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
These files contain the schema for the various write commands.  Some of the classes are for schema restrictions that we have on nested objects.  For example, an update command has an overall schema, but the update objects that we send with the command have a schema of their own.

## Files
- src/mongo/s/write\_ops/batched\_delete\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_document.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_request.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_delete\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_insert\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_insert\_request.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_insert\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_update\_document.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_document.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_request.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_request.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_update\_request\_test.cpp   ()
- src/mongo/s/write\_ops/batched\_upsert\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_upsert\_detail.h   (mongod, tools, mongos)

## [Interface](interface/2)

## [Dependencies](dependencies/2)

-------------

# Group Description
Metadata passed in the request object that does not have to do with the contents of the write command itself.  Currently used to check the shard version in a sharded cluster.

## Files
- src/mongo/s/write\_ops/batched\_request\_metadata.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_request\_metadata.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/batched\_request\_metadata\_test.cpp   ()

## [Interface](interface/3)

## [Dependencies](dependencies/3)

-------------

# Group Description
Schema for the errors that can be returned from write commands.  The two types are write errors and write concern errors.

## Files
- src/mongo/s/write\_ops/wc\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/wc\_error\_detail.h   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_error\_detail.cpp   (mongod, tools, mongos)
- src/mongo/s/write\_ops/write\_error\_detail.h   (mongod, tools, mongos)

## [Interface](interface/4)

## [Dependencies](dependencies/4)
