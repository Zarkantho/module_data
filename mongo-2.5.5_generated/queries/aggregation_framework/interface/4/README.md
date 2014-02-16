
# Interface

### src/mongo/db/pipeline/expression.cpp

<div></div>

    mongo::Expression::ObjectCtx::ObjectCtx(int)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionConstant::parse(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::addDependencies(mongo::DepsTracker*, std::vector<std::string, std::allocator<std::string> >*) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::addOperand(boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionFieldPath::create(std::string const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Expression::parseOperand(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::optimize()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ExpressionAdd

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionCoerceToBool::create(boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ExpressionNary

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::addField(mongo::FieldPath const&, boost::intrusive_ptr<mongo::Expression> const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::ExpressionNary

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::addToDocument(mongo::MutableDocument&, mongo::Document const&, mongo::Variables*) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionConstant::create(mongo::Value const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionNary::serialize(bool) const

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    vtable for mongo::ExpressionAnd

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::includePath(std::string const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Expression::parseObject(mongo::BSONObj, mongo::Expression::ObjectCtx*, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::create()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::ExpressionObject::createRoot()

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)

<div></div>

    mongo::Expression::parseExpression(mongo::BSONElement, mongo::VariablesParseState const&)

- Used By:

    - [src/mongo/dbtests/expressiontests.cpp](../unit\_tests)
