
# Interface for Replica Set Config
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/rs\_config.cpp

<div></div>

    mongo::ReplSetConfig::MemberCfg::asBson() const

- Used By:

    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetConfig::updateMembers(mongo::List1<mongo::Member>&) const

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::asBson() const

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::legalChange(mongo::ReplSetConfig const&, mongo::ReplSetConfig const&, std::string&)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ReplSetConfig::chainingAllowed() const

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetConfig::groupMx

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetConfig::DEFAULT_HB_TIMEOUT

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::getMajority() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::ReplSetConfig::TagSubgroup::updateLast(mongo::OpTime const&)

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetConfig::makeDirect()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::getHeartbeatTimeout() const

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::make(mongo::HostAndPort const&)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::saveConfigLocally(mongo::BSONObj)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ReplSetConfig::make(mongo::BSONObj, bool)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
