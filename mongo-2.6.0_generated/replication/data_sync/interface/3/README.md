
# Interface for Sync Source Feedback
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/sync\_source\_feedback.cpp

<div></div>

    mongo::SyncSourceFeedback::forwardSlaveHandshake()

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    vtable for mongo::SyncSourceFeedback

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::SyncSourceFeedback::ensureMe()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::SyncSourceFeedback::associateMember(mongo::BSONObj const&, int)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::SyncSourceFeedback::percolate(mongo::OID const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
