# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/v1/config/client/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/v1/config/client/service.proto',
  package='istio.mixer.v1.config.client',
  syntax='proto3',
  serialized_options=_b('Z#istio.io/api/mixer/v1/config/client\310\341\036\000\250\342\036\000\360\341\036\000\330\342\036\001'),
  serialized_pb=_b('\n$mixer/v1/config/client/service.proto\x12\x1cistio.mixer.v1.config.client\x1a\x14gogoproto/gogo.proto\"\xc7\x01\n\x0cIstioService\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x0f\n\x07service\x18\x04 \x01(\t\x12\x46\n\x06labels\x18\x05 \x03(\x0b\x32\x36.istio.mixer.v1.config.client.IstioService.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x35Z#istio.io/api/mixer/v1/config/client\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\xf0\xe1\x1e\x00\xd8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_ISTIOSERVICE_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='istio.mixer.v1.config.client.IstioService.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.mixer.v1.config.client.IstioService.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.mixer.v1.config.client.IstioService.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=292,
)

_ISTIOSERVICE = _descriptor.Descriptor(
  name='IstioService',
  full_name='istio.mixer.v1.config.client.IstioService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.mixer.v1.config.client.IstioService.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='istio.mixer.v1.config.client.IstioService.namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='istio.mixer.v1.config.client.IstioService.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='istio.mixer.v1.config.client.IstioService.service', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='istio.mixer.v1.config.client.IstioService.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ISTIOSERVICE_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=292,
)

_ISTIOSERVICE_LABELSENTRY.containing_type = _ISTIOSERVICE
_ISTIOSERVICE.fields_by_name['labels'].message_type = _ISTIOSERVICE_LABELSENTRY
DESCRIPTOR.message_types_by_name['IstioService'] = _ISTIOSERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IstioService = _reflection.GeneratedProtocolMessageType('IstioService', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ISTIOSERVICE_LABELSENTRY,
    __module__ = 'mixer.v1.config.client.service_pb2'
    # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.IstioService.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _ISTIOSERVICE,
  __module__ = 'mixer.v1.config.client.service_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.v1.config.client.IstioService)
  ))
_sym_db.RegisterMessage(IstioService)
_sym_db.RegisterMessage(IstioService.LabelsEntry)


DESCRIPTOR._options = None
_ISTIOSERVICE_LABELSENTRY._options = None
# @@protoc_insertion_point(module_scope)
