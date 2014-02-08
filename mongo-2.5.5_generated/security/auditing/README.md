# auditing

# Module Groups

-------------

# Group Description
Stubs for auditing enterprise module

# Files
- src/mongo/db/audit.cpp   (mongod, tools, mongos)
- src/mongo/db/audit.h   (mongod, tools, mongos)

# Interface

### src/mongo/db/audit.cpp

<div></div>

    mongo::audit::logCommandAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::mutablebson::Document const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logDropAllRolesFromDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logKillCursorsAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../storage\_layer\_structure)
    - [src/mongo/s/cursors.cpp](../sharding)

<div></div>

    mongo::audit::logCreateUser(mongo::ClientBasic*, mongo::UserName const&, bool, mongo::BSONObj const*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logInsertAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logDropUser(mongo::ClientBasic*, mongo::UserName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logRevokePrivilegesFromRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logKillOpAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logDropAllUsersFromDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logRenameCollection(mongo::ClientBasic*, mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logGrantRolesToRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logShutdown(mongo::ClientBasic*)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logRevokeRolesFromUser(mongo::ClientBasic*, mongo::UserName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logCreateCollection(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logDropCollection(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logUpdateUser(mongo::ClientBasic*, mongo::UserName const&, bool, mongo::BSONObj const*, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logDropRole(mongo::ClientBasic*, mongo::RoleName const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logDropDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/db/pdfile.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::appendImpersonatedUsers(mongo::BSONObjBuilder*)

- Used By:

    - [src/mongo/s/shard.cpp](../sharding)
    - [src/mongo/s/dbclient\_multi\_command.cpp](../sharding)

<div></div>

    mongo::audit::logDeleteAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logCreateRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logCreateIndex(mongo::ClientBasic*, mongo::BSONObj const*, mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logRevokeRolesFromRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::parseAndRemoveImpersonatedUserField(mongo::BSONObj, mongo::AuthorizationSession*, std::vector<mongo::UserName, std::allocator<mongo::UserName> >*, bool*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::audit::logGrantRolesToUser(mongo::ClientBasic*, mongo::UserName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logUpdateRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::RoleName, std::allocator<mongo::RoleName> > const*, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const*)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logCreateDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logQueryAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logDropIndex(mongo::ClientBasic*, mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logInProgAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logEnableSharding(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::audit::logUpdateAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logShardCollection(mongo::ClientBasic*, mongo::StringData const&, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::audit::logRemoveShard(mongo::ClientBasic*, mongo::StringData const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::audit::logAddShard(mongo::ClientBasic*, mongo::StringData const&, std::string const&, long long)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../sharding)

<div></div>

    mongo::audit::logReplSetReconfig(mongo::ClientBasic*, mongo::BSONObj const*, mongo::BSONObj const*)

- Used By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::audit::logGrantPrivilegesToRole(mongo::ClientBasic*, mongo::RoleName const&, std::vector<mongo::Privilege, std::allocator<mongo::Privilege> > const&)

- Used By:

    - [src/mongo/db/commands/user\_management\_commands.cpp](../database\_commands)

<div></div>

    mongo::audit::logGetMoreAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/s/strategy.cpp](../sharding)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logFsyncUnlockAuthzCheck(mongo::ClientBasic*, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::audit::logAuthentication(mongo::ClientBasic*, mongo::StringData const&, mongo::UserName const&, mongo::ErrorCodes::Error)

- Used By:

    - [src/mongo/db/commands/authentication\_commands.cpp](../database\_commands)

# Dependencies
(no dependencies outside this module)
