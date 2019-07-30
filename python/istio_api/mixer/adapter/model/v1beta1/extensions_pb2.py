# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/adapter/model/v1beta1/extensions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/adapter/model/v1beta1/extensions.proto',
  package='istio.mixer.adapter.model.v1beta1',
  syntax='proto3',
  serialized_options=_b('Z(istio.io/api/mixer/adapter/model/v1beta1'),
  serialized_pb=_b('\n,mixer/adapter/model/v1beta1/extensions.proto\x12!istio.mixer.adapter.model.v1beta1\x1a google/protobuf/descriptor.proto*\xb8\x01\n\x0fTemplateVariety\x12\x1a\n\x16TEMPLATE_VARIETY_CHECK\x10\x00\x12\x1b\n\x17TEMPLATE_VARIETY_REPORT\x10\x01\x12\x1a\n\x16TEMPLATE_VARIETY_QUOTA\x10\x02\x12(\n$TEMPLATE_VARIETY_ATTRIBUTE_GENERATOR\x10\x03\x12&\n\"TEMPLATE_VARIETY_CHECK_WITH_OUTPUT\x10\x04:m\n\x10template_variety\x12\x1c.google.protobuf.FileOptions\x18\xaf\xca\xbc\" \x01(\x0e\x32\x32.istio.mixer.adapter.model.v1beta1.TemplateVariety:6\n\rtemplate_name\x12\x1c.google.protobuf.FileOptions\x18\xd0\xcb\xbc\" \x01(\tB*Z(istio.io/api/mixer/adapter/model/v1beta1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_TEMPLATEVARIETY = _descriptor.EnumDescriptor(
  name='TemplateVariety',
  full_name='istio.mixer.adapter.model.v1beta1.TemplateVariety',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEMPLATE_VARIETY_CHECK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPLATE_VARIETY_REPORT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPLATE_VARIETY_QUOTA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPLATE_VARIETY_ATTRIBUTE_GENERATOR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPLATE_VARIETY_CHECK_WITH_OUTPUT', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=118,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_TEMPLATEVARIETY)

TemplateVariety = enum_type_wrapper.EnumTypeWrapper(_TEMPLATEVARIETY)
TEMPLATE_VARIETY_CHECK = 0
TEMPLATE_VARIETY_REPORT = 1
TEMPLATE_VARIETY_QUOTA = 2
TEMPLATE_VARIETY_ATTRIBUTE_GENERATOR = 3
TEMPLATE_VARIETY_CHECK_WITH_OUTPUT = 4

TEMPLATE_VARIETY_FIELD_NUMBER = 72295727
template_variety = _descriptor.FieldDescriptor(
  name='template_variety', full_name='istio.mixer.adapter.model.v1beta1.template_variety', index=0,
  number=72295727, type=14, cpp_type=8, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
TEMPLATE_NAME_FIELD_NUMBER = 72295888
template_name = _descriptor.FieldDescriptor(
  name='template_name', full_name='istio.mixer.adapter.model.v1beta1.template_name', index=1,
  number=72295888, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.enum_types_by_name['TemplateVariety'] = _TEMPLATEVARIETY
DESCRIPTOR.extensions_by_name['template_variety'] = template_variety
DESCRIPTOR.extensions_by_name['template_name'] = template_name
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

template_variety.enum_type = _TEMPLATEVARIETY
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(template_variety)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(template_name)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
