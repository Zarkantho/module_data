# update\_system

# Module Groups

-------------

# Group Description
libupdate.a (only used by libupdate\_driver.a). This is the new code for handling update  operations:   is this stuff only called from update.cpp?

# Files
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

# Interface
(not used outside this module)

-------------

# Group Description
libupdate\_driver.a. This is the external interface to the new update system:

# Files
- src/mongo/db/ops/modifier\_table.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/modifier\_table.h
- src/mongo/db/ops/modifier\_table\_test.cpp   ()
- src/mongo/db/ops/update\_driver.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/update\_driver.h
- src/mongo/db/ops/update\_driver\_test.cpp   ()

# Interface

### src/mongo/db/ops/update\_driver.cpp

<div></div>

    mongo::UpdateDriver::modsAffectIndices() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::CanonicalQuery const*, mongo::mutablebson::Document&) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::modOptions() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::makeOplogEntryQuery(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::UpdateDriver::setLogOp(bool)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::isDocReplacement() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::refreshIndexKeys(mongo::IndexPathSet const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::UpdateDriver::setContext(mongo::ModifierInterface::ExecInfo::UpdateContext)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::UpdateDriver::populateDocumentWithQueryFields(mongo::BSONObj const&, mongo::mutablebson::Document&) const

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<div></div>

    mongo::UpdateDriver::update(mongo::StringData const&, mongo::mutablebson::Document*, mongo::BSONObj*, mongo::FieldRefSet*)

- Used By:

    - [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

-------------

# Group Description
Utilities for the new update system (libupdate\_common.a)

# Files
- src/mongo/db/ops/path\_support.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/path\_support.h
- src/mongo/db/ops/path\_support\_test.cpp   ()
- src/mongo/db/ops/log\_builder.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/log\_builder.h
- src/mongo/db/ops/log\_builder\_test.cpp   ()
- src/mongo/db/ops/field\_checker.cpp   (mongod, tools, mongos)
- src/mongo/db/ops/field\_checker.h
- src/mongo/db/ops/field\_checker\_test.cpp   ()

# Interface
(not used outside this module)

-------------

# Group Description
Other things used by the update system. TODO: figure out what these are for.

# Files
- src/mongo/db/ops/update\_lifecycle.h
- src/mongo/db/ops/update\_lifecycle\_impl.cpp   (mongod, tools)
- src/mongo/db/ops/update\_lifecycle\_impl.h
- src/mongo/db/ops/update\_request.h
- src/mongo/db/ops/update\_result.h

# Interface

### src/mongo/db/ops/update\_lifecycle\_impl.cpp

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
Utilites for managing dotted field names such as "a.b.c". For example, has things like  "isPrefixOf".   is there any relationship between this and bson/ or bson/mutable ?

# Files
- src/mongo/db/field\_ref.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_ref.h
- src/mongo/db/field\_ref\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_ref\_set.h
- src/mongo/db/field\_ref\_set\_test.cpp   ()
- src/mongo/db/field\_ref\_test.cpp   ()

# Interface

### src/mongo/db/field\_ref.cpp

<div></div>

    mongo::FieldRef::parse(mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/matcher/path.cpp](../query\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/s/collection\_metadata.cpp](../sharding)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)

<div></div>

    mongo::FieldRef::getPart(unsigned long) const

- Used By:

    - [src/mongo/db/matcher/path\_internal.cpp](../query\_system)
    - [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/matcher/path.cpp](../query\_system)

<div></div>

    mongo::FieldRef::dottedField(unsigned long) const

- Used By:

    - [src/mongo/db/matcher/path.cpp](../query\_system)
    - [src/mongo/db/exec/and\_sorted.cpp](../query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)
    - [src/mongo/db/exec/or.cpp](../query\_system)
    - [src/mongo/db/exec/and\_hash.cpp](../query\_system)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
    - [src/mongo/db/exec/fetch.cpp](../query\_system)

<div></div>

    mongo::FieldRef::equalsDottedField(mongo::StringData const&) const

- Used By:

    - [src/mongo/db/exec/and\_hash.cpp](../query\_system)
    - [src/mongo/db/exec/fetch.cpp](../query\_system)
    - [src/mongo/db/exec/and\_sorted.cpp](../query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)
    - [src/mongo/db/exec/text.cpp](../query\_system)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
    - [src/mongo/db/exec/or.cpp](../query\_system)

### src/mongo/db/field\_ref\_set.cpp

<div></div>

    mongo::FieldRefSet::findConflicts(mongo::FieldRef const*, mongo::FieldRefSet*) const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::FieldRefSet::toString() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::FieldRefSet::fillFrom(std::vector<mongo::FieldRef*, std::allocator<mongo::FieldRef*> > const&)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::FieldRefSet::FieldRefSet()

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::FieldRefSet::keepShortest(mongo::FieldRef const*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
