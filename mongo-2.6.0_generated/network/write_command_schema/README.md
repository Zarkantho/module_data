# Write Command Schema
This module contains the code for interacting with the format for the requests and responses sent over the wire in the write commands wire protocol.  Note that because the write commands are actually build on top of the command operation in the old wire protocol, this format is actually not working with raw buffers and binary offsets, but is instead dealing with the BSON objects that are sent as the payload of the command and the command response.  For this we have a library to convert to and from C++ objects to BSON objects using a specified schema.

See https://github.com/10gen/specifications/blob/master/source/write-commands.rst for the complete specification.


-------------

## Write Commands Response Schema
Schema for the responses to write commands.

#### Files
- [src/mongo/s/write\_ops/batched\_command\_response.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_command_response.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_command\_response.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_command_response.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_command\_response\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_command_response_test.cpp)   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Write Commands Request Schema Interface
This contains the interface for dealing with the schema of the various write commands.  Note that this class does not actually contain the schema, but instead just multiplexes between the various write command types, calling straight through to the classes for each type when appropriate.

#### Files
- [src/mongo/s/write\_ops/batched\_command\_request.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_command_request.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_command\_request.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_command_request.h)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Write Commands Request Schema
These files contain the schema for the various write commands.  Some of the classes are for schema restrictions that we have on nested objects.  For example, an update command has an overall schema, but the update objects that we send with the command have a schema of their own.

#### Files
- [src/mongo/s/write\_ops/batched\_delete\_document.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_delete_document.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_delete\_document.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_delete_document.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_delete\_request.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_delete_request.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_delete\_request.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_delete_request.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_delete\_request\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_delete_request_test.cpp)   ()
- [src/mongo/s/write\_ops/batched\_insert\_request.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_insert_request.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_insert\_request.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_insert_request.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_insert\_request\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_insert_request_test.cpp)   ()
- [src/mongo/s/write\_ops/batched\_update\_document.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_update_document.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_update\_document.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_update_document.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_update\_request.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_update_request.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_update\_request.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_update_request.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_update\_request\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_update_request_test.cpp)   ()
- [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_upsert_detail.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_upsert\_detail.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_upsert_detail.h)   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Write Commands Operation Metadata
Metadata passed in the request object that does not have to do with the contents of the write command itself.  Currently used to check the shard version in a sharded cluster.

#### Files
- [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_request_metadata.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_request\_metadata.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_request_metadata.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/batched\_request\_metadata\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/batched_request_metadata_test.cpp)   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Write Commands Errors Schema
Schema for the errors that can be returned from write commands.  The two types are write errors and write concern errors.

#### Files
- [src/mongo/s/write\_ops/wc\_error\_detail.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/wc_error_detail.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/wc\_error\_detail.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/wc_error_detail.h)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/write\_error\_detail.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/write_error_detail.cpp)   (mongod, tools, mongos)
- [src/mongo/s/write\_ops/write\_error\_detail.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/write_ops/write_error_detail.h)   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)
