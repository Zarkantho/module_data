
# Interface

### src/mongo/util/progress\_meter.cpp

<div></div>

    mongo::ProgressMeter::hit(int)

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::ProgressMeter::toString() const

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/clientlistplugin.cpp](../web\_server)

<div></div>

    mongo::ProgressMeter::reset(unsigned long long, int, int)

- Used By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/util/mmap.cpp](../mmap)
    - [src/mongo/dbtests/threadedtests.cpp](../unit\_tests)
    - [src/mongo/tools/import.cpp](../tools)
    - [src/mongo/tools/dump.cpp](../tools)
