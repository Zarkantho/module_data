
# Interface for Background Operations
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/background.cpp

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    typeinfo for mongo::PeriodicTask

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::running() const

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::cancel()

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::PeriodicTask::startRunningPeriodicTasks()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::PeriodicTask::~PeriodicTask()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::go()

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/bgsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)

<div></div>

    mongo::BackgroundJob::wait(unsigned int)

- Used By:

    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)

<div></div>

    mongo::PeriodicTask::PeriodicTask()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/client/connpool.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    typeinfo for mongo::BackgroundJob

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../../security/authorization)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../../security/authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/util/net/sock.cpp](../../../../network/network\_core)
    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/consensus.cpp](../../../../replication/consensus)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/d\_globals.cpp](../../../../dead\_code/legacy\_code)

### src/mongo/util/concurrency/task.cpp

<div></div>

    vtable for mongo::task::Task

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    typeinfo for mongo::task::Server

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::task::Server::send(boost::function<void ()>)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    vtable for mongo::task::Server

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::task::Task::run()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::task::Task::Task()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::task::Task::setUp()

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::task::repeat(mongo::task::Task*, unsigned int)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::task::Task::halt()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::task::Server::doWork()

- Used By:

    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/manager.cpp](../../../../replication/replica\_set\_state)

<div></div>

    typeinfo for mongo::task::Task

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/s/cursors.cpp](../../../../sharding/routing)

<div></div>

    mongo::task::fork(mongo::task::Task*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../../replication/replica\_set\_state)
