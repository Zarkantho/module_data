
# Interface for Condition Variables
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/concurrency/synchronization.cpp

<div></div>

    mongo::NotifyAll::now()

- Used By:

    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)

<div></div>

    mongo::Notification::notifyOne()

- Used By:

    - [src/mongo/db/range\_deleter.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NotifyAll::awaitBeyondNow()

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)

<div></div>

    mongo::Notification::waitToBeNotified()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Notification::Notification()

- Used By:

    - [src/mongo/dbtests/threadedtests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::NotifyAll::NotifyAll()

- Used By:

    - [src/mongo/db/dur\_commitjob.cpp](../../../../storage/journaling)

<div></div>

    mongo::NotifyAll::notifyAll(unsigned long long)

- Used By:

    - [src/mongo/db/dur.cpp](../../../../storage/journaling)
