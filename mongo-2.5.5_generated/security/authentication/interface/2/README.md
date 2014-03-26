
# Interface

### src/mongo/db/auth/security\_key.cpp

<div></div>

    mongo::isInternalAuthSet()

- Used By:

    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)

<div></div>

    mongo::authenticateInternalUser(mongo::DBClientWithCommands*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/commands/isself.cpp](../../../database\_commands)
    - [src/mongo/s/shard.cpp](../../../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/repl/oplogreader.cpp](../../../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_config.cpp](../../../replication)

<div></div>

    mongo::setInternalUserAuthParams(mongo::BSONObj)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)

<div></div>

    mongo::setUpSecurityKey(std::string const&)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../startup\_initialization)
