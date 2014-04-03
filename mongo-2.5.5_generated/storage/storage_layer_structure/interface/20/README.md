
# Interface for Record Class
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/storage/record.cpp

<div></div>

    mongo::DiskLoc::obj() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/working\_set\_common.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/text.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::Record::touch(bool) const

- Used By:

    - [src/mongo/db/pagefault.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::Record::likelyInPhysicalMemory() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::DiskLoc::rec() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/fetch.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/2dcommon.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Record::_accessing() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/oplogstart.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::Record::MemoryTrackingEnabled

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::DiskLoc::drec() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::Record::likelyInPhysicalMemory(char const*)

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::DiskLoc::ext() const

- Used By:

    - [src/mongo/db/exec/oplogstart.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/tools/dump.cpp](../../../../tools/tools)

<div></div>

    mongo::DeletedRecord::_accessing() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
