# page\_fault\_utilities

# Module Groups

-------------

# Group Description
Contains the PageFaultException and NoPageFaultsAllowed classes.   where are these used?

# Files
- src/mongo/db/pagefault.cpp   (mongod, tools)
- src/mongo/db/pagefault.h

# Interface

### src/mongo/db/pagefault.cpp

- <pre>mongo::PageFaultRetryableSection::~PageFaultRetryableSection()</pre>
Used By:
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

- <pre>mongo::NoPageFaultsAllowed::NoPageFaultsAllowed()</pre>
Used By:
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

- <pre>mongo::PageFaultException::touch()</pre>
Used By:
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

- <pre>mongo::PageFaultRetryableSection::PageFaultRetryableSection()</pre>
Used By:
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

- <pre>mongo::PageFaultException::PageFaultException(mongo::Record const*)</pre>
Used By:
    - [src/mongo/db/storage/record.cpp](../storage\_layer\_structure)

- <pre>mongo::NoPageFaultsAllowed::~NoPageFaultsAllowed()</pre>
Used By:
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
Code to go in and touch pages so that they are brought into memory.   who calls these?

# Files
- src/mongo/db/prefetch.cpp   (mongod, tools)
- src/mongo/db/prefetch.h

# Interface

### src/mongo/db/prefetch.cpp

- <pre>mongo::prefetchPagesForReplicatedOp(mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
