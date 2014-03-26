# Authentication
Authentication is the way to securely verify the identity of a user. This is distinct from Authorization, which is what actually determines what each user is allowed to do once authenticated.  There are different mechanisms and protocols to perform authentication.  MongoDB has a challenge response protocol built in, but SASL and Kerberos authentication support requires the enterprise module.


-------------

## Authentication Session
Thread local storage for any transient state needed for authentication mechanisms that are implemented by MongoDB.

#### Files
- src/mongo/db/auth/mongo\_authentication\_session.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/mongo\_authentication\_session.h   (mongod, tools, mongos)
- src/mongo/db/auth/authentication\_session.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Authentication Commands
Command entry point to authentication.

#### Files
- src/mongo/db/commands/authentication\_commands.cpp   (mongod, tools, mongos)
- src/mongo/db/commands/authentication\_commands.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Internal Cluster Authentication
Handles authentication between nodes in a cluster.

#### Files
- src/mongo/db/auth/security\_key.cpp   (mongod, tools, mongos)
- src/mongo/db/auth/security\_key.h   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
