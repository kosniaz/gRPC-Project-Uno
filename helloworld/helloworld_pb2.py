# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"(\n\x11HelloWorldRequest\x12\x13\n\x0btime_of_day\x18\x01 \x01(\t\"&\n\x12HelloWorldResponse\x12\x10\n\x08greeting\x18\x01 \x01(\t2`\n\nHelloWorld\x12R\n\x0frequestGreeting\x12\x1d.helloworld.HelloWorldRequest\x1a\x1e.helloworld.HelloWorldResponse\"\x00\x62\x06proto3')



_HELLOWORLDREQUEST = DESCRIPTOR.message_types_by_name['HelloWorldRequest']
_HELLOWORLDRESPONSE = DESCRIPTOR.message_types_by_name['HelloWorldResponse']
HelloWorldRequest = _reflection.GeneratedProtocolMessageType('HelloWorldRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloWorldRequest)
  })
_sym_db.RegisterMessage(HelloWorldRequest)

HelloWorldResponse = _reflection.GeneratedProtocolMessageType('HelloWorldResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDRESPONSE,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloWorldResponse)
  })
_sym_db.RegisterMessage(HelloWorldResponse)

_HELLOWORLD = DESCRIPTOR.services_by_name['HelloWorld']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOWORLDREQUEST._serialized_start=32
  _HELLOWORLDREQUEST._serialized_end=72
  _HELLOWORLDRESPONSE._serialized_start=74
  _HELLOWORLDRESPONSE._serialized_end=112
  _HELLOWORLD._serialized_start=114
  _HELLOWORLD._serialized_end=210
# @@protoc_insertion_point(module_scope)
