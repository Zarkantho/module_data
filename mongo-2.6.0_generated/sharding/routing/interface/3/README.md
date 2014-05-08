
# Interface for Sharded Cursor
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/cursors.cpp

<div></div>

    mongo::ShardedClientCursor::accessed()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::cursorCache

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::CursorCache::removeRef(long long)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::store(boost::shared_ptr<mongo::ShardedClientCursor>, int)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::updateMaxTimeMS(long long, int)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::storeRef(std::string const&, long long, std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::getMaxTimeMS(long long) const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardedClientCursor::sendNextBatch(mongo::Request&, int, mongo::_BufBuilder<mongo::TrivialAllocator>&, int&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::startTimeoutThread()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ShardedClientCursor::INIT_REPLY_BUFFER_SIZE

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardedClientCursor::getId()

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::remove(long long)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::get(long long) const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::gotKillCursors(mongo::Message&)

- Used By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardedClientCursor::getTotalSent() const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ShardedClientCursor::ShardedClientCursor(mongo::QueryMessage&, mongo::ParallelSortClusteredCursor*)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::CursorCache::getRef(long long) const

- Used By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
