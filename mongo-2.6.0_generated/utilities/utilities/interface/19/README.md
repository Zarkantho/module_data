
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/platform/process\_id.cpp

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)

<div></div>

    mongo::ProcessId::getCurrent()

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/bson/oid.cpp](../../../../bson/bson)
    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ProcessId::asLongLong() const

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ProcessId::toString() const

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/log\_process\_details.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/shell/shell\_utils\_launcher.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/s/version\_mongos.cpp](../../../../process\_management/build\_information)

### src/mongo/platform/random.cpp

<div></div>

    mongo::PseudoRandom::PseudoRandom(unsigned int)

- Used By:

    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::PseudoRandom::PseudoRandom(long long)

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)

<div></div>

    mongo::SecureRandom::create()

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/bson/oid.cpp](../../../../bson/bson)
    - [src/mongo/db/commands/authentication\_commands.cpp](../../../../security/authentication)
    - [src/mongo/db/dur\_journal.cpp](../../../../storage/journaling)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::PseudoRandom::nextInt32()

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::PseudoRandom::nextInt64()

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/kill\_current\_op.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

### src/mongo/util/processinfo.cpp

<div></div>

    mongo::ProcessInfo::systemInfo

- Used By:

    - [src/mongo/util/file\_allocator.cpp](../../../../storage/file\_allocation)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::writePidFile(std::string const&)

- Used By:

    - [src/mongo/db/initialize\_server\_global\_state.cpp](../../../../process\_management/startup\_initialization)

### src/mongo/util/processinfo\_darwin.cpp

<div></div>

    mongo::ProcessInfo::supported()

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ProcessInfo::getResidentSize()

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Used By:

    - [src/mongo/db/structure/btree/btree\_stats.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/db/dbcommands\_generic.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Used By:

    - [src/mongo/db/startup\_warnings.cpp](../../../../process\_management/startup\_initialization)
    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/btree/btree\_stats.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::ProcessInfo::blockInMemory(void const*)

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ProcessInfo::getExtraInfo(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ProcessInfo::pagesInMemory(void const*, unsigned long, std::vector<char, std::allocator<char> >*)

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ProcessInfo::getVirtualMemorySize()

- Used By:

    - [src/mongo/db/commands/server\_status.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/util/mmap.cpp](../../../../storage/data\_files)
    - [src/mongo/shell/shell\_utils.cpp](../../../../mongo\_shell/mongo\_shell)
