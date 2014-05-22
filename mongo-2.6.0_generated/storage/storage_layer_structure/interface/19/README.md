
# Interface for Record Class
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/storage/record.cpp

<div></div>

    mongo::DiskLoc::obj() const

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/exec/working\_set\_common.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/exec/2d.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/exec/text.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/exec/2dnear.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DiskLoc::ext() const

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Record::touch(bool) const

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::Record::likelyInPhysicalMemory() const

- Used By:

    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::Record::MemoryTrackingEnabled

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::DiskLoc::rec() const

- Used By:

    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::Record::likelyInPhysicalMemory(char const*)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/exec/fetch.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::DiskLoc::drec() const

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Record::_accessing() const

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::DeletedRecord::_accessing() const

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
