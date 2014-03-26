
# Interface for Distributed Lock
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/s/distlock.cpp

<div></div>

    mongo::ScopedDistributedLock::ScopedDistributedLock(mongo::ConnectionString const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)

<div></div>

    mongo::setLockPingerEnabled(bool)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ScopedDistributedLock::acquire(long long, std::string*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)
