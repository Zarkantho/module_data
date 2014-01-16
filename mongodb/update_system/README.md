# update\_system

# Module Groups

-------------

libupdate.a (only used by libupdate\_driver.a). This is the new code for handling update  operations:   is this stuff only called from update.cpp?

- src/mongo/db/ops/modifier\_add\_to\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_add\_to\_set.h
- src/mongo/db/ops/modifier\_add\_to\_set\_test.cpp   ()
- src/mongo/db/ops/modifier\_bit.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_bit.h
- src/mongo/db/ops/modifier\_bit\_test.cpp   ()
- src/mongo/db/ops/modifier\_compare.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_compare.h
- src/mongo/db/ops/modifier\_compare\_test.cpp   ()
- src/mongo/db/ops/modifier\_current\_date.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_current\_date.h
- src/mongo/db/ops/modifier\_current\_date\_test.cpp   ()
- src/mongo/db/ops/modifier\_inc.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_inc.h
- src/mongo/db/ops/modifier\_inc\_test.cpp   ()
- src/mongo/db/ops/modifier\_interface.h
- src/mongo/db/ops/modifier\_object\_replace.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_object\_replace.h
- src/mongo/db/ops/modifier\_object\_replace\_test.cpp   ()
- src/mongo/db/ops/modifier\_pop.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pop.h
- src/mongo/db/ops/modifier\_pop\_test.cpp   ()
- src/mongo/db/ops/modifier\_pull.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pull.h
- src/mongo/db/ops/modifier\_pull\_all.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_pull\_all.h
- src/mongo/db/ops/modifier\_pull\_all\_test.cpp   ()
- src/mongo/db/ops/modifier\_pull\_test.cpp   ()
- src/mongo/db/ops/modifier\_push.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_push.h
- src/mongo/db/ops/modifier\_push\_sorter.h
- src/mongo/db/ops/modifier\_push\_sorter\_test.cpp   ()
- src/mongo/db/ops/modifier\_push\_test.cpp   ()
- src/mongo/db/ops/modifier\_rename.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_rename.h
- src/mongo/db/ops/modifier\_rename\_test.cpp   ()
- src/mongo/db/ops/modifier\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_set.h
- src/mongo/db/ops/modifier\_set\_test.cpp   ()
- src/mongo/db/ops/modifier\_unset.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_unset.h
- src/mongo/db/ops/modifier\_unset\_test.cpp   ()

## Interface

(not used outside this module)

-------------

libupdate\_driver.a. This is the external interface to the new update system:

- src/mongo/db/ops/modifier\_table.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_table.h
- src/mongo/db/ops/modifier\_table\_test.cpp   ()
- src/mongo/db/ops/update\_driver.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/update\_driver.h
- src/mongo/db/ops/update\_driver\_test.cpp   ()

## Interface


### src/mongo/db/ops/update\_driver.cpp

<pre>mongo::UpdateDriver::modsAffectIndices() const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::~UpdateDriver()</pre>

#### Used By:

- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::CanonicalQuery const*, mongo::mutablebson::Document&) const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::modOptions() const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::makeOplogEntryQuery(mongo::BSONObj const&, bool) const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<pre>mongo::UpdateDriver::setLogOp(bool)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::isDocReplacement() const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::refreshIndexKeys(mongo::IndexPathSet const&)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)</pre>

#### Used By:

- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::UpdateDriver::parse(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<pre>mongo::UpdateDriver::setContext(mongo::ModifierInterface::ExecInfo::UpdateContext)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::BSONObj const&, mongo::mutablebson::Document&) const</pre>

#### Used By:

- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<pre>mongo::UpdateDriver::update(mongo::StringData const&, mongo::mutablebson::Document*, mongo::BSONObj*, mongo::FieldRefSet*)</pre>

#### Used By:

- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

-------------

Utilities for the new update system (libupdate\_common.a)

- src/mongo/db/ops/path\_support.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/path\_support.h
- src/mongo/db/ops/path\_support\_test.cpp   ()
- src/mongo/db/ops/log\_builder.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/log\_builder.h
- src/mongo/db/ops/log\_builder\_test.cpp   ()
- src/mongo/db/ops/field\_checker.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/field\_checker.h
- src/mongo/db/ops/field\_checker\_test.cpp   ()

## Interface

(not used outside this module)

-------------

Other things used by the update system. TODO: figure out what these are for.

- src/mongo/db/ops/update\_lifecycle.h
- src/mongo/db/ops/update\_lifecycle\_impl.cpp   (mongod, tools)
- src/mongo/db/ops/update\_lifecycle\_impl.h
- src/mongo/db/ops/update\_request.h
- src/mongo/db/ops/update\_result.h

## Interface


### src/mongo/db/ops/update\_lifecycle\_impl.cpp

<pre>mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<pre>vtable for mongo::UpdateLifecycleImpl</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

-------------

Utilites for managing dotted field names such as "a.b.c". For example, has things like  "isPrefixOf".   is there any relationship between this and bson/ or bson/mutable ?

- src/mongo/db/field\_ref.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_ref.h
- src/mongo/db/field\_ref\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_ref\_set.h
- src/mongo/db/field\_ref\_set\_test.cpp   ()
- src/mongo/db/field\_ref\_test.cpp   ()

## Interface


### src/mongo/db/field\_ref.cpp

<pre>mongo::FieldRef::parse(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/matcher/path.cpp](../query\_system)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/s/collection\_metadata.cpp](../sharding)
- [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)

<pre>mongo::FieldRef::getPart(unsigned long) const</pre>

#### Used By:

- [src/mongo/db/matcher/path\_internal.cpp](../query\_system)
- [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/matcher/path.cpp](../query\_system)

<pre>mongo::FieldRef::dottedField(unsigned long) const</pre>

#### Used By:

- [src/mongo/db/matcher/path.cpp](../query\_system)
- [src/mongo/db/exec/and\_sorted.cpp](../query\_system)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/db/exec/or.cpp](../query\_system)
- [src/mongo/db/exec/and\_hash.cpp](../query\_system)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/db/exec/fetch.cpp](../query\_system)

<pre>mongo::FieldRef::equalsDottedField(mongo::StringData const&) const</pre>

#### Used By:

- [src/mongo/db/exec/and\_hash.cpp](../query\_system)
- [src/mongo/db/exec/fetch.cpp](../query\_system)
- [src/mongo/db/exec/and\_sorted.cpp](../query\_system)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/db/exec/text.cpp](../query\_system)
- [src/mongo/db/exec/2dcommon.cpp](../query\_system)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/db/exec/or.cpp](../query\_system)

### src/mongo/db/field\_ref\_set.cpp

<pre>mongo::FieldRefSet::findConflicts(mongo::FieldRef const*, mongo::FieldRefSet*) const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::FieldRefSet::toString() const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::FieldRefSet::fillFrom(std::vector<mongo::FieldRef*, std::allocator<mongo::FieldRef*> > const&)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::FieldRefSet::FieldRefSet()</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::FieldRefSet::keepShortest(mongo::FieldRef const*)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)
