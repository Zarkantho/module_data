
# Interface for Options Parser
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/options\_parser/environment.cpp

<div></div>

    mongo::optionenvironment::Environment::toBSON() const

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Environment::set(std::string const&, mongo::optionenvironment::Value const&)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::optionenvironment::Environment::validate(bool)

- Used By:

    - [src/mongo/tools/mongoexport\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/s/mongos\_options\_init.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/shell\_options\_init.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::optionenvironment::Environment::get(std::string const&, mongo::optionenvironment::Value*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Environment::remove(std::string const&)

- Used By:

    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

### src/mongo/util/options\_parser/option\_description.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::OptionDescription::validRange(long, long)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::composing()

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Used By:

    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Used By:

    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::incompatibleWith(std::string const&)

- Used By:

    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::requires(std::string const&)

- Used By:

    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Used By:

    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)

- Used By:

    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

### src/mongo/util/options\_parser/option\_section.cpp

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)

- Used By:

    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

### src/mongo/util/options\_parser/startup\_options.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Used By:

    - [src/mongo/tools/mongostat\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options\_init.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/shell\_options\_init.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::optionenvironment::startupOptions

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../../tools/tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/mongos\_options\_init.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)
    - [src/mongo/tools/mongotop\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options\_init.cpp](../../../../mongo\_shell/mongo\_shell)

### src/mongo/util/options\_parser/value.cpp

<div></div>

    mongo::optionenvironment::Value::get(unsigned int*) const

- Used By:

    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Value::get(long*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Value::get(std::map<std::string, std::string, std::less<std::string>, std::allocator<std::pair<std::string const, std::string> > >*) const

- Used By:

    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Value::get(double*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Used By:

    - [src/mongo/tools/mongobridge\_options.cpp](../../../../tools/tools)
    - [src/mongo/tools/tool\_options.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/util/net/ssl\_options.cpp](../../../../network/ssl)
    - [src/mongo/unittest/temp\_dir.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Used By:

    - [src/mongo/tools/mongoexport\_options.cpp](../../../../tools/tools)
    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/mongod\_options.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)
    - [src/mongo/db/server\_options\_helpers.cpp](../../../../process\_management/mongod\_and\_mongos\_command\_line\_options)

<div></div>

    mongo::optionenvironment::Value::get(std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../../../../mongo\_shell/mongo\_shell)

<div></div>

    mongo::optionenvironment::Value::get(unsigned long long*) const

- Used By:

    - [src/mongo/dbtests/framework\_options.cpp](../../../../tests/unit\_tests)
