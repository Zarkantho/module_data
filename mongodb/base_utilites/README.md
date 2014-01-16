# base\_utilites

# Module Groups

-------------

Use this in a class to explicitly disallow copying of the class. This can prevent bugs where you  were accidentally copying a class that wasn't safe to copy.

- src/mongo/base/disallow\_copying.h

## Interface

(not used outside this module)

-------------

64 bit atomic counter

- src/mongo/base/counter.h
- src/mongo/base/counter\_test.cpp   ()

## Interface

(not used outside this module)

-------------

Vector and map that delete pointers to elements on destruction. "owning" the memory means you are  responsible for deleting it.

- src/mongo/base/owned\_pointer\_map.h
- src/mongo/base/owned\_pointer\_map\_test.cpp   ()
- src/mongo/base/owned\_pointer\_vector.h
- src/mongo/base/owned\_pointer\_vector\_test.cpp   ()

## Interface

(not used outside this module)

-------------

Status to return errors. StatusWith can return either an error or a value, so we don't have to  use return parameters as arguments to the function.

- src/mongo/base/status-inl.h
- src/mongo/base/status.cpp   (mongod, tools, mongos)
- src/mongo/base/status.h
- src/mongo/base/status\_test.cpp   ()
- src/mongo/base/status\_with.h
- src/mongo/base/error\_codes.err
- src/mongo/base/generate\_error\_codes.py

## Interface


### src/mongo/base/status.cpp

<pre>mongo::operator<<(std::ostream&, mongo::Status const&)</pre>

#### Used By:

- [src/mongo/base/initializer.cpp](../startup\_initialization)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)
- [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/client/examples/httpClientTest.cpp](../cpp\_client\_driver)
- [src/mongo/base/initializer.cpp](../startup\_initialization)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<pre>mongo::operator<<(std::ostream&, mongo::ErrorCodes::Error)</pre>

#### Used By:

- [src/mongo/db/json.cpp](../bson)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/json.cpp](../bson)

<pre>mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)</pre>

#### Used By:

- [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)
- [src/mongo/db/commands/rename\_collection\_common.cpp](../database\_commands)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../sharding)
- [src/mongo/base/initializer\_dependency\_graph.cpp](../startup\_initialization)
- [src/mongo/db/storage\_options.cpp](../storage\_layer\_structure)
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/db/commands/group.cpp](../database\_commands)
- [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/bson/bson\_validate.cpp](../bson)
- [src/mongo/logger/ramlog.cpp](../logging\_system)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/db/repl/rs.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_manager\_global.cpp
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
- [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
- [src/mongo/logger/log\_manager.cpp](../logging\_system)
- [src/mongo/db/matcher/expression\_leaf.cpp](../query\_system)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- [src/mongo/bson/mutable/element.cpp](../bson)
- [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
- [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
- [src/mongo/db/fts/fts\_enabled.cpp](../full\_text\_search\_module)
- [src/mongo/db/matcher/expression\_parser.cpp](../query\_system)
- [src/mongo/bson/util/bson\_extract.cpp](../bson)
- [src/mongo/bson/util/bson\_extract.cpp](../bson)
- [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
- [src/mongo/bson/bson\_validate.cpp](../bson)
- [src/mongo/base/initializer\_dependency\_graph.cpp](../startup\_initialization)
- [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
- [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
- [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/query/canonical\_query.cpp](../query\_system)
- [src/mongo/db/query/internal\_runner.cpp](../query\_system)
- [src/mongo/tools/mongobridge\_options.cpp](../tools)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/base/initializer.cpp](../startup\_initialization)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/db/query/cached\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/server\_parameters.cpp](../startup\_initialization)
- [src/mongo/db/index/s2\_access\_method.cpp](../indexing)
- [src/mongo/db/ops/field\_checker.cpp](../update\_system)
- [src/mongo/db/query/query\_planner.cpp](../query\_system)
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/query/parsed\_projection.cpp](../query\_system)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/logger/log\_manager.cpp](../logging\_system)
- [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/util/log.cpp](../logging\_system)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- [src/mongo/util/fail\_point\_registry.cpp](../utilities)
- [src/mongo/db/query/plan\_cache.cpp](../query\_system)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/tools/tool\_logger.cpp](../tools)
- [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
- [src/mongo/db/query/explain\_plan.cpp](../query\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
- [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
- [src/mongo/util/fail\_point\_registry.cpp](../utilities)
- [src/mongo/util/time\_support.cpp](../utilities)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/base/initializer.cpp](../startup\_initialization)
- [src/mongo/db/exec/projection\_exec.cpp](../query\_system)
- [src/mongo/unittest/unittest.cpp](../unit\_tests)
- [src/mongo/client/init.cpp](../cpp\_client\_driver)
- [src/mongo/db/matcher/expression\_parser\_tree.cpp](../query\_system)
- [src/mongo/tools/mongodump\_options.cpp](../tools)
- [src/mongo/base/parse\_number.cpp](../base\_utilites)
- [src/mongo/tools/mongooplog\_options.cpp](../tools)
- [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/db/ops/update\_driver.cpp](../update\_system)
- [src/mongo/bson/mutable/document.cpp](../bson)
- src/mongo/db/modules/subscription/src/sasl/mongo\_gssapi.cpp
- src/mongo/client/sasl\_client\_session.cpp
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/db/query/single\_solution\_runner.cpp](../query\_system)
- [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/ops/path\_support.cpp](../update\_system)
- [src/mongo/tools/mongostat\_options.cpp](../tools)
- [src/mongo/db/auth/authorization\_manager\_global.cpp](../authentication)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/ops/log\_builder.cpp](../update\_system)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
- [src/mongo/db/index/hash\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)
- [src/mongo/util/background.cpp](../utilities)
- [src/mongo/db/ops/insert.cpp](../query\_system)
- [src/mongo/util/time\_support.cpp](../utilities)
- [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

<pre>mongo::Status::operator!=(mongo::ErrorCodes::Error) const</pre>

#### Used By:

- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp

<pre>mongo::Status::operator==(mongo::Status const&) const</pre>

#### Used By:

- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)

<pre>mongo::Status::operator==(mongo::ErrorCodes::Error) const</pre>

#### Used By:

- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/db/auth/role\_graph.cpp](../authentication)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/bson/util/bson\_extract.cpp](../bson)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/bson/util/bson\_extract.cpp](../bson)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)

<pre>mongo::Status::toString() const</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/tools/mongoexport\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- [src/mongo/client/examples/rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/tools/tool\_options.cpp](../tools)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/s/mongos\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/tools/mongotop\_options\_init.cpp](../tools)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/framework\_options\_init.cpp](../unit\_tests)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/client/examples/whereExample.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongoexport\_options\_init.cpp](../tools)
- [src/mongo/tools/mongorestore\_options\_init.cpp](../tools)
- [src/mongo/tools/mongostat\_options\_init.cpp](../tools)
- [src/mongo/db/ops/update\_driver.cpp](../update\_system)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/db/exec/projection.cpp](../query\_system)
- [src/mongo/tools/mongobridge\_options.cpp](../tools)
- [src/mongo/db/commands/get\_last\_error.cpp](../database\_commands)
- [src/mongo/tools/bsondump\_options\_init.cpp](../tools)
- [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/mongofiles\_options\_init.cpp](../tools)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- [src/mongo/tools/mongobridge\_options\_init.cpp](../tools)
- [src/mongo/client/examples/first.cpp](../cpp\_client\_driver)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/tools/mongodump\_options\_init.cpp](../tools)
- [src/mongo/client/examples/second.cpp](../cpp\_client\_driver)
- [src/mongo/client/examples/clientTest.cpp](../cpp\_client\_driver)
- [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/client/examples/tutorial.cpp](../cpp\_client\_driver)
- [src/mongo/db/mongod\_options\_init.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp](../sharding)
- [src/mongo/tools/mongoimport\_options\_init.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
- [src/mongo/db/matcher/matcher.cpp](../query\_system)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_d.cpp
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- src/mongo/db/modules/subscription/src/sasl/sasl\_options.cpp
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/shell/shell\_options\_init.cpp](../mongo\_shell)
- [src/mongo/tools/mongooplog\_options\_init.cpp](../tools)
- [src/mongo/client/examples/authTest.cpp](../cpp\_client\_driver)
- [src/mongo/db/cap.cpp](../storage\_layer\_structure)

<pre>mongo::Status::operator!=(mongo::Status const&) const</pre>

#### Used By:

- [src/mongo/db/json.cpp](../bson)
- [src/mongo/db/auth/action\_set.cpp](../authentication)
- [src/mongo/base/initializer\_dependency\_graph.cpp](../startup\_initialization)
- [src/mongo/db/json.cpp](../bson)
- [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)
- [src/mongo/base/initializer\_dependency\_graph.cpp](../startup\_initialization)
- [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/base/initializer.cpp](../startup\_initialization)
- [src/mongo/base/initializer.cpp](../startup\_initialization)

<pre>mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)</pre>

#### Used By:

- [src/mongo/unittest/temp\_dir.cpp](../unit\_tests)
- src/mongo/db/modules/subscription/src/sasl/auxprop\_mongodb\_internal.cpp
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/db/write\_concern.cpp](../replication)
- [src/mongo/db/ops/modifier\_unset.cpp](../update\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/s/cluster\_client\_internal.cpp](../sharding)
- [src/mongo/db/query/lite\_parsed\_query.cpp](../query\_system)
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
- [src/mongo/db/json.cpp](../bson)
- [src/mongo/db/repl/rs.cpp](../replication)
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp
- [src/mongo/db/structure/record\_store.cpp](../storage\_layer\_structure)
- [src/mongo/util/options\_parser/option\_section.cpp](../startup\_initialization)
- [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/audit/audit\_options.cpp
- [src/mongo/base/initializer\_dependency\_graph.cpp](../startup\_initialization)
- [src/mongo/db/ops/modifier\_object\_replace.cpp](../update\_system)
- [src/mongo/db/matcher/expression\_where.cpp](../query\_system)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/ops/modifier\_pop.cpp](../update\_system)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)
- [src/mongo/db/json.cpp](../bson)
- [src/mongo/db/ops/modifier\_bit.cpp](../update\_system)
- [src/mongo/tools/tool\_options.cpp](../tools)
- src/mongo/db/modules/subscription/src/audit/audit\_log\_domain.cpp
- [src/mongo/shell/shell\_options.cpp](../mongo\_shell)
- [src/mongo/db/auth/authz\_manager\_external\_state.cpp](../authentication)
- [src/mongo/s/config\_upgrade\_helpers.cpp](../sharding)
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/util/options\_parser/constraints.cpp](../startup\_initialization)
- [src/mongo/db/matcher/expression\_parser\_text.cpp](../query\_system)
- [src/mongo/db/ops/modifier\_rename.cpp](../update\_system)
- [src/mongo/db/matcher/expression\_parser.cpp](../query\_system)
- [src/mongo/bson/util/bson\_extract.cpp](../bson)
- [src/mongo/bson/util/bson\_extract.cpp](../bson)
- [src/mongo/db/ops/modifier\_push.cpp](../update\_system)
- [src/mongo/db/jsobj.cpp](../bson)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/base/initializer\_dependency\_graph.cpp](../startup\_initialization)
- [src/mongo/db/ops/modifier\_current\_date.cpp](../update\_system)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
- src/mongo/db/modules/subscription/src/sasl/canon\_mongodb\_internal.cpp
- [src/mongo/db/matcher/expression\_parser\_geo.cpp](../query\_system)
- [src/mongo/db/ops/modifier\_set.cpp](../update\_system)
- [src/mongo/db/commands/write\_commands/write\_commands\_common.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/query/canonical\_query.cpp](../query\_system)
- [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)
- [src/mongo/util/options\_parser/value.cpp](../startup\_initialization)
- [src/mongo/db/initialize\_server\_global\_state.cpp](../startup\_initialization)
- [src/mongo/util/net/ssl\_options.cpp](../network)
- [src/mongo/base/initializer.cpp](../startup\_initialization)
- src/mongo/client/sasl\_client\_authenticate\_impl.cpp
- [src/mongo/db/fts/fts\_spec.cpp](../full\_text\_search\_module)
- [src/mongo/db/ops/field\_checker.cpp](../update\_system)
- [src/mongo/db/fts/fts\_language.cpp](../full\_text\_search\_module)
- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/auth/role\_graph\_update.cpp](../authentication)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/query/parsed\_projection.cpp](../query\_system)
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/db/ops/modifier\_compare.cpp](../update\_system)
- src/mongo/db/modules/subscription/src/sasl/sasl\_authentication\_session.cpp
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/util/fail\_point\_registry.cpp](../utilities)
- src/mongo/db/modules/subscription/src/sasl/sasl\_commands.cpp
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
- [src/mongo/util/options\_parser/option\_description.cpp](../startup\_initialization)
- [src/mongo/logger/rotatable\_file\_manager.cpp](../logging\_system)
- [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/s/config\_upgrade.cpp](../sharding)
- [src/mongo/db/auth/user\_management\_commands\_parser.cpp](../authentication)
- [src/mongo/client/sasl\_client\_authenticate.cpp](../cpp\_client\_driver)
- [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
- [src/mongo/util/fail\_point\_registry.cpp](../utilities)
- [src/mongo/logger/rotatable\_file\_writer.cpp](../logging\_system)
- [src/mongo/util/time\_support.cpp](../utilities)
- [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)
- [src/mongo/db/auth/authorization\_session.cpp](../authentication)
- [src/mongo/base/initializer.cpp](../startup\_initialization)
- [src/mongo/db/exec/projection\_exec.cpp](../query\_system)
- [src/mongo/db/auth/role\_graph.cpp](../authentication)
- src/mongo/db/modules/subscription/src/audit/audit\_command.cpp
- [src/mongo/db/matcher/expression\_parser\_tree.cpp](../query\_system)
- [src/mongo/s/dbclient\_shard\_resolver.cpp](../sharding)
- [src/mongo/db/ops/update\_driver.cpp](../update\_system)
- [src/mongo/logger/rotatable\_file\_writer.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/sasl/mongo\_gssapi.cpp
- src/mongo/client/sasl\_client\_session.cpp
- [src/mongo/db/ops/modifier\_inc.cpp](../update\_system)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/ops/modifier\_add\_to\_set.cpp](../update\_system)
- [src/mongo/db/ops/path\_support.cpp](../update\_system)
- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/ops/log\_builder.cpp](../update\_system)
- [src/mongo/util/options\_parser/environment.cpp](../startup\_initialization)
- [src/mongo/db/ops/modifier\_pull\_all.cpp](../update\_system)
- [src/mongo/db/auth/user\_document\_parser.cpp](../authentication)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp](../authentication)
- [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)
- [src/mongo/db/ops/insert.cpp](../query\_system)
- [src/mongo/util/time\_support.cpp](../utilities)
- [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)

-------------

Number to string conversion   Why use these: is this somehow fast/safe? somehow JSON-aware?

- src/mongo/base/parse\_number.cpp   (cppclientdriver)
- src/mongo/base/parse\_number.h
- src/mongo/base/parse\_number\_test.cpp   ()

## Interface


### src/mongo/base/parse\_number.cpp

<pre>mongo::Status mongo::parseNumberFromStringWithBase<unsigned int>(mongo::StringData const&, int, unsigned int*)</pre>

#### Used By:

- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/db/jsobj.cpp](../bson)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<pre>mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)</pre>

#### Used By:

- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/documenttests.cpp](../unit\_tests)
- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- [src/mongo/dbtests/mock/mock\_remote\_db\_server.cpp](../unit\_tests)
- [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
- src/mongo/db/modules/subscription/src/audit/impersonate\_helpers\_s.cpp
- [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
- [src/mongo/s/chunk\_manager\_targeter.cpp](../sharding)
- [src/mongo/s/strategy\_single.cpp](../sharding)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
- [src/mongo/db/queryutil.cpp](../query\_system)
- [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
- [src/mongo/db/fts/fts\_command\_mongos.cpp](../full\_text\_search\_module)
- [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
- [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/shell/shell\_utils\_extended.cpp](../mongo\_shell)
- [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/db/query/index\_bounds.cpp](../query\_system)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/db/cloner.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
- [src/mongo/bson/mutable/element.cpp](../bson)
- [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
- [src/mongo/db/index/2d\_access\_method.cpp](../indexing)
- [src/mongo/db/commands/server\_status.cpp](../database\_commands)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/util/version.cpp](../utilities)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
- [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/repl/rs\_config.cpp](../replication)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/s/collection\_metadata.cpp](../sharding)
- [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
- [src/mongo/s/write\_ops/write\_op.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/cluster\_write.cpp](../sharding)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/commands/distinct.cpp](../database\_commands)
- [src/mongo/scripting/v8\_profiler.cpp](../javascript\_libraries)
- [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
- [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
- [src/mongo/tools/restore.cpp](../tools)
- [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
- [src/mongo/s/write\_ops/batch\_write\_op.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/s/version\_manager.cpp](../sharding)
- [src/mongo/dbtests/jsontests.cpp](../unit\_tests)
- [src/mongo/db/commands/connection\_status.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp
- [src/mongo/db/server\_options\_helpers.cpp](../startup\_initialization)
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
- [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
- [src/mongo/s/d\_state.cpp](../sharding)
- [src/mongo/s/metadata\_loader.cpp](../sharding)
- [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/s/commands\_public.cpp](../database\_commands)
- src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
- [src/mongo/db/pipeline/value.cpp](../aggregation\_framework)
- [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)
- [src/mongo/db/query/type\_explain.cpp](../query\_system)
- [src/mongo/s/d\_migrate.cpp](../sharding)
- [src/mongo/s/commands\_admin.cpp](../database\_commands)
- [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/db/projection.cpp](../query\_system)
- [src/mongo/s/d\_merge.cpp](../sharding)
- [src/mongo/s/chunk.cpp](../sharding)
- [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)
- [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)
- [src/mongo/db/commands/mr.cpp](../database\_commands)
- [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
- [src/mongo/db/geo/hash.cpp](../geo\_queries)
- [src/mongo/s/mongo\_version\_range.cpp](../sharding)
- [src/mongo/db/exec/projection\_exec.cpp](../query\_system)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/s/strategy.cpp](../sharding)
- [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/bson/mutable/document.cpp](../bson)
- [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/tools/oplog.cpp](../tools)
- [src/mongo/client/examples/authTest.cpp](../cpp\_client\_driver)
- [src/mongo/db/instance.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
- [src/mongo/s/d\_logic.cpp](../sharding)
- [src/mongo/util/version.cpp](../utilities)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/geo/shapes.cpp](../geo\_queries)
- [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
- [src/mongo/s/type\_chunk.cpp](../sharding)
- [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)

<pre>mongo::Status mongo::parseNumberFromStringWithBase<unsigned long long>(mongo::StringData const&, int, unsigned long long*)</pre>

#### Used By:

- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<pre>mongo::Status mongo::parseNumberFromStringWithBase<double>(mongo::StringData const&, int, double*)</pre>

#### Used By:

- [src/mongo/db/server\_parameters.cpp](../startup\_initialization)
- [src/mongo/dbtests/jstests.cpp](../unit\_tests)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)

<pre>mongo::Status mongo::parseNumberFromStringWithBase<int>(mongo::StringData const&, int, int*)</pre>

#### Used By:

- [src/mongo/util/time\_support.cpp](../utilities)
- [src/mongo/util/version.cpp](../utilities)
- [src/mongo/util/options\_parser/options\_parser.cpp](../startup\_initialization)
- [src/mongo/db/server\_parameters.cpp](../startup\_initialization)
- [src/mongo/util/version.cpp](../utilities)
- [src/mongo/util/time\_support.cpp](../utilities)
- [src/mongo/db/commands/parameters.cpp](../database\_commands)

<pre>mongo::Status mongo::parseNumberFromStringWithBase<long long>(mongo::StringData const&, int, long long*)</pre>

#### Used By:

- [src/mongo/db/server\_parameters.cpp](../startup\_initialization)
- [src/mongo/db/json.cpp](../bson)
- [src/mongo/db/json.cpp](../bson)

-------------

The StringData class is a wrapper around a char* that can be constructed from either std::string  and a char* without copying the buffer. This is because a StringData doesn't free the buffer, so  unlike std::string it doesn't need to have its own copy.   Why: use for speed? is this similar to other classes people might be   familiar with from elsewhere?

- src/mongo/base/string\_data-inl.h
- src/mongo/base/string\_data.cpp   (cppclientdriver)
- src/mongo/base/string\_data.h
- src/mongo/base/string\_data\_test.cpp   ()

## Interface


### src/mongo/base/string\_data.cpp

<pre>mongo::operator<<(std::ostream&, mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)
- [src/mongo/logger/log\_severity.cpp](../logging\_system)
- [src/mongo/db/json.cpp](../bson)
- [src/mongo/db/auth/authorization\_manager.cpp](../authentication)
- src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
- [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
- [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
- src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/json.cpp](../bson)
- [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp
- [src/mongo/db/commands.cpp](../database\_commands)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
- [src/mongo/logger/message\_event\_utf8\_encoder.cpp](../logging\_system)
- src/mongo/db/modules/subscription/src/audit/audit\_indexes\_collections\_databases.cpp
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/logger/log\_severity.cpp](../logging\_system)
- [src/mongo/db/database.cpp](../storage\_layer\_structure)
- [src/mongo/db/clientlistplugin.cpp](../database\_web\_accesss)
- [src/mongo/db/query/plan\_cache.cpp](../query\_system)
- [src/mongo/db/storage/extent.cpp](../storage\_layer\_structure)
- src/mongo/db/modules/subscription/src/audit/audit\_application\_message.cpp
- src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
- [src/mongo/db/d\_concurrency.cpp](../concurrency)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/field\_ref.cpp](../update\_system)

<pre>mongo::StringData::Hasher::operator()(mongo::StringData const&) const</pre>

#### Used By:

- [src/mongo/db/ops/modifier\_table.cpp](../update\_system)
- [src/mongo/scripting/engine\_v8.cpp](../javascript\_libraries)
