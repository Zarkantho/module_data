# Process Management

Process management code.  Handles shutdown, startup, and configuration of a MongoDB process

## Modules

### [Build Information](build\_information)
Information about this server build, including server version, compile information, and javascript version.  Some files are automatically generated as part of the build process

### [Logging System](logging\_system)
System for managing log output from the server.  Currently this is also shared by the tools since the tools share much of the server code.

### [Mongod And Mongos Command Line Options](mongod\_and\_mongos\_command\_line\_options)
Command line options for mongod and mongos that are not connected to a specific module.

### [Mongos And Mongod Mains](mongos\_and\_mongod\_mains)
Main functions for the mongos and mongod binaries

### [Startup Initialization](startup\_initialization)
TODO: startup\_initialization description

