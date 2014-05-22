
# Interface for Server Parameters
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/server\_parameters.cpp

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Used By:

    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/conn\_pool\_options.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/conn\_pool\_options.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ExportedServerParameter<int>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/conn\_pool\_options.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    typeinfo for mongo::ServerParameter

- Used By:

    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/conn\_pool\_options.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Used By:

    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ExportedServerParameter<double>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Used By:

    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/conn\_pool\_options.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/db/commands/parameters.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../../../../network/write\_commands)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
