
# Interface for Fsync Command
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/commands/fsync.cpp

<div></div>

    mongo::_unlockFsync()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::lockedForWriting()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)

<div></div>

    mongo::filesLockedFsync

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
