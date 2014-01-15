# network

# Module Groups

-------------

Network library   can you say a few words about:   - what this does   - who uses it   - how to use it?

- src/mongo/util/net/listen.cpp   (mongod, tools, mongos)
- src/mongo/util/net/listen.h
- src/mongo/util/net/hostandport.h
- src/mongo/util/net/message.cpp   (cppclientdriver)
- src/mongo/util/net/message.h
- src/mongo/util/net/message\_port.cpp   (mongod, tools, mongos)
- src/mongo/util/net/message\_port.h
- src/mongo/util/net/httpclient.cpp   (cppclientdriver)
- src/mongo/util/net/httpclient.h
- src/mongo/util/net/sock.cpp   (mongod, tools, mongos)
- src/mongo/util/net/sock.h
- src/mongo/util/net/sock\_test.cpp   ()
- src/mongo/util/net/socket\_poll.cpp   (cppclientdriver)
- src/mongo/util/net/socket\_poll.h
- src/mongo/util/net/ssl\_manager.cpp   (cppclientdriver)
- src/mongo/util/net/ssl\_manager.h
- src/mongo/util/net/ssl\_options.cpp   (mongod, tools, mongos)
- src/mongo/util/net/ssl\_options.h

-------------

Top level (?) of handling incoming network connections on mongod and mongos. Inherits from  Listener (listen.h).

- src/mongo/util/net/message\_server.h
- src/mongo/util/net/message\_server\_port.cpp   (mongod, mongos)
