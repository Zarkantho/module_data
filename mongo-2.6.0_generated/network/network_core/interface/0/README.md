
# Interface for Base Wire Protocol Format
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/dbmessage.cpp

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, void*, int, int, int, long long)

- Used By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::replyToQuery(int, mongo::AbstractMessagingPort*, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Message::toString() const

- Used By:

    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)

### src/mongo/util/net/message.cpp

<div></div>

    mongo::doesOpGetAResponse(int)

- Used By:

    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
