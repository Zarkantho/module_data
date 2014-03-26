
# Interface

### src/mongo/db/dbmessage.cpp

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, void*, int, int, int, long long)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../sharding)
    - [src/mongo/s/cursors.cpp](../../../sharding)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Message::toString() const

- Used By:

    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/strategy.cpp](../../../sharding)

### src/mongo/util/net/message.cpp

<div></div>

    mongo::doesOpGetAResponse(int)

- Used By:

    - [src/mongo/s/d\_logic.cpp](../../../writeback\_listener)
