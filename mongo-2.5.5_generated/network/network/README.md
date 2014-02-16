# network

# Module Groups

-------------

# Group Description
Network library   can you say a few words about:   - what this does   - who uses it   - how to use it?

## Files
- src/mongo/util/net/listen.cpp   (mongod, tools, mongos)
- src/mongo/util/net/listen.h   (mongod, tools, mongos)
- src/mongo/util/net/hostandport.h   (mongod, tools, mongos)
- src/mongo/util/net/message.cpp   (mongod, tools, mongos)
- src/mongo/util/net/message.h   (mongod, tools, mongos)
- src/mongo/util/net/message\_port.cpp   (mongod, tools, mongos)
- src/mongo/util/net/message\_port.h   (mongod, tools, mongos)
- src/mongo/util/net/httpclient.cpp   (mongod, tools, mongos)
- src/mongo/util/net/httpclient.h   (mongod, tools, mongos)
- src/mongo/util/net/sock.cpp   (mongod, tools, mongos)
- src/mongo/util/net/sock.h   (mongod, tools, mongos)
- src/mongo/util/net/sock\_test.cpp   ()
- src/mongo/util/net/socket\_poll.cpp   (mongod, tools, mongos)
- src/mongo/util/net/socket\_poll.h   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_manager.cpp   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_manager.h   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_options.h   (mongod, tools, mongos)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Top level (?) of handling incoming network connections on mongod and mongos. Inherits from  Listener (listen.h).

## Files
- src/mongo/util/net/message\_server.h   (mongod, mongos)
- src/mongo/util/net/message\_server\_port.cpp   (mongod, mongos)

## [Interface](interface/1)

## [Dependencies](dependencies/1)
