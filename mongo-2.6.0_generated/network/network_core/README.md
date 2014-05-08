# Network Core
The core network stack upon which everything that interacts with the network in MongoDB is built.


-------------

## Base Wire Protocol Format
The format of the packets in our wire protocol upon which everything else is built.  See http://docs.mongodb.org/meta-driver/latest/legacy/mongodb-wire-protocol/ for the concepts behind it.  WARNING: The names in the server code do not match the names in the documentation.
The Message class has the lowest level buffer management, while the DbMessage class is a wrapper on top of it that helps for dealing with the different types of operations.

#### Files
- src/mongo/db/dbmessage.cpp   (mongod, tools, mongos)
- src/mongo/db/dbmessage.h   (mongod, tools, mongos)
- src/mongo/util/net/message.cpp   (mongod, tools, mongos)
- src/mongo/util/net/message.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Socket
Class providing an abstraction around a network socket.  Also contains the socket exception class.

#### Files
- src/mongo/util/net/sock.cpp   (mongod, tools, mongos)
- src/mongo/util/net/sock.h   (mongod, tools, mongos)
- src/mongo/util/net/sock\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Listener Interface
Interface for a class that listens on a port and accepts incoming connections.  This does not look like a C++ interface because it does not seem to have pure virtual functions, but using this class on its own will eventually cause assertion to fail when a connection is accepted.  This unfortunately turns a compile time check into a runtime check, and makes it harder to tell that this is an interface, but despite that this class is logically an interface and never used on its own.

#### Files
- src/mongo/util/net/listen.cpp   (mongod, tools, mongos)
- src/mongo/util/net/listen.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Message Port
Wrapper around a single socket providing an interface that works with the MongoDB wire protocol classes rather than raw buffers.  Also has methods to run the SSL handshake on the connection, and automatically handles piggybacking data to reduce the total number of network operations.

#### Files
- src/mongo/util/net/message\_port.cpp   (mongod, tools, mongos)
- src/mongo/util/net/message\_port.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## HostAndPort String
Helper class for storing and checking strings of the form "host:port"

#### Files
- src/mongo/util/net/hostandport.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Socket Poll
Code to poll a socket to check if it is still alive.  Useful for connection pooling to check if a connection we are getting from the pool is still good.

#### Files
- src/mongo/util/net/socket\_poll.cpp   (mongod, tools, mongos)
- src/mongo/util/net/socket\_poll.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Message Server
Main entry point into the MongoDB network stack.  The responsibility of this class is to listen on a port and interface, and make callbacks to a "handler" object.  The port, interface, and "handler" object are all passed into the constructor.
Note that mongod and mongos have different "handler" classes.  Currently these are defined in db.cpp and server.cpp, the same files that have the "main()" functions for mongod and mongos.
Note also that the classes that this is built on work with "Message" objects, which is the basic unit in the wire protocol, and what the name of this class is based on.

#### Files
- src/mongo/util/net/message\_server.h   (mongod, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Thread Based Message Server
Thread based implementation of a message server, and helpers. Listens on the provided port and spawns a thread for every new connection.  The thread reads all data from a connection and makes callbacks to the "handler" object that was registered for this message server.

#### Files
- src/mongo/util/net/message\_server\_port.cpp   (mongod, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Async Message Server
Experimental async implementation of a message server.  This is experimental and will probably be deleted before it gets used for real.

#### Files

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Mongos Request Handling Implementation
Implementation of the logic to handle incoming messages on mongos. The Request class is the entry point that decodes the operation type and calls to the STRATEGY object to do the work of handling the specific operation.

#### Files
- src/mongo/s/request.cpp   (mongos)
- src/mongo/s/request.h   (mongod, tools, mongos)
- src/mongo/s/strategy.cpp   (mongos)
- src/mongo/s/strategy.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## GetLastError Data
Globals and helpers for keeping track of the data needed for getLastError (part of legacy wire protocol).  Note that the globals are thread local, and a thread represents a connection, which is why we have getLastError state per thread.

#### Files
- src/mongo/db/lasterror.cpp   (mongod, tools, mongos)
- src/mongo/db/lasterror.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
