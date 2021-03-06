# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_debug_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import get_updates_caller_info_pb2
import sync_enums_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_debug_info.proto',
  package='sync_pb',
  serialized_pb='\n\x17\x63lient_debug_info.proto\x12\x07sync_pb\x1a\x1dget_updates_caller_info.proto\x1a\x10sync_enums.proto\"8\n\x08TypeHint\x12\x14\n\x0c\x64\x61ta_type_id\x18\x01 \x01(\x05\x12\x16\n\x0ehas_valid_hint\x18\x02 \x01(\x08\"r\n\nSourceInfo\x12>\n\x06source\x18\x01 \x01(\x0e\x32..sync_pb.GetUpdatesCallerInfo.GetUpdatesSource\x12$\n\ttype_hint\x18\x02 \x03(\x0b\x32\x11.sync_pb.TypeHint\"\x90\x03\n\x1bSyncCycleCompletedEventInfo\x12\"\n\x16num_blocking_conflicts\x18\x02 \x01(\x05\x42\x02\x18\x01\x12&\n\x1anum_non_blocking_conflicts\x18\x03 \x01(\x05\x42\x02\x18\x01\x12 \n\x18num_encryption_conflicts\x18\x04 \x01(\x05\x12\x1f\n\x17num_hierarchy_conflicts\x18\x05 \x01(\x05\x12\x1c\n\x14num_simple_conflicts\x18\x06 \x01(\x05\x12\x1c\n\x14num_server_conflicts\x18\x07 \x01(\x05\x12\x1e\n\x16num_updates_downloaded\x18\x08 \x01(\x05\x12(\n num_reflected_updates_downloaded\x18\t \x01(\x05\x12\x32\n\x0b\x63\x61ller_info\x18\n \x01(\x0b\x32\x1d.sync_pb.GetUpdatesCallerInfo\x12(\n\x0bsource_info\x18\x0b \x03(\x0b\x32\x13.sync_pb.SourceInfo\"\x97\x06\n\x18\x44\x61tatypeAssociationStats\x12\x14\n\x0c\x64\x61ta_type_id\x18\x01 \x01(\x05\x12*\n\"num_local_items_before_association\x18\x02 \x01(\x05\x12)\n!num_sync_items_before_association\x18\x03 \x01(\x05\x12)\n!num_local_items_after_association\x18\x04 \x01(\x05\x12(\n num_sync_items_after_association\x18\x05 \x01(\x05\x12\x1d\n\x15num_local_items_added\x18\x06 \x01(\x05\x12\x1f\n\x17num_local_items_deleted\x18\x07 \x01(\x05\x12 \n\x18num_local_items_modified\x18\x08 \x01(\x05\x12\x1c\n\x14num_sync_items_added\x18\t \x01(\x05\x12\x1e\n\x16num_sync_items_deleted\x18\n \x01(\x05\x12\x1f\n\x17num_sync_items_modified\x18\x0b \x01(\x05\x12%\n\x1dlocal_version_pre_association\x18\x14 \x01(\x03\x12$\n\x1csync_version_pre_association\x18\x15 \x01(\x03\x12\x11\n\thad_error\x18\x0c \x01(\x08\x12\x1d\n\x15\x64ownload_wait_time_us\x18\x0f \x01(\x03\x12\x18\n\x10\x64ownload_time_us\x18\r \x01(\x03\x12\x32\n*association_wait_time_for_high_priority_us\x18\x10 \x01(\x03\x12\x32\n*association_wait_time_for_same_priority_us\x18\x0e \x01(\x03\x12\x1b\n\x13\x61ssociation_time_us\x18\x11 \x01(\x03\x12,\n$high_priority_type_configured_before\x18\x12 \x03(\x05\x12,\n$same_priority_type_configured_before\x18\x13 \x03(\x05\"\xad\x02\n\x0e\x44\x65\x62ugEventInfo\x12\x43\n\x0fsingleton_event\x18\x01 \x01(\x0e\x32*.sync_pb.SyncEnums.SingletonDebugEventType\x12M\n\x1fsync_cycle_completed_event_info\x18\x02 \x01(\x0b\x32$.sync_pb.SyncCycleCompletedEventInfo\x12\x18\n\x10nudging_datatype\x18\x03 \x01(\x05\x12&\n\x1e\x64\x61tatypes_notified_from_server\x18\x04 \x03(\x05\x12\x45\n\x1a\x64\x61tatype_association_stats\x18\x05 \x01(\x0b\x32!.sync_pb.DatatypeAssociationStats\"\x91\x01\n\tDebugInfo\x12\'\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x17.sync_pb.DebugEventInfo\x12\x1b\n\x13\x63ryptographer_ready\x18\x02 \x01(\x08\x12&\n\x1e\x63ryptographer_has_pending_keys\x18\x03 \x01(\x08\x12\x16\n\x0e\x65vents_dropped\x18\x04 \x01(\x08\x42\x04H\x03`\x01')




_TYPEHINT = _descriptor.Descriptor(
  name='TypeHint',
  full_name='sync_pb.TypeHint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_type_id', full_name='sync_pb.TypeHint.data_type_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_valid_hint', full_name='sync_pb.TypeHint.has_valid_hint', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  serialized_start=85,
  serialized_end=141,
)


_SOURCEINFO = _descriptor.Descriptor(
  name='SourceInfo',
  full_name='sync_pb.SourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='sync_pb.SourceInfo.source', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_hint', full_name='sync_pb.SourceInfo.type_hint', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=143,
  serialized_end=257,
)


_SYNCCYCLECOMPLETEDEVENTINFO = _descriptor.Descriptor(
  name='SyncCycleCompletedEventInfo',
  full_name='sync_pb.SyncCycleCompletedEventInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_blocking_conflicts', full_name='sync_pb.SyncCycleCompletedEventInfo.num_blocking_conflicts', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
    _descriptor.FieldDescriptor(
      name='num_non_blocking_conflicts', full_name='sync_pb.SyncCycleCompletedEventInfo.num_non_blocking_conflicts', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')),
    _descriptor.FieldDescriptor(
      name='num_encryption_conflicts', full_name='sync_pb.SyncCycleCompletedEventInfo.num_encryption_conflicts', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_hierarchy_conflicts', full_name='sync_pb.SyncCycleCompletedEventInfo.num_hierarchy_conflicts', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_simple_conflicts', full_name='sync_pb.SyncCycleCompletedEventInfo.num_simple_conflicts', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_server_conflicts', full_name='sync_pb.SyncCycleCompletedEventInfo.num_server_conflicts', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_updates_downloaded', full_name='sync_pb.SyncCycleCompletedEventInfo.num_updates_downloaded', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_reflected_updates_downloaded', full_name='sync_pb.SyncCycleCompletedEventInfo.num_reflected_updates_downloaded', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller_info', full_name='sync_pb.SyncCycleCompletedEventInfo.caller_info', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_info', full_name='sync_pb.SyncCycleCompletedEventInfo.source_info', index=9,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=260,
  serialized_end=660,
)


_DATATYPEASSOCIATIONSTATS = _descriptor.Descriptor(
  name='DatatypeAssociationStats',
  full_name='sync_pb.DatatypeAssociationStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_type_id', full_name='sync_pb.DatatypeAssociationStats.data_type_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_local_items_before_association', full_name='sync_pb.DatatypeAssociationStats.num_local_items_before_association', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_sync_items_before_association', full_name='sync_pb.DatatypeAssociationStats.num_sync_items_before_association', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_local_items_after_association', full_name='sync_pb.DatatypeAssociationStats.num_local_items_after_association', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_sync_items_after_association', full_name='sync_pb.DatatypeAssociationStats.num_sync_items_after_association', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_local_items_added', full_name='sync_pb.DatatypeAssociationStats.num_local_items_added', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_local_items_deleted', full_name='sync_pb.DatatypeAssociationStats.num_local_items_deleted', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_local_items_modified', full_name='sync_pb.DatatypeAssociationStats.num_local_items_modified', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_sync_items_added', full_name='sync_pb.DatatypeAssociationStats.num_sync_items_added', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_sync_items_deleted', full_name='sync_pb.DatatypeAssociationStats.num_sync_items_deleted', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_sync_items_modified', full_name='sync_pb.DatatypeAssociationStats.num_sync_items_modified', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_version_pre_association', full_name='sync_pb.DatatypeAssociationStats.local_version_pre_association', index=11,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_version_pre_association', full_name='sync_pb.DatatypeAssociationStats.sync_version_pre_association', index=12,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='had_error', full_name='sync_pb.DatatypeAssociationStats.had_error', index=13,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='download_wait_time_us', full_name='sync_pb.DatatypeAssociationStats.download_wait_time_us', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='download_time_us', full_name='sync_pb.DatatypeAssociationStats.download_time_us', index=15,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='association_wait_time_for_high_priority_us', full_name='sync_pb.DatatypeAssociationStats.association_wait_time_for_high_priority_us', index=16,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='association_wait_time_for_same_priority_us', full_name='sync_pb.DatatypeAssociationStats.association_wait_time_for_same_priority_us', index=17,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='association_time_us', full_name='sync_pb.DatatypeAssociationStats.association_time_us', index=18,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_priority_type_configured_before', full_name='sync_pb.DatatypeAssociationStats.high_priority_type_configured_before', index=19,
      number=18, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='same_priority_type_configured_before', full_name='sync_pb.DatatypeAssociationStats.same_priority_type_configured_before', index=20,
      number=19, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=663,
  serialized_end=1454,
)


_DEBUGEVENTINFO = _descriptor.Descriptor(
  name='DebugEventInfo',
  full_name='sync_pb.DebugEventInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='singleton_event', full_name='sync_pb.DebugEventInfo.singleton_event', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_cycle_completed_event_info', full_name='sync_pb.DebugEventInfo.sync_cycle_completed_event_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nudging_datatype', full_name='sync_pb.DebugEventInfo.nudging_datatype', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datatypes_notified_from_server', full_name='sync_pb.DebugEventInfo.datatypes_notified_from_server', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datatype_association_stats', full_name='sync_pb.DebugEventInfo.datatype_association_stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=1457,
  serialized_end=1758,
)


_DEBUGINFO = _descriptor.Descriptor(
  name='DebugInfo',
  full_name='sync_pb.DebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='sync_pb.DebugInfo.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cryptographer_ready', full_name='sync_pb.DebugInfo.cryptographer_ready', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cryptographer_has_pending_keys', full_name='sync_pb.DebugInfo.cryptographer_has_pending_keys', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='events_dropped', full_name='sync_pb.DebugInfo.events_dropped', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  extension_ranges=[],
  serialized_start=1761,
  serialized_end=1906,
)

_SOURCEINFO.fields_by_name['source'].enum_type = get_updates_caller_info_pb2._GETUPDATESCALLERINFO_GETUPDATESSOURCE
_SOURCEINFO.fields_by_name['type_hint'].message_type = _TYPEHINT
_SYNCCYCLECOMPLETEDEVENTINFO.fields_by_name['caller_info'].message_type = get_updates_caller_info_pb2._GETUPDATESCALLERINFO
_SYNCCYCLECOMPLETEDEVENTINFO.fields_by_name['source_info'].message_type = _SOURCEINFO
_DEBUGEVENTINFO.fields_by_name['singleton_event'].enum_type = sync_enums_pb2._SYNCENUMS_SINGLETONDEBUGEVENTTYPE
_DEBUGEVENTINFO.fields_by_name['sync_cycle_completed_event_info'].message_type = _SYNCCYCLECOMPLETEDEVENTINFO
_DEBUGEVENTINFO.fields_by_name['datatype_association_stats'].message_type = _DATATYPEASSOCIATIONSTATS
_DEBUGINFO.fields_by_name['events'].message_type = _DEBUGEVENTINFO
DESCRIPTOR.message_types_by_name['TypeHint'] = _TYPEHINT
DESCRIPTOR.message_types_by_name['SourceInfo'] = _SOURCEINFO
DESCRIPTOR.message_types_by_name['SyncCycleCompletedEventInfo'] = _SYNCCYCLECOMPLETEDEVENTINFO
DESCRIPTOR.message_types_by_name['DatatypeAssociationStats'] = _DATATYPEASSOCIATIONSTATS
DESCRIPTOR.message_types_by_name['DebugEventInfo'] = _DEBUGEVENTINFO
DESCRIPTOR.message_types_by_name['DebugInfo'] = _DEBUGINFO

class TypeHint(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEHINT

  # @@protoc_insertion_point(class_scope:sync_pb.TypeHint)

class SourceInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOURCEINFO

  # @@protoc_insertion_point(class_scope:sync_pb.SourceInfo)

class SyncCycleCompletedEventInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYNCCYCLECOMPLETEDEVENTINFO

  # @@protoc_insertion_point(class_scope:sync_pb.SyncCycleCompletedEventInfo)

class DatatypeAssociationStats(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATATYPEASSOCIATIONSTATS

  # @@protoc_insertion_point(class_scope:sync_pb.DatatypeAssociationStats)

class DebugEventInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEBUGEVENTINFO

  # @@protoc_insertion_point(class_scope:sync_pb.DebugEventInfo)

class DebugInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEBUGINFO

  # @@protoc_insertion_point(class_scope:sync_pb.DebugInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), 'H\003`\001')
_SYNCCYCLECOMPLETEDEVENTINFO.fields_by_name['num_blocking_conflicts'].has_options = True
_SYNCCYCLECOMPLETEDEVENTINFO.fields_by_name['num_blocking_conflicts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
_SYNCCYCLECOMPLETEDEVENTINFO.fields_by_name['num_non_blocking_conflicts'].has_options = True
_SYNCCYCLECOMPLETEDEVENTINFO.fields_by_name['num_non_blocking_conflicts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\030\001')
# @@protoc_insertion_point(module_scope)
