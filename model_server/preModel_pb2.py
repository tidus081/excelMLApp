# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preModel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='preModel.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0epreModel.proto\"r\n\x08gRequest\x12\x0b\n\x03src\x18\x01 \x01(\t\x12\r\n\x05pname\x18\x02 \x01(\t\x12\r\n\x05sname\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\t\x12\x0c\n\x04real\x18\x06 \x01(\t\x12\x11\n\textension\x18\x07 \x01(\t\"\x19\n\x06gReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\tfileReply\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x32\xb7\x02\n\x07Greeter\x12!\n\tpass_data\x12\t.gRequest\x1a\x07.gReply\"\x00\x12(\n\rupload_object\x12\n.fileReply\x1a\x07.gReply\"\x00(\x01\x12)\n\x0c\x64ownload_csv\x12\t.gRequest\x1a\n.fileReply\"\x00\x30\x01\x12,\n\x0f\x64ownload_object\x12\t.gRequest\x1a\n.fileReply\"\x00\x30\x01\x12#\n\x0b\x62uild_model\x12\t.gRequest\x1a\x07.gReply\"\x00\x12\x1f\n\x07predict\x12\t.gRequest\x1a\x07.gReply\"\x00\x12\x1f\n\x07\x61nomaly\x12\t.gRequest\x1a\x07.gReply\"\x00\x12\x1f\n\tvectorize\x12\x07.gReply\x1a\x07.gReply\"\x00\x62\x06proto3')
)




_GREQUEST = _descriptor.Descriptor(
  name='gRequest',
  full_name='gRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='gRequest.src', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pname', full_name='gRequest.pname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sname', full_name='gRequest.sname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='gRequest.user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='gRequest.data', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='real', full_name='gRequest.real', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='gRequest.extension', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=132,
)


_GREPLY = _descriptor.Descriptor(
  name='gReply',
  full_name='gReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='gReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=159,
)


_FILEREPLY = _descriptor.Descriptor(
  name='fileReply',
  full_name='fileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='fileReply.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=188,
)

DESCRIPTOR.message_types_by_name['gRequest'] = _GREQUEST
DESCRIPTOR.message_types_by_name['gReply'] = _GREPLY
DESCRIPTOR.message_types_by_name['fileReply'] = _FILEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

gRequest = _reflection.GeneratedProtocolMessageType('gRequest', (_message.Message,), dict(
  DESCRIPTOR = _GREQUEST,
  __module__ = 'preModel_pb2'
  # @@protoc_insertion_point(class_scope:gRequest)
  ))
_sym_db.RegisterMessage(gRequest)

gReply = _reflection.GeneratedProtocolMessageType('gReply', (_message.Message,), dict(
  DESCRIPTOR = _GREPLY,
  __module__ = 'preModel_pb2'
  # @@protoc_insertion_point(class_scope:gReply)
  ))
_sym_db.RegisterMessage(gReply)

fileReply = _reflection.GeneratedProtocolMessageType('fileReply', (_message.Message,), dict(
  DESCRIPTOR = _FILEREPLY,
  __module__ = 'preModel_pb2'
  # @@protoc_insertion_point(class_scope:fileReply)
  ))
_sym_db.RegisterMessage(fileReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=191,
  serialized_end=502,
  methods=[
  _descriptor.MethodDescriptor(
    name='pass_data',
    full_name='Greeter.pass_data',
    index=0,
    containing_service=None,
    input_type=_GREQUEST,
    output_type=_GREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='upload_object',
    full_name='Greeter.upload_object',
    index=1,
    containing_service=None,
    input_type=_FILEREPLY,
    output_type=_GREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='download_csv',
    full_name='Greeter.download_csv',
    index=2,
    containing_service=None,
    input_type=_GREQUEST,
    output_type=_FILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='download_object',
    full_name='Greeter.download_object',
    index=3,
    containing_service=None,
    input_type=_GREQUEST,
    output_type=_FILEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='build_model',
    full_name='Greeter.build_model',
    index=4,
    containing_service=None,
    input_type=_GREQUEST,
    output_type=_GREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='predict',
    full_name='Greeter.predict',
    index=5,
    containing_service=None,
    input_type=_GREQUEST,
    output_type=_GREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='anomaly',
    full_name='Greeter.anomaly',
    index=6,
    containing_service=None,
    input_type=_GREQUEST,
    output_type=_GREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='vectorize',
    full_name='Greeter.vectorize',
    index=7,
    containing_service=None,
    input_type=_GREPLY,
    output_type=_GREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)