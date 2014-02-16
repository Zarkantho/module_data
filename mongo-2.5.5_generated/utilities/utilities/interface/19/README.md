
# Interface

### src/mongo/platform/process\_id.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Used By:

    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ProcessId::getCurrent()

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/bson/oid.cpp](../bson)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ProcessId::toString() const

- Used By:

    - [src/mongo/db/log\_process\_details.cpp](../logging\_system)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/s/version\_mongos.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::ProcessId::asLongLong() const

- Used By:

    - [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

### src/mongo/platform/random.cpp

<div></div>

    mongo::PseudoRandom::PseudoRandom(unsigned int)

- Used By:

    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

<div></div>

    mongo::SecureRandom::create()

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../sharding)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../sharding)

<div></div>

    mongo::PseudoRandom::nextInt64()

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../cpp\_client\_driver)
    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

### src/mongo/util/processinfo.cpp

<div></div>

    mongo::ProcessInfo::systemInfo

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)

<div></div>

    mongo::writePidFile(std::string const&)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)

### src/mongo/util/processinfo\_darwin.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::ProcessInfo::blockInMemory(void const*)

- Used By:

    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ProcessInfo::getExtraInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)
    - [src/mongo/db/startup\_warnings.cpp](../startup\_initialization)

<div></div>

    mongo::ProcessInfo::pagesInMemory(void const*, unsigned long, std::vector<char, std::allocator<char> >*)

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../storage\_layer\_structure)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/shell/shell\_utils.cpp](../mongo\_shell)
