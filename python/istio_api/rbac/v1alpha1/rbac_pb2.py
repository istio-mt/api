# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rbac/v1alpha1/rbac.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rbac/v1alpha1/rbac.proto',
  package='istio.rbac.v1alpha1',
  syntax='proto3',
  serialized_options=_b('Z\032istio.io/api/rbac/v1alpha1'),
  serialized_pb=_b('\n\x18rbac/v1alpha1/rbac.proto\x12\x13istio.rbac.v1alpha1\"\x84\x01\n\x10WorkloadSelector\x12\x41\n\x06labels\x18\x01 \x03(\x0b\x32\x31.istio.rbac.v1alpha1.WorkloadSelector.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8f\x01\n\x13\x41uthorizationPolicy\x12@\n\x11workload_selector\x18\x01 \x01(\x0b\x32%.istio.rbac.v1alpha1.WorkloadSelector\x12\x36\n\x05\x61llow\x18\x02 \x03(\x0b\x32\'.istio.rbac.v1alpha1.ServiceRoleBinding\"=\n\x0bServiceRole\x12.\n\x05rules\x18\x01 \x03(\x0b\x32\x1f.istio.rbac.v1alpha1.AccessRule\"\x96\x02\n\nAccessRule\x12\x10\n\x08services\x18\x01 \x03(\t\x12\r\n\x05hosts\x18\x05 \x03(\t\x12\x11\n\tnot_hosts\x18\x06 \x03(\t\x12\r\n\x05paths\x18\x02 \x03(\t\x12\x11\n\tnot_paths\x18\x07 \x03(\t\x12\x0f\n\x07methods\x18\x03 \x03(\t\x12\x13\n\x0bnot_methods\x18\x08 \x03(\t\x12\r\n\x05ports\x18\t \x03(\x05\x12\x11\n\tnot_ports\x18\n \x03(\x05\x12?\n\x0b\x63onstraints\x18\x04 \x03(\x0b\x32*.istio.rbac.v1alpha1.AccessRule.Constraint\x1a)\n\nConstraint\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\"\xe7\x01\n\x12ServiceRoleBinding\x12.\n\x08subjects\x18\x01 \x03(\x0b\x32\x1c.istio.rbac.v1alpha1.Subject\x12-\n\x07roleRef\x18\x02 \x01(\x0b\x32\x1c.istio.rbac.v1alpha1.RoleRef\x12\x32\n\x04mode\x18\x03 \x01(\x0e\x32$.istio.rbac.v1alpha1.EnforcementMode\x12\x30\n\x07\x61\x63tions\x18\x04 \x03(\x0b\x32\x1f.istio.rbac.v1alpha1.AccessRule\x12\x0c\n\x04role\x18\x05 \x01(\t\"\xaf\x02\n\x07Subject\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\r\n\x05names\x18\x04 \x03(\t\x12\x11\n\tnot_names\x18\x05 \x03(\t\x12\x11\n\x05group\x18\x02 \x01(\tB\x02\x18\x01\x12\x0e\n\x06groups\x18\x06 \x03(\t\x12\x12\n\nnot_groups\x18\x07 \x03(\t\x12\x12\n\nnamespaces\x18\x08 \x03(\t\x12\x16\n\x0enot_namespaces\x18\t \x03(\t\x12\x0b\n\x03ips\x18\n \x03(\t\x12\x0f\n\x07not_ips\x18\x0b \x03(\t\x12@\n\nproperties\x18\x03 \x03(\x0b\x32,.istio.rbac.v1alpha1.Subject.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x07RoleRef\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xb0\x03\n\nRbacConfig\x12\x32\n\x04mode\x18\x01 \x01(\x0e\x32$.istio.rbac.v1alpha1.RbacConfig.Mode\x12\x39\n\tinclusion\x18\x02 \x01(\x0b\x32&.istio.rbac.v1alpha1.RbacConfig.Target\x12\x39\n\texclusion\x18\x03 \x01(\x0b\x32&.istio.rbac.v1alpha1.RbacConfig.Target\x12>\n\x10\x65nforcement_mode\x18\x04 \x01(\x0e\x32$.istio.rbac.v1alpha1.EnforcementMode\x1aq\n\x06Target\x12\x10\n\x08services\x18\x01 \x03(\t\x12\x41\n\x12workload_selectors\x18\x03 \x03(\x0b\x32%.istio.rbac.v1alpha1.WorkloadSelector\x12\x12\n\nnamespaces\x18\x02 \x03(\t\"E\n\x04Mode\x12\x07\n\x03OFF\x10\x00\x12\x06\n\x02ON\x10\x01\x12\x15\n\x11ON_WITH_INCLUSION\x10\x02\x12\x15\n\x11ON_WITH_EXCLUSION\x10\x03*/\n\x0f\x45nforcementMode\x12\x0c\n\x08\x45NFORCED\x10\x00\x12\x0e\n\nPERMISSIVE\x10\x01\x42\x1cZ\x1aistio.io/api/rbac/v1alpha1b\x06proto3')
)

_ENFORCEMENTMODE = _descriptor.EnumDescriptor(
  name='EnforcementMode',
  full_name='istio.rbac.v1alpha1.EnforcementMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENFORCED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMISSIVE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1688,
  serialized_end=1735,
)
_sym_db.RegisterEnumDescriptor(_ENFORCEMENTMODE)

EnforcementMode = enum_type_wrapper.EnumTypeWrapper(_ENFORCEMENTMODE)
ENFORCED = 0
PERMISSIVE = 1


_RBACCONFIG_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='istio.rbac.v1alpha1.RbacConfig.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_WITH_INCLUSION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ON_WITH_EXCLUSION', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1617,
  serialized_end=1686,
)
_sym_db.RegisterEnumDescriptor(_RBACCONFIG_MODE)


_WORKLOADSELECTOR_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='istio.rbac.v1alpha1.WorkloadSelector.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.rbac.v1alpha1.WorkloadSelector.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.rbac.v1alpha1.WorkloadSelector.LabelsEntry.value', index=1,
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
  serialized_start=137,
  serialized_end=182,
)

_WORKLOADSELECTOR = _descriptor.Descriptor(
  name='WorkloadSelector',
  full_name='istio.rbac.v1alpha1.WorkloadSelector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='labels', full_name='istio.rbac.v1alpha1.WorkloadSelector.labels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WORKLOADSELECTOR_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=182,
)


_AUTHORIZATIONPOLICY = _descriptor.Descriptor(
  name='AuthorizationPolicy',
  full_name='istio.rbac.v1alpha1.AuthorizationPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workload_selector', full_name='istio.rbac.v1alpha1.AuthorizationPolicy.workload_selector', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow', full_name='istio.rbac.v1alpha1.AuthorizationPolicy.allow', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=185,
  serialized_end=328,
)


_SERVICEROLE = _descriptor.Descriptor(
  name='ServiceRole',
  full_name='istio.rbac.v1alpha1.ServiceRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='istio.rbac.v1alpha1.ServiceRole.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=330,
  serialized_end=391,
)


_ACCESSRULE_CONSTRAINT = _descriptor.Descriptor(
  name='Constraint',
  full_name='istio.rbac.v1alpha1.AccessRule.Constraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.rbac.v1alpha1.AccessRule.Constraint.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='istio.rbac.v1alpha1.AccessRule.Constraint.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=631,
  serialized_end=672,
)

_ACCESSRULE = _descriptor.Descriptor(
  name='AccessRule',
  full_name='istio.rbac.v1alpha1.AccessRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='istio.rbac.v1alpha1.AccessRule.services', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hosts', full_name='istio.rbac.v1alpha1.AccessRule.hosts', index=1,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_hosts', full_name='istio.rbac.v1alpha1.AccessRule.not_hosts', index=2,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paths', full_name='istio.rbac.v1alpha1.AccessRule.paths', index=3,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_paths', full_name='istio.rbac.v1alpha1.AccessRule.not_paths', index=4,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='methods', full_name='istio.rbac.v1alpha1.AccessRule.methods', index=5,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_methods', full_name='istio.rbac.v1alpha1.AccessRule.not_methods', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='istio.rbac.v1alpha1.AccessRule.ports', index=7,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_ports', full_name='istio.rbac.v1alpha1.AccessRule.not_ports', index=8,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='istio.rbac.v1alpha1.AccessRule.constraints', index=9,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACCESSRULE_CONSTRAINT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=672,
)


_SERVICEROLEBINDING = _descriptor.Descriptor(
  name='ServiceRoleBinding',
  full_name='istio.rbac.v1alpha1.ServiceRoleBinding',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subjects', full_name='istio.rbac.v1alpha1.ServiceRoleBinding.subjects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roleRef', full_name='istio.rbac.v1alpha1.ServiceRoleBinding.roleRef', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='istio.rbac.v1alpha1.ServiceRoleBinding.mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='istio.rbac.v1alpha1.ServiceRoleBinding.actions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='istio.rbac.v1alpha1.ServiceRoleBinding.role', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=675,
  serialized_end=906,
)


_SUBJECT_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='istio.rbac.v1alpha1.Subject.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='istio.rbac.v1alpha1.Subject.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='istio.rbac.v1alpha1.Subject.PropertiesEntry.value', index=1,
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
  serialized_start=1163,
  serialized_end=1212,
)

_SUBJECT = _descriptor.Descriptor(
  name='Subject',
  full_name='istio.rbac.v1alpha1.Subject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='istio.rbac.v1alpha1.Subject.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='names', full_name='istio.rbac.v1alpha1.Subject.names', index=1,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_names', full_name='istio.rbac.v1alpha1.Subject.not_names', index=2,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='istio.rbac.v1alpha1.Subject.group', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='istio.rbac.v1alpha1.Subject.groups', index=4,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_groups', full_name='istio.rbac.v1alpha1.Subject.not_groups', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='istio.rbac.v1alpha1.Subject.namespaces', index=6,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_namespaces', full_name='istio.rbac.v1alpha1.Subject.not_namespaces', index=7,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ips', full_name='istio.rbac.v1alpha1.Subject.ips', index=8,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='not_ips', full_name='istio.rbac.v1alpha1.Subject.not_ips', index=9,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='istio.rbac.v1alpha1.Subject.properties', index=10,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SUBJECT_PROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=909,
  serialized_end=1212,
)


_ROLEREF = _descriptor.Descriptor(
  name='RoleRef',
  full_name='istio.rbac.v1alpha1.RoleRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='istio.rbac.v1alpha1.RoleRef.kind', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.rbac.v1alpha1.RoleRef.name', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1214,
  serialized_end=1251,
)


_RBACCONFIG_TARGET = _descriptor.Descriptor(
  name='Target',
  full_name='istio.rbac.v1alpha1.RbacConfig.Target',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='istio.rbac.v1alpha1.RbacConfig.Target.services', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workload_selectors', full_name='istio.rbac.v1alpha1.RbacConfig.Target.workload_selectors', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespaces', full_name='istio.rbac.v1alpha1.RbacConfig.Target.namespaces', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1502,
  serialized_end=1615,
)

_RBACCONFIG = _descriptor.Descriptor(
  name='RbacConfig',
  full_name='istio.rbac.v1alpha1.RbacConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='istio.rbac.v1alpha1.RbacConfig.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inclusion', full_name='istio.rbac.v1alpha1.RbacConfig.inclusion', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exclusion', full_name='istio.rbac.v1alpha1.RbacConfig.exclusion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enforcement_mode', full_name='istio.rbac.v1alpha1.RbacConfig.enforcement_mode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RBACCONFIG_TARGET, ],
  enum_types=[
    _RBACCONFIG_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1254,
  serialized_end=1686,
)

_WORKLOADSELECTOR_LABELSENTRY.containing_type = _WORKLOADSELECTOR
_WORKLOADSELECTOR.fields_by_name['labels'].message_type = _WORKLOADSELECTOR_LABELSENTRY
_AUTHORIZATIONPOLICY.fields_by_name['workload_selector'].message_type = _WORKLOADSELECTOR
_AUTHORIZATIONPOLICY.fields_by_name['allow'].message_type = _SERVICEROLEBINDING
_SERVICEROLE.fields_by_name['rules'].message_type = _ACCESSRULE
_ACCESSRULE_CONSTRAINT.containing_type = _ACCESSRULE
_ACCESSRULE.fields_by_name['constraints'].message_type = _ACCESSRULE_CONSTRAINT
_SERVICEROLEBINDING.fields_by_name['subjects'].message_type = _SUBJECT
_SERVICEROLEBINDING.fields_by_name['roleRef'].message_type = _ROLEREF
_SERVICEROLEBINDING.fields_by_name['mode'].enum_type = _ENFORCEMENTMODE
_SERVICEROLEBINDING.fields_by_name['actions'].message_type = _ACCESSRULE
_SUBJECT_PROPERTIESENTRY.containing_type = _SUBJECT
_SUBJECT.fields_by_name['properties'].message_type = _SUBJECT_PROPERTIESENTRY
_RBACCONFIG_TARGET.fields_by_name['workload_selectors'].message_type = _WORKLOADSELECTOR
_RBACCONFIG_TARGET.containing_type = _RBACCONFIG
_RBACCONFIG.fields_by_name['mode'].enum_type = _RBACCONFIG_MODE
_RBACCONFIG.fields_by_name['inclusion'].message_type = _RBACCONFIG_TARGET
_RBACCONFIG.fields_by_name['exclusion'].message_type = _RBACCONFIG_TARGET
_RBACCONFIG.fields_by_name['enforcement_mode'].enum_type = _ENFORCEMENTMODE
_RBACCONFIG_MODE.containing_type = _RBACCONFIG
DESCRIPTOR.message_types_by_name['WorkloadSelector'] = _WORKLOADSELECTOR
DESCRIPTOR.message_types_by_name['AuthorizationPolicy'] = _AUTHORIZATIONPOLICY
DESCRIPTOR.message_types_by_name['ServiceRole'] = _SERVICEROLE
DESCRIPTOR.message_types_by_name['AccessRule'] = _ACCESSRULE
DESCRIPTOR.message_types_by_name['ServiceRoleBinding'] = _SERVICEROLEBINDING
DESCRIPTOR.message_types_by_name['Subject'] = _SUBJECT
DESCRIPTOR.message_types_by_name['RoleRef'] = _ROLEREF
DESCRIPTOR.message_types_by_name['RbacConfig'] = _RBACCONFIG
DESCRIPTOR.enum_types_by_name['EnforcementMode'] = _ENFORCEMENTMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkloadSelector = _reflection.GeneratedProtocolMessageType('WorkloadSelector', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _WORKLOADSELECTOR_LABELSENTRY,
    __module__ = 'rbac.v1alpha1.rbac_pb2'
    # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.WorkloadSelector.LabelsEntry)
    ))
  ,
  DESCRIPTOR = _WORKLOADSELECTOR,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.WorkloadSelector)
  ))
_sym_db.RegisterMessage(WorkloadSelector)
_sym_db.RegisterMessage(WorkloadSelector.LabelsEntry)

AuthorizationPolicy = _reflection.GeneratedProtocolMessageType('AuthorizationPolicy', (_message.Message,), dict(
  DESCRIPTOR = _AUTHORIZATIONPOLICY,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.AuthorizationPolicy)
  ))
_sym_db.RegisterMessage(AuthorizationPolicy)

ServiceRole = _reflection.GeneratedProtocolMessageType('ServiceRole', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEROLE,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.ServiceRole)
  ))
_sym_db.RegisterMessage(ServiceRole)

AccessRule = _reflection.GeneratedProtocolMessageType('AccessRule', (_message.Message,), dict(

  Constraint = _reflection.GeneratedProtocolMessageType('Constraint', (_message.Message,), dict(
    DESCRIPTOR = _ACCESSRULE_CONSTRAINT,
    __module__ = 'rbac.v1alpha1.rbac_pb2'
    # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.AccessRule.Constraint)
    ))
  ,
  DESCRIPTOR = _ACCESSRULE,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.AccessRule)
  ))
_sym_db.RegisterMessage(AccessRule)
_sym_db.RegisterMessage(AccessRule.Constraint)

ServiceRoleBinding = _reflection.GeneratedProtocolMessageType('ServiceRoleBinding', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEROLEBINDING,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.ServiceRoleBinding)
  ))
_sym_db.RegisterMessage(ServiceRoleBinding)

Subject = _reflection.GeneratedProtocolMessageType('Subject', (_message.Message,), dict(

  PropertiesEntry = _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), dict(
    DESCRIPTOR = _SUBJECT_PROPERTIESENTRY,
    __module__ = 'rbac.v1alpha1.rbac_pb2'
    # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.Subject.PropertiesEntry)
    ))
  ,
  DESCRIPTOR = _SUBJECT,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.Subject)
  ))
_sym_db.RegisterMessage(Subject)
_sym_db.RegisterMessage(Subject.PropertiesEntry)

RoleRef = _reflection.GeneratedProtocolMessageType('RoleRef', (_message.Message,), dict(
  DESCRIPTOR = _ROLEREF,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.RoleRef)
  ))
_sym_db.RegisterMessage(RoleRef)

RbacConfig = _reflection.GeneratedProtocolMessageType('RbacConfig', (_message.Message,), dict(

  Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), dict(
    DESCRIPTOR = _RBACCONFIG_TARGET,
    __module__ = 'rbac.v1alpha1.rbac_pb2'
    # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.RbacConfig.Target)
    ))
  ,
  DESCRIPTOR = _RBACCONFIG,
  __module__ = 'rbac.v1alpha1.rbac_pb2'
  # @@protoc_insertion_point(class_scope:istio.rbac.v1alpha1.RbacConfig)
  ))
_sym_db.RegisterMessage(RbacConfig)
_sym_db.RegisterMessage(RbacConfig.Target)


DESCRIPTOR._options = None
_WORKLOADSELECTOR_LABELSENTRY._options = None
_SUBJECT_PROPERTIESENTRY._options = None
_SUBJECT.fields_by_name['group']._options = None
# @@protoc_insertion_point(module_scope)
