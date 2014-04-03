
# Interface for User Roles
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/auth/role\_graph\_builtin\_roles.cpp

<div></div>

    mongo::RoleGraph::generateUniversalPrivileges(std::vector<mongo::Privilege, std::allocator<mongo::Privilege> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/dbeval.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../queries/database\_commands)

### src/mongo/db/auth/role\_name.cpp

<div></div>

    mongo::RoleName::RoleName(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/tools/restore.cpp](../../../../tools/tools)
