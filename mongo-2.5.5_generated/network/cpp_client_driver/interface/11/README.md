
# Interface

### src/mongo/client/parallel.cpp

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(std::set<mongo::ServerAndQuery, std::less<mongo::ServerAndQuery>, std::allocator<mongo::ServerAndQuery> > const&, std::string const&, mongo::Query const&, int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::ParallelSortClusteredCursor::getNS()

- Used By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::Future::CommandResult::join(int)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::getShardCursor(mongo::Shard const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::init()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::more()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(mongo::QuerySpec const&, mongo::CommandInfo const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::isSharded()

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::getQueryShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::explain(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::next()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::ParallelSortClusteredCursor::getPrimary()

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
