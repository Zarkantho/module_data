
# Interface

### src/mongo/s/write\_ops/wc\_error\_detail.cpp

<div></div>

    mongo::WCErrorDetail::cloneTo(mongo::WCErrorDetail*) const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)

<div></div>

    mongo::WCErrorDetail::setErrMessage(mongo::StringData const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WCErrorDetail::getErrMessage() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::WCErrorDetail::setErrCode(int)

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WCErrorDetail::getErrCode() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)

<div></div>

    mongo::WCErrorDetail::~WCErrorDetail()

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)

<div></div>

    mongo::WCErrorDetail::setErrInfo(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WCErrorDetail::WCErrorDetail()

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

### src/mongo/s/write\_ops/write\_error\_detail.cpp

<div></div>

    mongo::WriteErrorDetail::getErrMessage() const

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::setErrCode(int)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::WriteErrorDetail()

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::setErrMessage(mongo::StringData const&)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::getErrCode() const

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/cluster\_write.cpp](../../../sharding)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::~WriteErrorDetail()

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::setErrInfo(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::getErrInfo() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::cloneTo(mongo::WriteErrorDetail*) const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::setIndex(int)

- Used By:

    - [src/mongo/s/write\_ops/write\_op.cpp](../../../write\_commands)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::getIndex() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_op.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)

<div></div>

    mongo::WriteErrorDetail::isErrInfoSet() const

- Used By:

    - [src/mongo/s/write\_ops/batch\_write\_exec.cpp](../../../write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../write\_commands)
