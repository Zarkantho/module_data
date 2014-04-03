
# Interface for Replica Set Heartbeats
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/heartbeat.cpp

<div></div>

    mongo::HeartbeatInfo::numPings

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::requestHeartbeat(std::string const&, std::string const&, std::string const&, mongo::BSONObj&, int, int&, bool)

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
