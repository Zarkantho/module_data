
# Interface for System Profiler
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/introspect.cpp

<div></div>

    mongo::getOrCreateProfileCollection(mongo::Database*, bool, std::string*)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
