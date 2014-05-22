
# Interface for Distributed Lock
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/distlock.cpp

<div></div>

    mongo::DistributedLock::isLockHeld(double, std::string*)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::setLockPingerEnabled(bool)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ScopedDistributedLock::~ScopedDistributedLock()

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ScopedDistributedLock::acquire(long long, std::string*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ScopedDistributedLock::tryAcquire(std::string*)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DistributedLock::unlock(mongo::BSONObj*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ScopedDistributedLock::ScopedDistributedLock(mongo::ConnectionString const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
