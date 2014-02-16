
# Interface

### src/mongo/s/distlock.cpp

<div></div>

    mongo::ScopedDistributedLock::ScopedDistributedLock(mongo::ConnectionString const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authentication)

<div></div>

    mongo::setLockPingerEnabled(bool)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../unit\_tests)

<div></div>

    mongo::ScopedDistributedLock::acquire(long long, std::string*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../authentication)
