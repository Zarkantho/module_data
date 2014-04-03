
# Interface for Parallel Cursor
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/client/parallel.cpp

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(std::set<mongo::ServerAndQuery, std::less<mongo::ServerAndQuery>, std::allocator<mongo::ServerAndQuery> > const&, std::string const&, mongo::Query const&, int, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Future::CommandResult::join(int)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Future::spawnCommand(std::string const&, std::string const&, mongo::BSONObj const&, int, mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ParallelSortClusteredCursor::getShardCursor(mongo::Shard const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::init()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::more()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ParallelSortClusteredCursor::~ParallelSortClusteredCursor()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::ParallelSortClusteredCursor(mongo::QuerySpec const&, mongo::CommandInfo const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::isSharded()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::getQueryShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::explain(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ParallelSortClusteredCursor::next()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ParallelSortClusteredCursor::getPrimary()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
