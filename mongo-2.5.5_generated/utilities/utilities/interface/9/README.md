
# Interface

### src/mongo/util/background.cpp

<div></div>

    mongo::BackgroundJob::~BackgroundJob()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authorization)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)

<div></div>

    typeinfo for mongo::PeriodicTask

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../writeback\_listener)
    - [src/mongo/client/connpool.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::running() const

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::cancel()

- Used By:

    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::PeriodicTask::startRunningPeriodicTasks()

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::PeriodicTask::~PeriodicTask()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../writeback\_listener)
    - [src/mongo/client/connpool.cpp](../../../cpp\_client\_driver)

<div></div>

    mongo::BackgroundJob::go()

- Used By:

    - [src/mongo/db/repl/bgsync.cpp](../../../replication)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)

<div></div>

    mongo::BackgroundJob::wait(unsigned int)

- Used By:

    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)

<div></div>

    mongo::PeriodicTask::PeriodicTask()

- Used By:

    - [src/mongo/s/d\_writeback.cpp](../../../writeback\_listener)
    - [src/mongo/client/connpool.cpp](../../../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::BackgroundJob

- Used By:

    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../../../authorization)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Used By:

    - [src/mongo/db/commands/fsync.cpp](../../../database\_commands)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/d\_globals.cpp](../../../legacy\_code)
    - [src/mongo/s/server.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/clientcursor.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/db/repl/write\_concern.cpp](../../../replication)
    - [src/mongo/dbtests/framework.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/auth\_schema\_upgrade\_d.cpp](../../../authorization)
    - [src/mongo/client/replica\_set\_monitor.cpp](../../../cpp\_client\_driver)
    - [src/mongo/db/repl/consensus.cpp](../../../replication)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/util/net/sock.cpp](../../../network\_core)
    - [src/mongo/s/writeback\_listener.cpp](../../../writeback\_listener)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)

### src/mongo/util/concurrency/task.cpp

<div></div>

    vtable for mongo::task::Task

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    typeinfo for mongo::task::Server

- Used By:

    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    mongo::task::Server::send(boost::function<void ()>)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    vtable for mongo::task::Server

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    mongo::task::Task::run()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    mongo::task::Task::Task()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/db/repl/rs.cpp](../../../replication)
    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/s/cursors.cpp](../../../sharding)

<div></div>

    mongo::task::Task::setUp()

- Used By:

    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/s/cursors.cpp](../../../sharding)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    mongo::task::repeat(mongo::task::Task*, unsigned int)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/s/cursors.cpp](../../../sharding)

<div></div>

    mongo::task::Task::halt()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)

<div></div>

    mongo::task::Server::doWork()

- Used By:

    - [src/mongo/db/repl/manager.cpp](../../../replication)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../replication)

<div></div>

    typeinfo for mongo::task::Task

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
    - [src/mongo/s/cursors.cpp](../../../sharding)

<div></div>

    mongo::task::fork(mongo::task::Task*)

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../../../replication)
