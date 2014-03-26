# Network

The MongoDB network stack

## Modules

### [Cpp Client Driver](cpp\_client\_driver)
TODO: cpp\_client\_driver description

### [SSL](ssl)
Support for SSL connections

### [REST Client](rest\_client)
Client for accessing the mongodb rest api.  Only used by mongostat when run with the "--http" option.

### [Network Core](network\_core)
The core network stack upon which everything that interacts with the network in MongoDB is built.

### [Write Command Schema](write\_command\_schema)
This module contains the code for interacting with the format for the requests and responses sent over the wire in the write commands wire protocol.  Note that because the write commands are actually build on top of the command operation in the old wire protocol, this format is actually not working with raw buffers and binary offsets, but is instead dealing with the BSON objects that are sent as the payload of the command and the command response.  For this we have a library to convert to and from C++ objects to BSON objects using a specified schema.
See https://github.com/10gen/specifications/blob/master/source/write-commands.rst for the complete specification.

### [Write Commands](write\_commands)
New write commands for new wire protocol. The new "write commands" are all implemented as server Commands run using "db.$cmd.findOne(...)".  The legacy write operations did not recieve responses, but commands do recieve responses, so sending writes as "commands" ensures that all writes get a response.  Note that this means the "write commands" are layered on top of the legacy wire protocol, rather than replacing it.

### [Web Server](web\_server)
Database web server.  Handles various types of requests, such as rest and jsonp.  This is completely orthogonal to our wire protocol

