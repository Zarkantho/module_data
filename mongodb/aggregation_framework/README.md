# aggregation\_framework

# Module Groups

-------------

should be a library ;(   who calls/owns this stuff?

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

## Interface


### src/mongo/db/pipeline/accumulator\_avg.cpp

<pre>mongo::AccumulatorAvg::create()</pre>

#### Used By:

- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_first.cpp

<pre>mongo::AccumulatorFirst::create()</pre>

#### Used By:

- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_last.cpp

<pre>mongo::AccumulatorLast::create()</pre>

#### Used By:

- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_min\_max.cpp

<pre>mongo::AccumulatorMinMax::createMax()</pre>

#### Used By:

- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::AccumulatorMinMax::createMin()</pre>

#### Used By:

- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/accumulator\_sum.cpp

<pre>mongo::AccumulatorSum::create()</pre>

#### Used By:

- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document.cpp

<pre>vtable for mongo::DocumentStorage</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::MutableDocument::getNestedField(mongo::FieldPath const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::DocumentStorage::clone() const</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Document const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Document::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::MutableDocument::getNestedField(std::vector<mongo::Position, std::allocator<mongo::Position> > const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::DocumentStorage::findField(mongo::StringData) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::Document::toBson() const</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::DocumentStorage::appendField(mongo::StringData)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::Document::Document(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Document::toString() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Document::hash_combine(unsigned long&) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Document::toBsonWithMetaData() const</pre>

#### Used By:

- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Document::deserializeForSorter(mongo::BufReader&, mongo::Document::SorterDeserializeSettings const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Document::compare(mongo::Document const&, mongo::Document const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Document::getNestedField(mongo::FieldPath const&, std::vector<mongo::Position, std::allocator<mongo::Position> >*) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source.cpp

<pre>mongo::DocumentSource::depsToProjection(std::set<std::string, std::less<std::string>, std::allocator<std::string> > const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>typeinfo for mongo::DocumentSource</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_bson\_array.cpp

<pre>mongo::DocumentSourceBsonArray::create(mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_command\_shards.cpp

<pre>mongo::DocumentSourceCommandShards::create(std::vector<mongo::Strategy::CommandResult, std::allocator<mongo::Strategy::CommandResult> > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_cursor.cpp

<pre>mongo::DocumentSourceCursor::create(std::string const&, long long, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>mongo::DocumentSourceCursor::getLimit() const</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_geo\_near.cpp

<pre>mongo::DocumentSourceGeoNear::create(boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_group.cpp

<pre>mongo::DocumentSourceGroup::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_limit.cpp

<pre>mongo::DocumentSourceLimit::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>mongo::DocumentSourceLimit::create(boost::intrusive_ptr<mongo::ExpressionContext> const&, long long)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_match.cpp

<pre>mongo::DocumentSourceMatch::redactSafePortion() const</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>mongo::DocumentSourceMatch::getQuery() const</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>mongo::DocumentSourceMatch::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>typeinfo for mongo::DocumentSourceMatch</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_merge\_cursors.cpp

<pre>mongo::DocumentSourceMergeCursors::create(std::vector<std::pair<mongo::ConnectionString, long long>, std::allocator<std::pair<mongo::ConnectionString, long long> > > const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_out.cpp

<pre>typeinfo for mongo::DocumentSourceOut</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

### src/mongo/db/pipeline/document\_source\_project.cpp

<pre>mongo::DocumentSourceProject::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_sort.cpp

<pre>mongo::DocumentSourceSort::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

<pre>typeinfo for mongo::DocumentSourceSort</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/document\_source\_unwind.cpp

<pre>mongo::DocumentSourceUnwind::createFromBson(mongo::BSONElement, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/expression.cpp

<pre>mongo::Expression::ObjectCtx::ObjectCtx(int)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionConstant::parse(mongo::BSONElement, mongo::VariablesParseState const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionNary::addOperand(boost::intrusive_ptr<mongo::Expression> const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionFieldPath::create(std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Expression::parseOperand(mongo::BSONElement, mongo::VariablesParseState const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionNary::optimize()</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>vtable for mongo::ExpressionAdd</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionCoerceToBool::create(boost::intrusive_ptr<mongo::Expression> const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>vtable for mongo::ExpressionNary</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionObject::addField(mongo::FieldPath const&, boost::intrusive_ptr<mongo::Expression> const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>typeinfo for mongo::ExpressionNary</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionObject::addToDocument(mongo::MutableDocument&, mongo::Document const&, mongo::Variables*) const</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionConstant::create(mongo::Value const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionNary::serialize(bool) const</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>vtable for mongo::ExpressionAnd</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionObject::includePath(std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Expression::parseObject(mongo::BSONObj, mongo::Expression::ObjectCtx*, mongo::VariablesParseState const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionObject::create()</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionObject::createRoot()</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Expression::parseExpression(mongo::BSONElement, mongo::VariablesParseState const&)</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::ExpressionNary::addDependencies(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&, std::vector<std::string, std::allocator<std::string> >*) const</pre>

#### Used By:

- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

### src/mongo/db/pipeline/field\_path.cpp

<pre>mongo::FieldPath::FieldPath(std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::FieldPath::getPath(bool) const</pre>

#### Used By:

- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

<pre>mongo::FieldPath::FieldPath(std::vector<std::string, std::allocator<std::string> > const&)</pre>

#### Used By:

- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

<pre>mongo::FieldPath::tail() const</pre>

#### Used By:

- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

### src/mongo/db/pipeline/pipeline.cpp

<pre>mongo::Pipeline::addRequiredPrivileges(mongo::Command*, std::string const&, mongo::BSONObj, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Pipeline::addInitialSource(boost::intrusive_ptr<mongo::DocumentSource>)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Pipeline::splitForSharded()</pre>

#### Used By:

- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Pipeline::run(mongo::BSONObjBuilder&)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Pipeline::serialize() const</pre>

#### Used By:

- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Pipeline::stitch()</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Pipeline::parseCommand(std::string&, mongo::BSONObj const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Pipeline::canRunInMongos() const</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Pipeline::getInitialQuery() const</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)

<pre>mongo::Pipeline::writeExplainOps() const</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Pipeline::commandName</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

### src/mongo/db/pipeline/pipeline\_d.cpp

<pre>mongo::PipelineD::prepareCursorSource(boost::intrusive_ptr<mongo::Pipeline> const&, boost::intrusive_ptr<mongo::ExpressionContext> const&)</pre>

#### Used By:

- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

### src/mongo/db/pipeline/value.cpp

<pre>mongo::Value::compare(mongo::Value const&, mongo::Value const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::operator<<(mongo::BSONObjBuilderValueStream&, mongo::Value const&)</pre>

#### Used By:

- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Value::operator[](mongo::StringData) const</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::ValueStorage::putString(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Value::hash_combine(unsigned long&) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::deserializeForSorter(mongo::BufReader&, mongo::Value::SorterDeserializeSettings const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::ValueStorage::putDocument(mongo::Document const&)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToLong() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::getWidestNumeric(mongo::BSONType, mongo::BSONType)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToDate() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::addToBsonArray(mongo::BSONArrayBuilder*) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::serializeForSorter(mongo::_BufBuilder<mongo::TrivialAllocator>&) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::Value(mongo::BSONArray const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::getDocument() const</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::Value::getDouble() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToBool() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToTimestamp() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::operator[](unsigned long) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToString() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::Value(mongo::BSONElement const&)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)

<pre>mongo::operator<<(std::ostream&, mongo::Value const&)</pre>

#### Used By:

- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/dbtests/pipelinetests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Value::addToBsonObj(mongo::BSONObjBuilder*, mongo::StringData) const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/accumulatortests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToInt() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::coerceToDouble() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::ValueStorage::putRegEx(mongo::BSONRegEx const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::ValueStorage::putVector(mongo::RCVector const*)</pre>

#### Used By:

- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<pre>mongo::Value::Value(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)

<pre>mongo::Value::toString() const</pre>

#### Used By:

- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

-------------

Generic interface for getting and merging sorted streams of documents. Only used in aggregation.   +1 "only used in aggregation" :)

- src/mongo/db/sorter/sorter.cpp
- src/mongo/db/sorter/sorter.h
- src/mongo/db/sorter/sorter\_test.cpp   ()

## Interface


### src/mongo/db/sorter/sorter\_test.cpp

<pre>mongo::isMongos()</pre>

#### Used By:

- [src/mongo/s/grid.cpp](../sharding)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)

-------------

Code for external sort. This sits inside the sorter, and the sorter "spills over" to disk if  external sorting is allowed.   who calls this?

- src/mongo/db/extsort.cpp   (mongod, tools)
- src/mongo/db/extsort.h

## Interface


### src/mongo/db/extsort.cpp

<pre>mongo::BSONObjExternalSorter::BSONObjExternalSorter(mongo::ExternalSortComparison const*, long)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)

-------------

I believe this is just used in External Sort, but it's standing on its own here without a  description.

- src/mongo/db/sort\_phase\_one.h

## Interface

(not used outside this module)
