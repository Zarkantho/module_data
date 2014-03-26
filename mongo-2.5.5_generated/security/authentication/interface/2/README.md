
# Interface for Internal Cluster Authentication
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/auth/security\_key.cpp

<div></div>

    mongo::isInternalAuthSet()

- Used By:

    - [src/mongo/db/repl/oplogreader.cpp](../../../replication/replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/isself.cpp](../../../queries/database\_commands)

<div></div>

    mongo::authenticateInternalUser(mongo::DBClientWithCommands*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication/replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication/replication)
    - [src/mongo/db/commands/isself.cpp](../../../queries/database\_commands)
    - [src/mongo/s/shard.cpp](../../../sharding/sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication/replication)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication/replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../security/authorization)
    - [src/mongo/db/repl/manager.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication/replication)

<div></div>

    mongo::setInternalUserAuthParams(mongo::BSONObj)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../process\_management/startup\_initialization)

<div></div>

    mongo::setUpSecurityKey(std::string const&)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../process\_management/startup\_initialization)
