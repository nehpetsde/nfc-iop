Connection Handover
===================

To transfer larger amounts of data between two NFC devices an
alternative carrier connection such as Bluetooth or WiFi can be
identified and initiated with NFC.

The NFC Forum Connection Handover specification defines the framework
that allows to negotiate an alternative carrier for further data
transfer. The device that intends to share data sends a Handover
Request message to the service ``urn:nfc:sn:handover`` of the peer
device. The request informs about the alternative carrier(s) that the
requester has available. The peer device determines if any of the
alternative carriers matches a local carrier and returns a Handover
Select message with one or multiple matching alternative carriers.
That information allows the requester to determine its final
candidate, if any, and use that carrier for the actual data transfer.

Connection Handover can also be performed if one of the devices does
not have a P2P cabable NFC implementation but uses an NFC Tag. In this
case the requester acquires connection handover select information by
reading the tag without prior sending information about its local
alternative carrier technologies. The main difference is thus that the
selector can not adapt its response to the capabilites of the
requester and, if the tag is not internally connected to the host
processor, it can also not adapt to dynamic properties of the
selectable carriers.

The default data format for an NFC Tag for connection handover is an
NDEF message that is a Handover Select Message which allows multiple
carriers or configurations to be included. A *Simplified Tag Format*
can be used if only one carrier is available and additional features
of the *Handover Tag Format* are less important than tag size.

Version 1.3 of the NFC Forum Connection Handover specification
introduced a three party model where a third device mediates
connection handover between two other devices. This allows to
establish an alternative carrier connection between two devices that
can not, or not easily, be brought into near field communication
distance. The mediation process is basically to acquire alternative
carrier information from one device in a first conversation and then
negotiate a suitable technology with the other device in a second
conversation.

Connection handover using NFC has become an important enabler of
easy-to-use spontaneous data sharing between many types of consumer
electronics devices. It is thus an important goal that any NFC-enabled
device with alternative carrier technologies implements and utilizes
connection handover in an interoperable way.

.. requirement::

   The interoperability test scenarios require that an NFC Device with
   alternative carrier technologies such as Bluetooth or Wi-Fi
   implements the NFC Forum Connection Handover specification.

.. rubric:: **Terminology:**

Negotiated Handover
  When two devices run in NFC P2P mode, negotiated handover is used by
  the device that intends to transfer content to propose alternative
  carriers and learn which ones match the capabilities of the other
  device.

Handover Tag Format
  A device using the handover tag format presents alternative carrier
  information in the form of a Handover Select Message. This is
  especially useful if the device has multiple carriers or carrier
  configurations available. Additionally, if the tag is internally
  connected to the host processor it may present carrier power states
  matching reality.

Simplified Tag Format
  A device using the simplified tag format presents a single
  alternative carrier in one NDEF record that marks both start and end
  of the NDEF message.

Handover Requester
  The device that intends to send data over an alternative carrier and
  thus transmits a Handover Request Message to an NFC Peer Device or
  reads alternative carrier information from an NFC Tag.

Handover Selector
  The device that replies a Handover Select Message to an NFC Peer
  Device or supplies alternative carrier information on an NFC Tag.

Handover Mediator

  A device tthat acquires alternative carrier information from two
  other devices to select a suitable alternative and request that a
  connection be established.

.. toctree::
   :maxdepth: 2

   common_procedures
   bluetooth_simple_pairing
   wifi_protected_setup
..
   bluetooth_edr
   wifi_wsc
   wifi_p2p
   mixed_bt_wifi
