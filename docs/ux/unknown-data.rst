Handling of unknown data
========================

From time to time a device may receive information types it does not
understand and can therefore not process. On a fixed function device
this will be known by design while on an application hosting device it
will typically mean that no appropriate data handler was found. It is
desirable that a user is appropriately informed about this situation
and not left with the impression that NFC is not working.

Receive unknown data from device
--------------------------------

#. Prepare the |DIT| to send a single record NDEF message with the
   media type "application/octet-stream" and some arbitrary amount of
   payload data bytes when near field communication is established.

#. Establish near field communication between the |DIT| and the |DUT|
   and verify that the user is notified of unknown content being
   received.

#. Prepare the |DIT| to send a single record NDEF message with the
   NDEF record type "Unknown" (Type Name Format value 0x05) and some
   arbitrary amount of payload data bytes when near field
   communication is established.

#. Establish near field communication between the |DIT| and the |DUT|
   and verify that the user is notified of unknown content being
   received.

Read unknown data from tag
--------------------------

#. Prepare a tag to contain a single record NDEF message with the
   media type "application/octet-stream" and some arbitrary amount of
   payload data bytes.

#. Use the |DUT| to the tag and verify that the user is notified of
   unknown content being received.

#. Prepare a tag to contain a single record NDEF message with the NDEF
   record type "Unknown" (Type Name Format value 0x05) and some
   arbitrary amount of payload data bytes.

#. Use the |DUT| to read the tag and verify that the user is notified
   of unknown content being received.
