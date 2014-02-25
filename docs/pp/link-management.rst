Link Management
===============

The LLCP Link Management component is responsible for link activation,
and deactivation, keep the appearance of a symmetric communication
link, as well as frame aggregation and disaggregation.

.. _p2p_link_activation:

Link Activation
---------------

The link activation is started when the local Medium Access Layer
(MAC) notifies the LLC that a peer device capable of executing LLCP
has come into communication range. Presently, the only MAC layer
defined is the NFC Data Exchange Protocol (DEP). In NFC-DEP, a device
capable of executing LLCP is discovered if the magic octet sequence
``46666Dh`` is received during MAC activation.

The LLCP specification defines that a Parameter Exchange (PAX) PDU is
send and received during activation. However, if the MAC layer is
NFC-DEP, then the LLC Parameters that would go into the PAX PDU are
transmitted as part of the NFC-DEP activation procedure and the PAX
PDU is actually forbidden.

LLC Parameters received are *commitments* of capabilities of the
sending party, not subjected to negotiation. The most important, and
strictly required, parameter is the *Version Number* to indicate the
*major* and *minor* protocol version supported. Both sides then
independently determine the protocol version to run by using the lower
minor version if the major versions are identical. If the major
versions differ then the more advanced implementation may decide if it
can fall back to the <major>.<minor> version of the peer device.

.. requirement::

   The interoperability test scenarios require that NFC devices
   implement at least LLCP Version 1.1.

The *Maximum Information Unit Extension (MIUX)* parameter indicates
the maximum number of information octets that the implementation is
able to receive within a single LLC PDU. The guaranteed MIU is 128
octets and the MIUX parameter only encodes the number of additional
octets that are acceptable. The sum of 128 and MIUX is the *Link
MIU*. It is highly recommended that implementations provide a *Link
MIU* of more than 128 octets (thus send an MIUX parameter). If an
implementation can afford the memory, the largest possible Link MIU of
2176 octets should be used. If a device is short on memory it should
at least use a Link MIU of 248 octets, to allow full utilization of an
NFC-DEP information packet.

.. requirement::

   The interoperability test scenarios require that NFC devices have a
   Link MIU of 248 octets or more.

The *Well-Known Service List (WKS)* parameter informs the peer device
of the well-known service access points that are active on the device
and for which LLC PDUs will be accepted. It does, however, not imply
that other well-known services would not become available after link
activation, for example on a platform with on-demand service
activation. The main purpose of the WKS parameter is to reduce the
amount of service discovery or blind communication attempts.

.. requirement::

   The interoperability test scenarios require that NFC devices send a
   WKS parameter during link activation.

The *Link Timeout (LTO)* parameter announces the maximum time the LLC
may ever need from receiving to returning an LLC PDU. Said
differently, a local LLC can safely assume that if, after sending an
LLC PDU, the remote device's Link Timeout expires before an LLC PDU is
received, that communication will no longer be possible. If an LTO
parameter is not received during link activation, a default value of
100 milliseconds is applied. The larget possible Link Timeout value is
2550 milliseconds which is, as a time to let the user know the end of
communication, not an ideal upper bound.

.. requirement::

   The interoperability test scenarios require that if an LTO
   parameter then the resulting remote Link Timeout value does not
   exceed 1000 milliseconds.

The *Option (OPT)* parameter communicates the link service class
supported by the sending LLC. The link service class indicates the
supported transport types: connection-less, connection-oriented, or
both. If the OPT parameter is not received during link activation (or
the link service class set to zero), the local LLC may behave as if
both connection-less and connection-oriented transport type are
supported.

.. requirement::

   The interoperability test scenarios require that NFC devices support
   both connection-less and connection-oriented transport type and
   send an an OPT parameter during link activation.

#. Enable near field communication between the |DIT| and the |DUT| and
   receive the LLC Parameters.
#. Verify that the VERSION parameter is received and announces a major
   version of 1 and a minor version of 1 or higher.
#. Verify that the MIUX parameter is received with an MIU extension
   value of 120 or more octets (resulting in a remote Link MIU of 248
   or more octets).
#. Verify that the WKS parameter is received and announces presence of
   well-known services at service access point addresses 0, 1, and 4.
#. Verify that if the LTO parameter is received it's value does not
   exceed 100 (resulting in a remote Link Timeout value of no more
   than 1000 milliseconds).
#. Verify that the OPT parameter is received and indicates support for
   both connection-less and connection-oriented transport type
   communication.

.. _p2p_link_deactivation:

Link Deactivation
-----------------

The most usual way of Peer-To-Peer link termination between two NFC
devices is a communication timeout due to both devices moved out of
near field communication range. Nevertheless, a device may for
whatever reason wish to terminate the link while communication would
still be possible. The LLCP specification call this *intentional link
deactivation* and allows a local link management component to send a
Disconnect (DISC) PDU to the remote link management component. No
further PDUs are then to be exchanged between the two LLCs (buffered
transmissions may still be send by a MAC layer but not propagate to
the LLC). Note that unlike termination of a *data link connection* the
link management component receiving a DISC PDU will not return a
Disconnected Mode (DM) PDU.

#. Perform :ref:`p2p_link_activation`
#. Send a Disconnect (DISC) PDU with source service access point
   address 0 to the remote link management component at the
   destination service access point address 0.
#. Verify that the |DUT| does not send any further LLC PDU.

.. _p2p_link_symmetry:

Link Symmetry
-------------

The LLC layer allows service users to run symmetrical communication on
top a master-slave communication style MAC layer such as NFC-DEP. To
applications or protocols on top of LLCP this means that service data
units can be send or received at any point in time, independent of the
time when the other device would eventually ask for or answer a
transmission.

To achieve symmetrical communication both link management components
observe the flow of outbound PDUs and send, if no other PDU is
available, a Symmetry (SYMM) PDU as a substitute. The time until a
SYMM PDU is sent as a substitute is critical for performance and the
appearance of symmetrical communication. Generally it should be as
short as possible, but if an implementation expects other PDUs to
become available within a short amount of time it may well increase
performance if that PDU is sent a few milliseconds later instead of
delaying it until a next PDU is received from the remote LLC. 

.. requirement::

   The interoperability test scenarios require that NFC devices send a
   SYMM PDU no later than 10 milliseconds after a PDU was received and
   no other PDU became availble for sending.

Sometimes a concern exists that if only SYMM PDUs are exchanged with
short delays it does negatively affect power consumption for no useful
information exchange (apart from the fact that two devices are still
in proximity which could as well regarded useful information). Without
debating that concern, a viable way to reduce the exchange of only
SYMM PDUs is to observe when a specific number of SYMM PDUs has been
the only exchange between the two LLCs, and then increase the time
between receiving and returning a SYMM PDU. Any other PDU sent or
received would then restore the original conditions.

.. requirement::

   The interoperability test scenarios require that NFC devices do not
   increase the time between receiving and sending a SYMM PDU before
   at least a consecutive sequence of 10 SYMM PDUs has been received
   and send (5 per direction).

#. Perform :ref:`p2p_link_activation`
#. Verify for at least 5 seconds that Symmetry (SYMM) or other PDUs
   are received within the time limits of the remote *Link Timeout*.
#. Verify that the average time between an outbound and the next
   inbound PDU does not exceed 10 milliseconds until a sequence of 10
   consecutive SYMM PDUs are sent and received (5 per direction).
#. Perform :ref:`p2p_link_deactivation`

.. _p2p_aggregation:

Aggregation
-----------

Frame aggregation allows an LLC to send more than one PDU in a single
transmission using Aggregated Frame (AGF) PDUs. As LLCP allows
multiple conversations at the same time this does almost always
significantly increase data throughput and decrease transaction delays
for all communications running across the LLCP Link. It is thus highly
recommended that NFC Devices implement and use frame aggregation
whenever possible.

.. requirement::

   The interoperability test scenarios require that NFC devices
   implement and use frame aggregation.

Disaggregating AGF PDUs is mandatory for any LLCP implementation. When
disaggregating, embedded PDUs are to be processed in the order they
appear within the AGF PDU and treated as if they were received
individually in that order.

#. Perform :ref:`p2p_link_activation`
#. Send two CONNECT PDUs with different source service access point
   addresses and the destination service access point address ``0``
   aggregated into a single AGF PDU. Both CONNECT PDUs shall not
   contain a Service Name (SN) parameter, so they are not treated as a
   request to resolve and connect by service name.
#. Verify that the |DUT| returns a Disconnected Mode (DM) PDU to each
   of the service access points that sent a CONNECT PDU aggregated
   within a single AGF PDU.
#. Perform :ref:`p2p_link_deactivation`

