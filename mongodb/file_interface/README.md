# file\_interface

# Module Groups

-------------

# Group Description
Abstraction layer for dealing with files. It's basically the read(2), open(2), and write(2)  interface for posix, and something else for Windows. Not used by mmap code, and does not depend  on file allocator library. Use this if you need a file but not a memory mapped file.

# Files
- src/mongo/util/file.cpp   (mongod, cppclientdriver, tools, mongos)
- src/mongo/util/file.h   (mongod, cppclientdriver, tools, mongos)

# Interface

### src/mongo/util/file.cpp

<div></div>

    mongo::File::write(unsigned long long, char const*, unsigned int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::File::File()

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::File::open(char const*, bool, bool)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::File::truncate(unsigned long long)

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::File::~File()

- Used By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<div></div>

    mongo::File::is_open() const

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::File::freeSpace(std::string const&)

- Used By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::File::fsync() const

- Used By:

    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::File::len()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::File::read(unsigned long long, char*, unsigned int)

- Used By:

    - [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/db/dur\_journal.cpp](../journaling)

# Dependencies

### src/mongo/util/file.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)
