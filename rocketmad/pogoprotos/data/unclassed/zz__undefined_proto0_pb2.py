# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/unclassed/zz__undefined_proto0.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/unclassed/zz__undefined_proto0.proto',
  package='pogoprotos.data.unclassed',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/data/unclassed/zz__undefined_proto0.proto\x12\x19pogoprotos.data.unclassed\"\xb5\x01\n\x12ZZ_UndefinedProto0\x12I\n\x06result\x18\x01 \x01(\x0e\x32\x39.pogoprotos.data.unclassed.ZZ_UndefinedProto0.ZZ_0_Result\"T\n\x0bZZ_0_Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1a\n\x16\x45RROR_PLAYER_NOT_FOUND\x10\x03\x62\x06proto3')
)



_ZZ_UNDEFINEDPROTO0_ZZ_0_RESULT = _descriptor.EnumDescriptor(
  name='ZZ_0_Result',
  full_name='pogoprotos.data.unclassed.ZZ_UndefinedProto0.ZZ_0_Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=181,
  serialized_end=265,
)
_sym_db.RegisterEnumDescriptor(_ZZ_UNDEFINEDPROTO0_ZZ_0_RESULT)


_ZZ_UNDEFINEDPROTO0 = _descriptor.Descriptor(
  name='ZZ_UndefinedProto0',
  full_name='pogoprotos.data.unclassed.ZZ_UndefinedProto0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.unclassed.ZZ_UndefinedProto0.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ZZ_UNDEFINEDPROTO0_ZZ_0_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=265,
)

_ZZ_UNDEFINEDPROTO0.fields_by_name['result'].enum_type = _ZZ_UNDEFINEDPROTO0_ZZ_0_RESULT
_ZZ_UNDEFINEDPROTO0_ZZ_0_RESULT.containing_type = _ZZ_UNDEFINEDPROTO0
DESCRIPTOR.message_types_by_name['ZZ_UndefinedProto0'] = _ZZ_UNDEFINEDPROTO0
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZZ_UndefinedProto0 = _reflection.GeneratedProtocolMessageType('ZZ_UndefinedProto0', (_message.Message,), dict(
  DESCRIPTOR = _ZZ_UNDEFINEDPROTO0,
  __module__ = 'pogoprotos.data.unclassed.zz__undefined_proto0_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.unclassed.ZZ_UndefinedProto0)
  ))
_sym_db.RegisterMessage(ZZ_UndefinedProto0)


# @@protoc_insertion_point(module_scope)