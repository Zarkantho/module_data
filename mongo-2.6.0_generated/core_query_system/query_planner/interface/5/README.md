
# Interface for Explain Document Schema
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/type\_explain.cpp

<div></div>

    mongo::TypeExplain::setIndexOnly(bool)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getAllPlansAt(unsigned long) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::clauses

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::sizeAllPlans() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isIDHackSet() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::TypeExplain::setNChunkSkips(long long)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::scanAndOrder

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setCursor(mongo::StringData const&)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getIsMultiKey() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isMultiKey

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setIndexBounds(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getClausesAt(unsigned long) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setIDHack(bool)

- Used By:

    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::isIndexBoundsSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setMillis(long long)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::TypeExplain::setScanAndOrder(bool)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getCursor() const

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getIDHack() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::TypeExplain::isNScannedObjectsSet() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::TypeExplain::getIndexBounds() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setIndexFilterApplied(bool)

- Used By:

    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getNScannedObjects() const

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getScanAndOrder() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::TypeExplain()

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::isScanAndOrderSet() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setNScannedObjects(long long)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::setNScanned(long long)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::getNScanned() const

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::isIsMultiKeySet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::indexBounds

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isCursorSet() const

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::addToAllPlans(mongo::TypeExplain*)

- Used By:

    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::isAllPlansSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setIsMultiKey(bool)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::isNScannedSet() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::TypeExplain::isClausesSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::sizeClauses() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getN() const

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::TypeExplain::setNScannedAllPlans(long long)

- Used By:

    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::setNScannedObjectsAllPlans(long long)

- Used By:

    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::allPlans

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setServer(mongo::StringData const&)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::TypeExplain::cursor

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::TypeExplain::setNYields(long long)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::TypeExplain::setN(long long)

- Used By:

    - [src/mongo/db/query/eof\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
