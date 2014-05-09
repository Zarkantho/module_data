# Authorization
Authorization is the process of determining what a user is allowed to do in the system.  The five main entities in our authorization system are Users, Resources, Actions, Privileges, and Roles.

1. A User is the basic entity that operates on the system. 2. A Resource is something that the system provides that can be acted on by a User. 3. An Action is something that a User can do to a Resource. 4. A Privilege is a set of Actions that can performed on a given Resource. 5. A Role is a set of Priviliges.

Users can be assigned Roles and Privileges, which describe what the user is allowed to do.

Note that some of this code, such as the code to access the User data, is shared by the Authentication module.


-------------

## Action Types
Action types are things that users are allowed to do to a resource.  For example "shutdown" is an action type.  An action set is a bitmask of action types.

#### Files
- src/mongo/db/auth/action\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/action\_set.h   (mongod, tools, mongos)
- src/mongo/db/auth/action\_set\_test.cpp   ()
- src/mongo/db/auth/action\_types.txt   (mongod, tools, mongos)
- build/darwin/ssl/mongo/db/auth/action\_type.h   (mongod, tools, mongos)
- build/darwin/ssl/mongo/db/auth/action\_type.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/generate\_action\_types.py   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Privileges
A privilege represents a set of actions that can be performed on a given resource.

#### Files
- src/mongo/db/auth/privilege.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/privilege.h   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser.h   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Resource Pattern
A resource is something that the database contains or provides that a user can perform actions on.  A Resource Pattern is a representation of a specific resource or a class of resources.

#### Files
- src/mongo/db/auth/resource\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/resource\_pattern.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## User Roles
A role is a set of privileges that a user with that role is allowed to perform.  Roles can contain other roles, and should be organized in a directed acyclic graph.  The role graph is the in memory representation of our persistent role data, so this code has the logic to pull the role documents and convert to the in memory graph representation.

#### Files
- src/mongo/db/auth/role\_graph.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph.h   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph\_builtin\_roles.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph\_test.cpp   ()
- src/mongo/db/auth/role\_graph\_update.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_name.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_name.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Users
A representation of a user.  This contains the user credentials as well as the roles and privileges of the user.  Because it contains both the credentials and the privileges, this is used by both Authentication and Authorization.

#### Files
- src/mongo/db/auth/user.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_document\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_document\_parser.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_document\_parser\_test.cpp   ()
- src/mongo/db/auth/user\_name.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_name.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_name\_hash.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## User Management Commands
Commands to manage user and role definitions.

#### Files
- src/mongo/db/auth/user\_management\_commands\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_management\_commands\_parser.h   (mongod, tools, mongos)
- src/mongo/db/commands/user\_management\_commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/user\_management\_commands.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## User Cache Invalidator
Background Job that periodically invalidates user data cached on the mongos.

#### Files
- src/mongo/db/auth/user\_cache\_invalidator\_job.cpp   (mongos)
- src/mongo/db/auth/user\_cache\_invalidator\_job.h   (mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Authorization Data Indexes
Indexes on mongod for collections containing authorization data.

#### Files
- src/mongo/db/auth/auth\_index\_d.cpp   (mongod, tools)
- src/mongo/db/auth/auth\_index\_d.h   (mongod, tools)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Authorization Manager
Abstraction around the persistent authorization data, such as users and roles.  Also handles upgrade of the authorization data, and ensures that concurrent access is handled correctly.

#### Files
- src/mongo/db/auth/authorization\_manager.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_global.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_global.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_test.cpp   ()
- src/mongo/db/auth/authz\_documents\_update\_guard.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_documents\_update\_guard.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Authorization Manager Specialization
Abstraction around the component of the Authorization Manager implementation that must be specialized for mongos or mongod.

#### Files
- src/mongo/db/auth/authz\_manager\_external\_state.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state.h   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp   (mongod, tools)
- src/mongo/db/auth/authz\_manager\_external\_state\_d.h   (mongod, tools)
- src/mongo/db/auth/authz\_manager\_external\_state\_local.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_local.h   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp   (tools)
- src/mongo/db/auth/authz\_manager\_external\_state\_mock.h   (tools)
- src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp   (mongos)
- src/mongo/db/auth/authz\_manager\_external\_state\_s.h   (mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Authorization Data Upgrade Commands
Commands that are the entry point to upgrade the authentication data.  Calls into the Authorization Manager to actually do the upgrade.

#### Files
- src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp   (mongod, tools)
- src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp   (mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

## Authorization Session
Handles authorization of actions in a session, which in this case is a session/thread/connection.  This state is all thread local, and keeps track of what users we have authenticated as for this session/thread/connection.

#### Files
- src/mongo/db/auth/authorization\_session.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_session.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_session\_test.cpp   ()
- src/mongo/db/auth/user\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_set.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_set\_test.cpp   ()

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

## Authorization Session Specialization
Abstraction around the component of the Authorization Session implementation that must be specialized for mongos or mongod.

#### Files
- src/mongo/db/auth/authz\_session\_external\_state.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state.h   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_d.cpp   (mongod, tools)
- src/mongo/db/auth/authz\_session\_external\_state\_d.h   (mongod, tools)
- src/mongo/db/auth/authz\_session\_external\_state\_mock.h   ()
- src/mongo/db/auth/authz\_session\_external\_state\_s.cpp   (mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_s.h   (mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_server\_common.h   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)
