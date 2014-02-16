# authentication

# Module Groups

-------------

# Group Description
Action types are things that users are allowed to do to a resource.  For example "shutdown" is an action type.  An action set is a bitmask of action types.

## Files
- src/mongo/db/auth/action\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/action\_set.h   (mongod, tools, mongos)
- src/mongo/db/auth/action\_set\_test.cpp   ()
- src/mongo/db/auth/action\_types.txt   (mongod, tools, mongos)
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp   (mongod, tools, mongos)
- build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.h   (mongod, tools, mongos)
- src/mongo/db/auth/generate\_action\_types.py   (mongod, tools, mongos)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Authapalooza! TODO: actually separate this logically.

## Files
- src/mongo/db/auth/auth\_index\_d.cpp   (mongod, tools)
- src/mongo/db/auth/auth\_index\_d.h   (mongod, tools)
- src/mongo/db/auth/auth\_server\_parameters.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authentication\_session.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_global.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_global.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_manager\_test.cpp   ()
- src/mongo/db/auth/authorization\_session.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_session.h   (mongod, tools, mongos)
- src/mongo/db/auth/authorization\_session\_test.cpp   ()
- src/mongo/db/auth/authz\_documents\_update\_guard.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_documents\_update\_guard.h   (mongod, tools, mongos)
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
- src/mongo/db/auth/authz\_session\_external\_state.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state.h   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_d.cpp   (mongod, tools)
- src/mongo/db/auth/authz\_session\_external\_state\_d.h   (mongod, tools)
- src/mongo/db/auth/authz\_session\_external\_state\_mock.h   ()
- src/mongo/db/auth/authz\_session\_external\_state\_s.cpp   (mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_s.h   (mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_server\_common.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/authz\_session\_external\_state\_server\_common.h   (mongod, tools, mongos)
- src/mongo/db/auth/mongo\_authentication\_session.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/mongo\_authentication\_session.h   (mongod, tools, mongos)
- src/mongo/db/auth/privilege.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/privilege.h   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser.h   (mongod, tools, mongos)
- src/mongo/db/auth/privilege\_parser\_test.cpp   ()
- src/mongo/db/auth/resource\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/resource\_pattern.h   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph.h   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph\_builtin\_roles.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_graph\_test.cpp   ()
- src/mongo/db/auth/role\_graph\_update.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_name.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/role\_name.h   (mongod, tools, mongos)
- src/mongo/db/auth/security\_key.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/security\_key.h   (mongod, tools, mongos)
- src/mongo/db/auth/user.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_cache\_invalidator\_job.cpp   (mongos)
- src/mongo/db/auth/user\_cache\_invalidator\_job.h   (mongos)
- src/mongo/db/auth/user\_document\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_document\_parser.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_document\_parser\_test.cpp   ()
- src/mongo/db/auth/user\_management\_commands\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_management\_commands\_parser.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_name.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_name.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_name\_hash.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/user\_set.h   (mongod, tools, mongos)
- src/mongo/db/auth/user\_set\_test.cpp   ()

## [Interface](interface/1)

## [Dependencies](dependencies/1)
