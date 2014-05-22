
# Interface for Ram Log
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/logger/ramlog.cpp

<div></div>

    mongo::RamLog::LineIterator::LineIterator(mongo::RamLog*)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::RamLogAppender::RamLogAppender(mongo::RamLog*)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

<div></div>

    mongo::RamLog::getNames(std::vector<std::string, std::allocator<std::string> >&)

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::RamLog::getIfExists(std::string const&)

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::RamLog::LineIterator::getTotalLinesWritten()

- Used By:

    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::RamLog::toHTML(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Used By:

    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)

<div></div>

    mongo::RamLog::getLine_inlock(unsigned int) const

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::RamLog::get(std::string const&)

- Used By:

    - [src/mongo/db/dbwebserver.cpp](../../../../network/web\_server)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/repl/health.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::RamLog::LineIterator::lastWrite()

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
