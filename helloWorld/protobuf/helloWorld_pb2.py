# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloWorld.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloWorld.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10helloWorld.proto\"K\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x15\n\rfavorite_nums\x18\x02 \x03(\x05\x12\x1a\n\x12opt_favorite_color\x18\x03 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favorite_nums', full_name='User.favorite_nums', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opt_favorite_color', full_name='User.opt_favorite_color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['User'] = _USER

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'helloWorld_pb2'
  # @@protoc_insertion_point(class_scope:User)
  ))
_sym_db.RegisterMessage(User)


# @@protoc_insertion_point(module_scope)
