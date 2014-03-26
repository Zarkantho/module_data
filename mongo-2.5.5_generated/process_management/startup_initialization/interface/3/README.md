
# Interface

### src/mongo/util/options\_parser/environment.cpp

<div></div>

    mongo::optionenvironment::Environment::operator[](std::string const&) const

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::Environment::count(std::string const&) const

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongoadmin\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::Environment::validate()

- Used By:

    - [src/mongo/tools/mongodump\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../../../tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongoadmin\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../../../tools)
    - [src/mongo/s/mongos\_options\_init.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../../../tools)
    - [src/mongo/shell/shell\_options\_init.cpp](../../../mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../../../tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../../../tools)

### src/mongo/util/options\_parser/option\_description.cpp

<div></div>

    mongo::optionenvironment::OptionDescription::hidden()

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setDefault(mongo::optionenvironment::Value)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../tools)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::setImplicit(mongo::optionenvironment::Value)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)

<div></div>

    mongo::optionenvironment::OptionDescription::requires(std::string const&)

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)

<div></div>

    mongo::optionenvironment::OptionDescription::format(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::OptionDescription::setSources(mongo::optionenvironment::OptionSources)

- Used By:

    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::incompatibleWith(std::string const&)

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::OptionDescription::validRange(long, long)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::OptionDescription::positional(int, int)

- Used By:

    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

### src/mongo/util/options\_parser/option\_section.cpp

<div></div>

    mongo::optionenvironment::OptionSection::addOptionChaining(std::string const&, std::string const&, mongo::optionenvironment::OptionType, std::string const&)

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongoadmin\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../tools)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::OptionSection::addSection(mongo::optionenvironment::OptionSection const&)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::OptionSection::helpString() const

- Used By:

    - [src/mongo/tools/mongoadmin\_options.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)

### src/mongo/util/options\_parser/startup\_options.cpp

<div></div>

    mongo::optionenvironment::startupOptionsParsed

- Used By:

    - [src/mongo/tools/mongodump\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongooplog\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../../../tools)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/mongod\_options\_init.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../../../tools)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongoadmin\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../../../tools)
    - [src/mongo/s/mongos\_options\_init.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../../../tools)
    - [src/mongo/shell/shell\_options\_init.cpp](../../../mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../../../tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::startupOptions

- Used By:

    - [src/mongo/tools/mongooplog\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/s/mongos\_options\_init.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongodump\_options.cpp](../../../tools)
    - [src/mongo/dbtests/framework\_options\_init.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongodump\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoexport\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongorestore\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongostat\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongoadmin\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/bsondump\_options\_init.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongobridge\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongostat\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoadmin\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options\_init.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongotop\_options.cpp](../../../tools)
    - [src/mongo/tools/mongoimport\_options\_init.cpp](../../../tools)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)
    - [src/mongo/tools/mongofiles\_options.cpp](../../../tools)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/mongooplog\_options.cpp](../../../tools)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/shell/shell\_options\_init.cpp](../../../mongo\_shell)
    - [src/mongo/tools/mongofiles\_options\_init.cpp](../../../tools)

### src/mongo/util/options\_parser/value.cpp

<div></div>

    mongo::optionenvironment::Value::get(std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(double*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::Value::get(std::string*) const

- Used By:

    - [src/mongo/unittest/temp\_dir.cpp](../../../unit\_tests)
    - [src/mongo/util/net/ssl\_options.cpp](../../../ssl)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/shell/shell\_options.cpp](../../../mongo\_shell)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)

<div></div>

    mongo::optionenvironment::Value::get(unsigned int*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(long*) const

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::Value::get(bool*) const

- Used By:

    - [src/mongo/tools/mongoexport\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)

<div></div>

    mongo::optionenvironment::Value::get(unsigned long long*) const

- Used By:

    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)

<div></div>

    mongo::optionenvironment::Value::get(int*) const

- Used By:

    - [src/mongo/tools/tool\_options.cpp](../../../tools)
    - [src/mongo/db/mongod\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/s/mongos\_options.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework\_options.cpp](../../../unit\_tests)
    - [src/mongo/tools/mongobridge\_options.cpp](../../../tools)
