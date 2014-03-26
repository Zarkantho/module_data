
# Interface for Mongos Request Handling Implementation
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/request.cpp

<div></div>

    mongo::Request::process(int)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Request::init()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Request::Request(mongo::Message&, mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

### src/mongo/s/strategy.cpp

<div></div>

    mongo::Strategy::commandOp(std::string const&, mongo::BSONObj const&, int, std::string const&, mongo::BSONObj const&, std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> >*)

- Used By:

    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)

<div></div>

    mongo::STRATEGY

- Used By:

    - [src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/db/fts/fts\_command\_mongos.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp](../../../../sharding/sharding)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/sharding)
