
# Interface for Heath Status Helpers
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/health.cpp

<div></div>

    mongo::rsLog

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)

<div></div>

    mongo::ReplSetImpl::lastOtherElectableOpTime() const

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ReplSetImpl::findById(unsigned int) const

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/oplogreader.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::_summarizeStatus(mongo::BSONObjBuilder&) const

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)

<div></div>

    mongo::ScopedConn::_map

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::ReplSetImpl::lastOtherOpTime() const

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::fillRsLog(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)

<div></div>

    mongo::ReplSetImpl::_summarizeAsHtml(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Used By:

    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)

<div></div>

    mongo::ScopedConn::mapMutex

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::ReplSetImpl::getMutableMember(unsigned int)

- Used By:

    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::ReplSetImpl::_getOplogDiagsAsHtml(unsigned int, std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&) const

- Used By:

    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)
