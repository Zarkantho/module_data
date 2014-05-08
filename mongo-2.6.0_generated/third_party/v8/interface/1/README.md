
# Interface for V8 Javascript Engine
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/third\_party/v8/src/api.cc

<div></div>

    v8::Message::GetSourceLine() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Set(unsigned int, v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::False()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::True()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Array::CloneElementAt(unsigned int)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::ThrowException(v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToString() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::DisposeGlobal(v8::internal::Object**)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IntegerValue() const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Message::GetEndPosition() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::GetHiddenValue(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::HandleScope::~HandleScope()

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Boolean::Value() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::InstanceTemplate()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::BooleanValue() const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Date::New(double)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::CanContinue() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetTotalTime() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Delete(unsigned int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::HasOwnProperty(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfile::GetTopDownRoot() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Function::Call(v8::Handle<v8::Object>, int, v8::Handle<v8::Value>*)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Array::New(int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::IgnoreOutOfMemoryException()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Isolate::Exit()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::IsExecutionTerminating(v8::Isolate*)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::GetRealNamedProperty(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Set(v8::Handle<v8::Value>, v8::Handle<v8::Value>, v8::PropertyAttribute)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::ObjectTemplate::SetNamedPropertyHandler(v8::Handle<v8::Value> (*)(v8::Local<v8::String>, v8::AccessorInfo const&), v8::Handle<v8::Value> (*)(v8::Local<v8::String>, v8::Local<v8::Value>, v8::AccessorInfo const&), v8::Handle<v8::Integer> (*)(v8::Local<v8::String>, v8::AccessorInfo const&), v8::Handle<v8::Boolean> (*)(v8::Local<v8::String>, v8::AccessorInfo const&), v8::Handle<v8::Array> (*)(v8::AccessorInfo const&), v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::CheckedGetInternalField(int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsExternal() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Get(unsigned int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::HeapStatistics::HeapStatistics()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Array::Length() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::Exception() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Context::Exit()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Message::GetStartColumn() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Message::GetScriptResourceName() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetScriptResourceName() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Message::GetEndColumn() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::GetVersion()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::LowMemoryNotification()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsFunction() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Script::Compile(v8::Handle<v8::String>, v8::Handle<v8::Value>, v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Context::Global()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::GetOwnPropertyNames()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::GetPrototype()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::Inherit(v8::Handle<v8::FunctionTemplate>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::String::Utf8Length() const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::Uint32Value() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Integer::Value() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::AddGCPrologueCallback(void (*)(v8::GCType, v8::GCCallbackFlags), v8::GCType)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::ForceSet(v8::Handle<v8::Value>, v8::Handle<v8::Value>, v8::PropertyAttribute)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Context::New(v8::ExtensionConfiguration*, v8::Handle<v8::ObjectTemplate>, v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetFunctionName() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Function::NewInstance() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetChildrenCount() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::String::New(char const*, int)

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Isolate::Dispose()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Has(unsigned int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfiler::StopProfiling(v8::Handle<v8::String>, v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetChild(int) const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::GetHeapStatistics(v8::HeapStatistics*)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::SetClassName(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsObject() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Template::Set(v8::Handle<v8::String>, v8::Handle<v8::Data>, v8::PropertyAttribute)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::String::Utf8Value::~Utf8Value()

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsRegExp() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Number::Value() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::New()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::GetPropertyNames()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Integer::New(int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Get(v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Date::NumberValue() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::AddGCEpilogueCallback(void (*)(v8::GCType, v8::GCCallbackFlags), v8::GCType)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::TerminateExecution(v8::Isolate*)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Exception::Error(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsBoolean() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::TryCatch()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::GlobalizeReference(v8::internal::Object**)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToInteger() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::HasInstance(v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::HandleScope::CreateHandle(v8::internal::Object*)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToObject() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToNumber() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::New(v8::Handle<v8::Value> (*)(v8::Arguments const&), v8::Handle<v8::Value>, v8::Handle<v8::Signature>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::~TryCatch()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToUint32() const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Has(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Int32::Value() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToBoolean() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::HandleScope::HandleScope()

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::MakeWeak(v8::internal::Object**, void*, void (*)(v8::Persistent<v8::Value>, void*))

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::V8::AdjustAmountOfExternalAllocatedMemory(long)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::ToInt32() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::ObjectTemplate::SetInternalFieldCount(int)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsArray() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Function::SetName(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::GetFunction()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Context::HasOutOfMemoryException()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Message::GetLineNumber() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetLineNumber() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::ObjectTemplate::SetIndexedPropertyHandler(v8::Handle<v8::Value> (*)(unsigned int, v8::AccessorInfo const&), v8::Handle<v8::Value> (*)(unsigned int, v8::Local<v8::Value>, v8::AccessorInfo const&), v8::Handle<v8::Integer> (*)(unsigned int, v8::AccessorInfo const&), v8::Handle<v8::Boolean> (*)(unsigned int, v8::AccessorInfo const&), v8::Handle<v8::Array> (*)(v8::AccessorInfo const&), v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfileNode::GetSelfTime() const

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Isolate::Enter()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::External::New(void*)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Function::NewInstance(int, v8::Handle<v8::Value>*) const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::Message() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::External::Value() const

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Number::New(double)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::HasCaught() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Message::GetStartPosition() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsDate() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::FunctionTemplate::PrototypeTemplate()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::ObjectTemplate::SetCallAsFunctionHandler(v8::Handle<v8::Value> (*)(v8::Arguments const&), v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::HasRealNamedProperty(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Isolate::New()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Null()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::SetInternalField(int, v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Script::Run()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::CpuProfiler::StartProfiling(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::Int32Value() const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::TryCatch::ReThrow()

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::Delete(v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Script::New(v8::Handle<v8::String>, v8::ScriptOrigin*, v8::ScriptData*, v8::Handle<v8::String>)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Context::Enter()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::NumberValue() const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::String::Utf8Value::Utf8Value(v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/v8\_profiler.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::String::WriteAscii(char*, int, int, int) const

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::InternalFieldCount()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::StrictEquals(v8::Handle<v8::Value>) const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::HandleScope::RawClose(v8::internal::Object**)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Value::IsNumber() const

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Undefined()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Object::SetHiddenValue(v8::Handle<v8::String>, v8::Handle<v8::Value>)

- Used By:

    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

### src/third\_party/v8/src/v8threads.cc

<div></div>

    v8::Locker::Locker(v8::Isolate*)

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    v8::Locker::~Locker()

- Used By:

    - [src/mongo/scripting/engine\_v8.cpp](../../../../javascript/javascript\_libraries)
    - [src/mongo/scripting/v8\_utils.cpp](../../../../javascript/javascript\_libraries)
