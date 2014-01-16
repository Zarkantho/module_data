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

    mongo::AccumulatorAvg::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_first.cpp

    mongo::AccumulatorFirst::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_last.cpp

    mongo::AccumulatorLast::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_min\_max.cpp

    mongo::AccumulatorMinMax::createMax()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::AccumulatorMinMax::createMin()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_sum.cpp

    mongo::AccumulatorSum::create()

- Used By:

    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document.cpp

    vtable for mongo::DocumentStorage

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::MutableDocument::getNestedField(mongo::FieldPath const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::DocumentStorage::clone() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Document const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Document::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::MutableDocument::getNestedField(std::vector<mongo::Position, std::allocator<mongo::Position> > const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::DocumentStorage::findField(mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::Document::toBson() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::DocumentStorage::appendField(mongo::StringData)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::Document::Document(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Document::toString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Document::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Document::toBsonWithMetaData() const

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Document::deserializeForSorter(mongo::BufReader&, mongo::Document::SorterDeserializeSettings const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Document::compare(mongo::Document const&, mongo::Document const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Document::getNestedField(mongo::FieldPath const&, std::vector<mongo::Position, std::allocator<mongo::Position> >*) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source.cpp

    mongo::DocumentSource::depsToProjection(std::set<std::string, std::less<std::string>, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    typeinfo for mongo::DocumentSource

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_bson\_array.cpp

    mongo::DocumentSourceBsonArray::create(mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_command\_shards.cpp

    mongo::DocumentSourceCommandShards::create(std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_cursor.cpp

    mongo::DocumentSourceCursor::create(std::string const&, long long, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    mongo::DocumentSourceCursor::getLimit() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_geo\_near.cpp

    mongo::DocumentSourceGeoNear::create(boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_group.cpp

    mongo::DocumentSourceGroup::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_limit.cpp

    mongo::DocumentSourceLimit::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    mongo::DocumentSourceLimit::create(boost::intrusive_ptr<mongo::ExpressionContext> const&, long long)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_match.cpp

    mongo::DocumentSourceMatch::redactSafePortion() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    mongo::DocumentSourceMatch::getQuery() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    mongo::DocumentSourceMatch::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    typeinfo for mongo::DocumentSourceMatch

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp

    mongo::DocumentSourceMergeCursors::create(std::vector<std::pair<mongo::ConnectionString, long long>, std::allocator<std::pair<mongo::ConnectionString, long long> > > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_out.cpp

    typeinfo for mongo::DocumentSourceOut

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_project.cpp

    mongo::DocumentSourceProject::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_sort.cpp

    mongo::DocumentSourceSort::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

    typeinfo for mongo::DocumentSourceSort

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_unwind.cpp

    mongo::DocumentSourceUnwind::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/expression.cpp

    mongo::Expression::ObjectCtx::ObjectCtx(int)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionConstant::parse(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionNary::addOperand(boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionFieldPath::create(std::string const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Expression::parseOperand(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionNary::optimize()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    vtable for mongo::ExpressionAdd

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionCoerceToBool::create(boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    vtable for mongo::ExpressionNary

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionObject::addField(mongo::FieldPath const&, boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    typeinfo for mongo::ExpressionNary

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionObject::addToDocument(mongo::MutableDocument&, mongo::Document const&, mongo::Variables*) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionConstant::create(mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionNary::serialize(bool) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    vtable for mongo::ExpressionAnd

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionObject::includePath(std::string const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Expression::parseObject(mongo::BSONObj, mongo::Expression::ObjectCtx*, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionObject::create()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionObject::createRoot()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Expression::parseExpression(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::ExpressionNary::addDependencies(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&, std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

### src/mongo/db/pipeline/field\_path.cpp

    mongo::FieldPath::FieldPath(std::string const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::FieldPath::getPath(bool) const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

    mongo::FieldPath::FieldPath(std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

    mongo::FieldPath::tail() const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/pipeline.cpp

    mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Pipeline::splitForSharded()

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Pipeline::run(mongo::BSONObjBuilder&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Pipeline::serialize() const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Pipeline::stitch()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Pipeline::canRunInMongos() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Pipeline::getInitialQuery() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Pipeline::writeExplainOps() const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Pipeline::commandName

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

### src/mongo/db/pipeline/pipeline\_d.cpp

    mongo::PipelineD::prepareCursorSource(boost::intrusive_ptr<mongo::Pipeline> const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

### src/mongo/db/pipeline/value.cpp

    mongo::Value::compare(mongo::Value const&, mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Value const&)

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Value::operator[](mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::ValueStorage::putString(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Value::hash_combine(unsigned long&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::deserializeForSorter(mongo::BufReader&, mongo::Value::SorterDeserializeSettings const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::ValueStorage::putDocument(mongo::Document const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::Value::coerceToLong() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::getWidestNumeric(mongo::BSONType, mongo::BSONType)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::coerceToDate() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::addToBsonArray(mongo::BSONArrayBuilder*) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::Value(mongo::BSONArray const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::getDocument() const

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::Value::getDouble() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

    mongo::Value::coerceToBool() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::coerceToTimestamp() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::operator[](unsigned long) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::coerceToString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::Value(mongo::BSONElement const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

    mongo::operator<<(std::ostream&, mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Value::addToBsonObj(mongo::BSONObjBuilder*, mongo::StringData) const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

    mongo::Value::coerceToInt() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::coerceToDouble() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::ValueStorage::putRegEx(mongo::BSONRegEx const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::ValueStorage::putVector(mongo::RCVector const*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

    mongo::Value::Value(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

    mongo::Value::toString() const

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

-------------

# Group Description
Generic interface for getting and merging sorted streams of documents. Only used in aggregation.   +1 "only used in aggregation" :)

# Files
- src/mongo/db/sorter/sorter.cpp
- src/mongo/db/sorter/sorter.h
- src/mongo/db/sorter/sorter\_test.cpp   ()

# Interface

### src/mongo/db/sorter/sorter\_test.cpp

    mongo::isMongos()

- Used By:

    - [src/mongo/s/grid.cpp](../sharding)
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

-------------

# Group Description
Code for external sort. This sits inside the sorter, and the sorter "spills over" to disk if  external sorting is allowed.   who calls this?

# Files
- src/mongo/db/extsort.cpp   (mongod, tools)
- src/mongo/db/extsort.h

# Interface

### src/mongo/db/extsort.cpp

    mongo::BSONObjExternalSorter::BSONObjExternalSorter(mongo::ExternalSortComparison const*, long)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)

-------------

# Group Description
I believe this is just used in External Sort, but it's standing on its own here without a  description.

# Files
- src/mongo/db/sort\_phase\_one.h

# Interface
(not used outside this module)
