
# Interface for Progress Meter
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/util/progress\_meter.cpp

<div></div>

    mongo::ProgressMeter::hit(int)

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../queries/indexing)
    - [src/mongo/dbtests/threadedtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/db/dur\_journal.cpp](../../../storage/journaling)
    - [src/mongo/util/mmap.cpp](../../../storage/mmap)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/tools/import.cpp](../../../tools/tools)
    - [src/mongo/db/commands/touch.cpp](../../../queries/database\_commands)

<div></div>

    mongo::ProgressMeter::toString() const

- Used By:

    - [src/mongo/db/curop.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/clientlistplugin.cpp](../../../network/web\_server)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Used By:

    - [src/mongo/db/curop.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/tools/tool.cpp](../../../tools/tools)
    - [src/mongo/db/dur\_journal.cpp](../../../storage/journaling)
    - [src/mongo/util/mmap.cpp](../../../storage/mmap)
    - [src/mongo/dbtests/threadedtests.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/import.cpp](../../../tools/tools)
    - [src/mongo/tools/dump.cpp](../../../tools/tools)
