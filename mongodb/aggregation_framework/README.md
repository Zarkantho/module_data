# aggregation\_framework

# Module Groups

-------------

# Group Description
should be a library ;(   who calls/owns this stuff?

# Files
- src/mongo/db/pipeline/accumulator.h
- src/mongo/db/pipeline/accumulator\_add\_to\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_avg.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_first.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_last.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_min\_max.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_push.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/accumulator\_sum.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document.h
- src/mongo/db/pipeline/document\_internal.h
- src/mongo/db/pipeline/document\_source.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source.h
- src/mongo/db/pipeline/document\_source\_bson\_array.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_command\_shards.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_cursor.cpp   (mongod, tools)
- src/mongo/db/pipeline/document\_source\_geo\_near.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_group.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_limit.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_match.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_out.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_project.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_redact.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_skip.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_sort.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/document\_source\_unwind.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/expression.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/expression.h
- src/mongo/db/pipeline/expression\_context.h
- src/mongo/db/pipeline/field\_path.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/field\_path.h
- src/mongo/db/pipeline/pipeline.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/pipeline.h
- src/mongo/db/pipeline/pipeline\_d.cpp   (mongod, tools)
- src/mongo/db/pipeline/pipeline\_d.h
- src/mongo/db/pipeline/pipeline\_optimizations.h
- src/mongo/db/pipeline/value.cpp   (mongod, tools, mongos)
- src/mongo/db/pipeline/value.h
- src/mongo/db/pipeline/value\_internal.h

# Interface

### src/mongo/db/pipeline/accumulator\_avg.cpp

<div></div>

    mongo::AccumulatorAvg::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_first.cpp

<div></div>

    mongo::AccumulatorFirst::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_last.cpp

<div></div>

    mongo::AccumulatorLast::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_min\_max.cpp

<div></div>

    mongo::AccumulatorMinMax::createMax()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::AccumulatorMinMax::createMin()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_sum.cpp

<div></div>

    mongo::AccumulatorSum::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document.cpp

<div></div>

    vtable for mongo::DocumentStorage

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::MutableDocument::getNestedField(mongo::FieldPath const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentStorage::clone() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Document const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::Document::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::MutableDocument::getNestedField(std::vector<mongo::Position, std::allocator<mongo::Position> > const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentStorage::findField(mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::Document::toBson() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::DocumentStorage::appendField(mongo::StringData)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

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

    mongo::Document::toBsonWithMetaData() const

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Document::deserializeForSorter(mongo::BufReader&, mongo::Document::SorterDeserializeSettings const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Document::compare(mongo::Document const&, mongo::Document const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Document::getNestedField(mongo::FieldPath const&, std::vector<mongo::Position, std::allocator<mongo::Position> >*) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source.cpp

<div></div>

    mongo::DocumentSource::depsToProjection(std::set<std::string, std::less<std::string>, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::DocumentSource

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_bson\_array.cpp

<div></div>

    mongo::DocumentSourceBsonArray::create(mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_command\_shards.cpp

<div></div>

    mongo::DocumentSourceCommandShards::create(std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_cursor.cpp

<div></div>

    mongo::DocumentSourceCursor::create(std::string const&, long long, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentSourceCursor::getLimit() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_geo\_near.cpp

<div></div>

    mongo::DocumentSourceGeoNear::create(boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_group.cpp

<div></div>

    mongo::DocumentSourceGroup::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_limit.cpp

<div></div>

    mongo::DocumentSourceLimit::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentSourceLimit::create(boost::intrusive_ptr<mongo::ExpressionContext> const&, long long)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_match.cpp

<div></div>

    mongo::DocumentSourceMatch::redactSafePortion() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentSourceMatch::getQuery() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    mongo::DocumentSourceMatch::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::DocumentSourceMatch

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp

<div></div>

    mongo::DocumentSourceMergeCursors::create(std::vector<std::pair<mongo::ConnectionString, long long>, std::allocator<std::pair<mongo::ConnectionString, long long> > > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_out.cpp

<div></div>

    typeinfo for mongo::DocumentSourceOut

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_project.cpp

<div></div>

    mongo::DocumentSourceProject::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_sort.cpp

<div></div>

    mongo::DocumentSourceSort::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::DocumentSourceSort

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_unwind.cpp

<div></div>

    mongo::DocumentSourceUnwind::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/expression.cpp

<div></div>

    mongo::Expression::ObjectCtx::ObjectCtx(int)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionConstant::parse(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::addOperand(boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionFieldPath::create(std::string const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Expression::parseOperand(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::optimize()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ExpressionAdd

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionCoerceToBool::create(boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ExpressionNary

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::addField(mongo::FieldPath const&, boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::ExpressionNary

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::addToDocument(mongo::MutableDocument&, mongo::Document const&, mongo::Variables*) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionConstant::create(mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::serialize(bool) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ExpressionAnd

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::includePath(std::string const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Expression::parseObject(mongo::BSONObj, mongo::Expression::ObjectCtx*, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::create()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::createRoot()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Expression::parseExpression(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::addDependencies(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&, std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

### src/mongo/db/pipeline/field\_path.cpp

<div></div>

    mongo::FieldPath::FieldPath(std::string const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::FieldPath::getPath(bool) const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

<div></div>

    mongo::FieldPath::FieldPath(std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

<div></div>

    mongo::FieldPath::tail() const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/pipeline.cpp

<div></div>

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::splitForSharded()

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::serialize() const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::stitch()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::canRunInMongos() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::getInitialQuery() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::writeExplainOps() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Pipeline::commandName

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

### src/mongo/db/pipeline/pipeline\_d.cpp

<div></div>

    mongo::PipelineD::prepareCursorSource(boost::intrusive_ptr<mongo::Pipeline> const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

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

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
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

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<div></div>

    mongo::Value::coerceToLong() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::getWidestNumeric(mongo::BSONType, mongo::BSONType)

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

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
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

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::Value::Value(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<div></div>

    mongo::Value::toString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

# Dependencies

### src/mongo/db/pipeline/accumulator\_add\_to\_set.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/accumulator\_avg.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/accumulator\_min\_max.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/accumulator\_push.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/accumulator\_sum.cpp

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/document.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    MurmurHash3_x86_32(void const*, int, unsigned int, void*)

- Provided By:

    - [src/third\_party/murmurhash3/MurmurHash3.cpp](../murmurhash3)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/pipeline/document\_source.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_bson\_array.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_command\_shards.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_cursor.cpp

<div></div>

    mongo::TypeExplain::getScanAndOrder() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::isScanAndOrderSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::scanAndOrder

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::MaxBytesToReturnToClientAtOnce

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::TypeExplain::getAllPlansAt(unsigned long) const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::clauses

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::ClientCursor::erase(long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::isClausesSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::sizeAllPlans() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::TypeExplain::isIndexBoundsSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::sizeClauses() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::TypeExplain::isAllPlansSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::TypeExplain::isIsMultiKeySet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::getClausesAt(unsigned long) const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::indexBounds

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::isCursorSet() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::getIndexBounds() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::getCursor() const

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursorPin::c() const

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::cursor

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::TypeExplain::allPlans

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::TypeExplain::isMultiKey

- Provided By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/pipeline/document\_source\_geo\_near.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_group.cpp

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    snappy::RawUncompress(char const*, unsigned long, char*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    snappy::Compress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

### src/mongo/db/pipeline/document\_source\_limit.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_match.cpp

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONElement::getGtLtOp(int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

### src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp

<div></div>

    vtable for mongo::ScopedDbConnection

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientCursor::more()

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientCursor::_finishConsInit()

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::pool

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::ScopedDbConnection::_setSocketTimeout()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::DBClientCursor::initLazy(bool)

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientCursor::next()

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientCursor::initLazyFinish(bool&)

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    vtable for mongo::DBClientCursor

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBConnectionPool::get(mongo::ConnectionString const&, double)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::DBClientCursor::~DBClientCursor()

- Provided By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::ConnectionString::_finishInit()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ScopedDbConnection::~ScopedDbConnection()

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::AScopedConnection::_numConnections

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBConnectionPool::release(std::string const&, mongo::DBClientBase*)

- Provided By:

    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

### src/mongo/db/pipeline/document\_source\_out.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBClientWithCommands::getLastErrorString(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

### src/mongo/db/pipeline/document\_source\_project.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_redact.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_skip.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/document\_source\_sort.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    snappy::RawUncompress(char const*, unsigned long, char*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    snappy::Compress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

### src/mongo/db/pipeline/document\_source\_unwind.cpp

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/db/pipeline/expression.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

### src/mongo/db/pipeline/field\_path.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

### src/mongo/db/pipeline/pipeline.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Privilege::Privilege(mongo::ResourcePattern const&, mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/privilege.cpp](../authentication)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::IntrusiveCounterUnsigned::addRef() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::IntrusiveCounterUnsigned::release() const

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    mongo::BSONElement::Array() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Provided By:

    - [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ActionType::remove

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::Command::parseResourcePattern(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ResourcePattern::toString() const

- Provided By:

    - [src/mongo/db/auth/resource\_pattern.cpp](../authentication)

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::ActionType::find

- Provided By:

    - build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    typeinfo for mongo::IntrusiveCounterUnsigned

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

### src/mongo/db/pipeline/pipeline\_d.cpp

<div></div>

    mongo::ShardedConnectionInfo::addHook()

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Provided By:

    - [src/mongo/db/query/canonical\_query.cpp](../query\_system)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for mongo::DBDirectClient

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::ShardingState::getVersion(std::string const&) const

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::ClientCursor::~ClientCursor()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Runner*, int, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Provided By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

### src/mongo/db/pipeline/value.cpp

<div></div>

    mongo::typeName(mongo::BSONType)

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    MurmurHash3_x86_32(void const*, int, unsigned int, void*)

- Provided By:

    - [src/third\_party/murmurhash3/MurmurHash3.cpp](../murmurhash3)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::OID::hash_combine(unsigned long&) const

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::time_t_to_String_short(long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::RCString::create(mongo::StringData)

- Provided By:

    - [src/mongo/util/intrusive\_counter.cpp](../utilities)

-------------

# Group Description
Generic interface for getting and merging sorted streams of documents. Only used in aggregation.   +1 "only used in aggregation" :)

# Files
- src/mongo/db/sorter/sorter.cpp
- src/mongo/db/sorter/sorter.h
- src/mongo/db/sorter/sorter\_test.cpp   ()

# Interface

### src/mongo/db/sorter/sorter\_test.cpp

<div></div>

    mongo::isMongos()

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

# Dependencies

### src/mongo/db/sorter/sorter\_test.cpp

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::Suite::Suite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::log()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::unittest::Suite

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::unittest::TempDir::~TempDir()

- Provided By:

    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    snappy::RawUncompress(char const*, unsigned long, char*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::filesystem3::detail::is_empty(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    snappy::Compress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::join()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::unittest::TempDir::TempDir(std::string const&)

- Provided By:

    - [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::demangleName(std::type_info const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    mongo::unittest::Suite::~Suite()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Code for external sort. This sits inside the sorter, and the sorter "spills over" to disk if  external sorting is allowed.   who calls this?

# Files
- src/mongo/db/extsort.cpp   (mongod, tools)
- src/mongo/db/extsort.h

# Interface

### src/mongo/db/extsort.cpp

<div></div>

    mongo::BSONObjExternalSorter::BSONObjExternalSorter(mongo::ExternalSortComparison const*, long)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)

# Dependencies

### src/mongo/db/extsort.cpp

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::killCurrentOp

- Provided By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    snappy::RawUncompress(char const*, unsigned long, char*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    snappy::Compress(char const*, unsigned long, std::string*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::create_directories(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    snappy::GetUncompressedLength(char const*, unsigned long, unsigned long*)

- Provided By:

    - [src/third\_party/snappy/snappy.cc](../snappy)

<div></div>

    mongo::storageGlobalParams

- Provided By:

    - [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)

-------------

# Group Description
I believe this is just used in External Sort, but it's standing on its own here without a  description.

# Files
- src/mongo/db/sort\_phase\_one.h

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)
