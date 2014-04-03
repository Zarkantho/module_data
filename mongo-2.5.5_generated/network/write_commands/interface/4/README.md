
# Interface for Config Coordinator
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/write\_ops/config\_coordinator.cpp

<div></div>

    mongo::ConfigCoordinator::executeBatch(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*, bool)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)

<div></div>

    mongo::ConfigCoordinator::ConfigCoordinator(mongo::MultiCommandDispatch*, std::vector<mongo::ConnectionString, std::allocator<mongo::ConnectionString> > const&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/sharding\_uncategorized)
