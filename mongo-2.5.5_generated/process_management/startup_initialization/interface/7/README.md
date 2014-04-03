
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/server\_parameters.cpp

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    typeinfo for mongo::ServerParameter

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::ExportedServerParameter<int>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)

<div></div>

    mongo::ExportedServerParameter<double>::setFromString(std::string const&)

- Used By:

    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Used By:

    - [src/mongo/db/commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp](../../../../security/authorization)
    - [src/mongo/db/fts/fts\_enabled.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/auth/auth\_server\_parameters.cpp](../../../../security/legacy\_code)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/auth/authorization\_manager\_global.cpp](../../../../security/authorization)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/storage\_options.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/qlog.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/server\_extra\_log\_context.cpp](../../../../process\_management/logging\_system)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replication)
    - [src/mongo/db/commands/parameters.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/sharding\_uncategorized)
