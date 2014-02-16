
# Interface

### src/mongo/db/dbhelpers.cpp

<div></div>

    mongo::Helpers::findById(mongo::Client&, char const*, mongo::BSONObj, mongo::BSONObj&, bool*, bool*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Helpers::ensureIndex(char const*, mongo::BSONObj, bool, char const*)

- Used By:

    - [src/mongo/db/auth/auth\_index\_d.cpp](../../../authentication)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::Helpers::RemoveSaver::goingToDelete(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)

<div></div>

    mongo::Helpers::findById(mongo::Collection*, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)

<div></div>

    mongo::Helpers::RemoveSaver::~RemoveSaver()

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Helpers::toKeyFormat(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Helpers::RemoveSaver::RemoveSaver(std::string const&, std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Helpers::removeRange(mongo::KeyRange const&, bool, bool, mongo::Helpers::RemoveSaver*, bool, bool)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../sharding)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::reverseNaturalObj

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)

<div></div>

    mongo::Helpers::findAll(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/structure/catalog/cap.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::Helpers::inferKeyPattern(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Helpers::getLast(char const*, mongo::BSONObj&)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../replication)

<div></div>

    mongo::Helpers::putSingleton(char const*, mongo::BSONObj)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)

<div></div>

    mongo::Helpers::upsert(std::string const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, mongo::BSONObj&, bool)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/catalog/database.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../../../authentication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/health.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)

<div></div>

    mongo::Helpers::putSingletonGod(char const*, mongo::BSONObj, bool)

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)

<div></div>

    mongo::Helpers::emptyCollection(char const*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)

<div></div>

    mongo::Helpers::findOne(mongo::StringData const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)

<div></div>

    mongo::Helpers::getLocsInRange(mongo::KeyRange const&, long long, std::set<mongo::DiskLoc, std::less<mongo::DiskLoc>, std::allocator<mongo::DiskLoc> >*, long long*, long long*)

- Used By:

    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../unit\_tests)
