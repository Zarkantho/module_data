
# Interface for Oplog Reader
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/oplogreader.cpp

<div></div>

    mongo::replAuthenticate(mongo::DBClientBase*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::OplogReader::tailingQuery(char const*, mongo::BSONObj const&, mongo::BSONObj const*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::OplogReader::connect(std::string const&)

- Used By:

    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::OplogReader::query(char const*, mongo::Query, int, int, mongo::BSONObj const*)

- Used By:

    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::OplogReader::tailingQueryGTE(char const*, mongo::OpTime, mongo::BSONObj const*)

- Used By:

    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)

<div></div>

    mongo::OplogReader::connect(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::OplogReader::OplogReader()

- Used By:

    - [src/mongo/tools/oplog.cpp](../../../../tools/tools)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
