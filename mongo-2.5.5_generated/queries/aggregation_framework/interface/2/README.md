
# Interface

### src/mongo/db/pipeline/value.cpp

<div></div>

    mongo::Value::compare(mongo::Value const&, mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Value::operator[](mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::ValueStorage::putString(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Value::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::deserializeForSorter(mongo::BufReader&, mongo::Value::SorterDeserializeSettings const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::ValueStorage::putDocument(mongo::Document const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToLong() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToDate() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::addToBsonArray(mongo::BSONArrayBuilder*) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::getWidestNumeric(mongo::BSONType, mongo::BSONType)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::Value(mongo::BSONArray const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::getDocument() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::Value::getDouble() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToBool() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToTimestamp() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::operator[](unsigned long) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::Value(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Value::addToBsonObj(mongo::BSONObjBuilder*, mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToInt() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToDouble() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::ValueStorage::putRegEx(mongo::BSONRegEx const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::ValueStorage::putVector(mongo::RCVector const*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Value::Value(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::toString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document.cpp

<div></div>

    mongo::MutableDocument::getNestedField(mongo::FieldPath const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentStorage::clone() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Document const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)

<div></div>

    mongo::Document::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::MutableDocument::getNestedField(std::vector<mongo::Position, std::allocator<mongo::Position> > const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::DocumentStorage

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Document::deserializeForSorter(mongo::BufReader&, mongo::Document::SorterDeserializeSettings const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentStorage::findField(mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::Document::toBson() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentStorage::appendField(mongo::StringData)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../sharding)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Document::Document(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Document::toString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Document::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Document::metaFieldTextScore

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    mongo::Document::compare(mongo::Document const&, mongo::Document const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Document::getNestedField(mongo::FieldPath const&, std::vector<mongo::Position, std::allocator<mongo::Position> >*) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
