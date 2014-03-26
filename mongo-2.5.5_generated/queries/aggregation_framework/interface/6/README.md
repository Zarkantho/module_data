
# Interface for Dotted Field Utilities
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/pipeline/field\_path.cpp

<div></div>

    mongo::FieldPath::FieldPath(std::string const&)

- Used By:

    - [src/mongo/dbtests/documenttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/pipelinetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/expressiontests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::FieldPath::getPath(bool) const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::FieldPath::FieldPath(std::vector<std::string, std::allocator<std::string> > const&)

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::FieldPath::tail() const

- Used By:

    - [src/mongo/dbtests/pipelinetests.cpp](../../../tests/unit\_tests)
