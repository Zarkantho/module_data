# BSON

MongoDB BSON support

## Modules

### [BSON](bson)
This is the core class for managing BSON objects.  Mutable BSON and other in memory BSON management methods in the server are all built on this library

### [Mutable BSON](mutable\_bson)
Mutable BSON is built on top of the BSON library, and provides an interface for logically a BSON object.  It lazily unpacks a BSON object into a vector of elements as changes are made, and can reserialize into a new BSON object with all the changes.

