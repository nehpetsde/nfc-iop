Bluetooth Simple Pairing
========================

Version 2.1 + EDR (BR/EDR) of the Bluetooth Core Specification
introduced Secure Simple Pairing with four association models: *Just
Works*, *Numeric Comparision*, *Passkey Entry* and *Out Of Band*. In
version 4.0 the security model for Bluetooth Low Energy (LE) was added
for similar association models except *Numeric Comparision*.

The general phases to achieve an association between two Bluetooth
devices are (1) Device Discovery, (2) Bluetooth Connection, (3)
Security Establishment, and (4) Device Authentication. Device
Discovery can be achieved in-band or out-of-band using NFC and
basically makes the Bluetooth address known to the other device. If
the out-of-band communication transmitted security information, that
information will then be used during Device Authentication to achieve
secure pairing with protection against man-in-the-middle attacks
without requiring the user to input a passkey or confirm that numeric
values shown are equal.

*An illustration of the Secure Simple Pairing Association Models can be
found in the Bluetooth Core Specification Version 4.1, Volume 1, Part
A, Section 5.2.4.5, Figure 5.2.*

The data format for Bluetooth Out Of Band pairing for Bluetooth BR/EDR
and Bluetooth LE is defined within the Bluetooth specification. For
NFC transmission it becomes the payload of an NDEF record termed
*Bluetooth BR/EDR Carrier Configuration Record* and *Bluetooth LE
Carrier Configuration Record*. The NFC Forum and Bluetooth SIG
*Bluetooth Secure Simple Pairing using NFC* Application Document
contains implementation hints and recommendations on optional data
elements that should be included in the out-of-band data when used
with NFC.

.. rubric:: **Bluetooth BR/EDR Carrier Configuration Record**

The record type is the Internet Media Type
"application/vnd.bluetooth.ep.oob" and the payload is the Bluetooth
BR/EDR out-of-band configuration data.

The configuration data must include the *BR/EDR Bluetooth Device
Address* and may include any number of *Extended Inquiry Response*
(EIR) data elements.

For negotiated connection handover both devices have the ability to
transmit the *Simple Pairing Hash C* and *Simple Pairing Randomizer R*
that allow the receiver to then authenticate the device during
Bluetooth link setup.

.. requirement::

   The interoperability test scenarios require that Bluetooth BR/EDR
   Carrier Configuration data includes the Simple Pairing Hash and
   Randomizer if negotiated handover is performed.
   
The Bluetooth Device Name allows a graphical user interface to better
represent the other device in informational messages that may be shown
while connecting or especially if the connection could not be made
(for example if the other device kept the Bluetooth radio deactivated
and thus a device name could also not be learned through Bluetooth
inquiry).

.. requirement::

   The interoperability test scenarios require that Bluetooth BR/EDR
   Carrier Configuration data includes the Bluetooth Local Name
   (Device Name).


.. rubric:: **Bluetooth LE Carrier Configuration Record**

The record type is the Internet Media Type
"application/vnd.bluetooth.le.oob" and the payload is the Bluetooth
LE out-of-band configuration data.

The configuration data must include the *LE Bluetooth Device Address*
and *LE Role* and may include any number of other *Advertising and Scan
Response Data* (AD) elements.

For negotiated connection handover both devices have the ability to
transmit the *Temporary Key TK* that allows the receiver to
authenticate the device during Bluetooth link setup.

.. requirement::

   The interoperability test scenarios require that Bluetooth LE
   Carrier Configuration data includes the Temporary Key TK value if
   negotiated handover is performed.
   
The Bluetooth Device Name allows a graphical user interface to better
represent the other device in informational messages that may be shown
while connecting or especially if the connection could not be made
(for example if the other device kept the Bluetooth radio deactivated
and thus a device name could also not be learned through Bluetooth
inquiry).

.. requirement::

   The interoperability test scenarios require that Bluetooth LE
   Carrier Configuration data includes the Bluetooth Local Name
   (Bluetooth Device Name).


.. contents:: **List of Test Scenarios**
   :local:
   :depth: 1
   :backlinks: none


Negotiated Handover with Bluetooth BR/EDR Device
------------------------------------------------

#. Perform :ref:`p2p_link_activation` and :ref:`ch_establish_connection`
#. Send a Handover Request Message with a Bluetooth BR/EDR Carrier
   Configuration Record that includes the Bluetooth Device Address,
   Simple Pairing Hash C, Simple Pairing Randomizer R, Class of
   Device, Local Name and appropriate Service Class UUIDs.
#. Verify that the |DUT| returns a Handover Select Message with a
   Bluetooth BR/EDR Carrier Configuration Record that includes the
   Bluetooth Device Address, Simple Pairing Hash C, Simple Pairing
   Randomizer R, Class of Device, Local Name and appropriate Service
   Class UUIDs.
#. :ref:`ch_terminate_connection`
#. Verify that a Bluetooth connection can be made to the |DUT|.

Negotiated Handover with Bluetooth LE Device
--------------------------------------------

#. Perform :ref:`p2p_link_activation` and :ref:`ch_establish_connection`
#. Send a Handover Request Message with a Bluetooth LE Carrier
   Configuration Record that includes the Bluetooth Device Address, LE
   Role, Temporary Key TK, and Local Name.
#. Verify that the |DUT| returns a Handover Select Message with a
   Bluetooth LE Carrier Configuration Record that includes the
   Bluetooth Device Address, LE Role, Temporary Key TK, and Local
   Name.
#. :ref:`ch_terminate_connection`
#. Verify that a Bluetooth connection can be made to the |DUT|.


Static Handover with Bluetooth BR/EDR Device
--------------------------------------------

Handover Tag Format
^^^^^^^^^^^^^^^^^^^

#. Read the NDEF Message from the NFC Tag presented by the |DUT|.
#. Verify that the NDEF Message is a Handover Select Message with a
   Bluetooth BR/EDR Carrier Configuration Record that includes the
   Bluetooth Device Address, Class of Device, Local Name and
   appropriate Service Class UUIDs.
#. Verify that a Bluetooth connection can be made to the |DUT|.

Simplified Tag Format
^^^^^^^^^^^^^^^^^^^^^

#. Read the NDEF Message from the NFC Tag presented by the |DUT|.
#. Verify that the NDEF Message is a single Bluetooth BR/EDR Carrier
   Configuration Record that includes the Bluetooth Device Address,
   Class of Device, Local Name and appropriate Service Class UUIDs.
#. Verify that a Bluetooth connection can be made to the |DUT|.

Static Handover with Bluetooth LE Device
----------------------------------------

Handover Tag Format
^^^^^^^^^^^^^^^^^^^

#. Read the NDEF Message from the NFC Tag presented by the |DUT|.
#. Verify that the NDEF Message is a Handover Select Message with a
   Bluetooth LE Carrier Configuration Record that includes the
   Bluetooth Device Address, Generic Access Profile Role, Appearance,
   Flags and Local Name.
#. Verify that a Bluetooth connection can be made to the |DUT|.

Simplified Tag Format
^^^^^^^^^^^^^^^^^^^^^

#. Read the NDEF Message from the NFC Tag presented by the |DUT|.
#. Verify that the NDEF Message is a single Bluetooth LE Carrier
   Configuration Record that includes the Bluetooth Device Address,
   Generic Access Profile Role, Appearance, Flags and Local Name.
#. Verify that a Bluetooth connection can be made to the |DUT|.


