SNEP Default Server
===================

The SNEP specification defines both a protocol and a *Default SNEP
Server* that can be connected to on services access point address 4 or
with the service name ``urn:nfc:sn:snep``. The *Default SNEP Server*
is a mandatory service on NFC Forum compliant devices.

The *Default SNEP Server* provides a simple inbox into which remote
clients can drop NDEF messages. What then happens with these messages
is not defined but the most natural processing in application hosting
devices such as smartphones is to see if there is an application
installed that can handle the message type that was received.

.. requirement::

   The interoperability test scenarios require that a *Default SNEP
   Server* implementation either dispatches or makes visible the NDEF
   message received such that the success of receiving can be clearly
   identified.

Because the *Default SNEP Server* is a mandatory component on every
NFC Forum Device, the maximum NDEF message size that is guaranteed to
be transmittable is only 1024 octets. However, as application hosting
devices have quite substantially more memory and processing power,
larger transmission sizes are desirable and achievable.

.. requirement::

   The interoperability test scenarios require that a *Default SNEP
   Server* implementation supports NDEF message sizes of at least
   20480 byte (20 KByte).

.. _connect_snep_default_server:

Connect to the Default Server
-----------------------------

The *Default SNEP Server* is a well-known service with the service
access point address 4 and service name ``urn:nfc:sn:snep``. The NFC
Forum Device Requirements mandate that an NFC Forum Device always has
that service available. A SNEP client can choose to either connect
directly to the destination address 4 or use the well-known service
name.

The SNEP protocol uses the LLCP connection-oriented transport type
facility, thus a client first has to establish a *data link
connection* with the server. As part of the connect procedure, the
server will indicate its *data link connection* receive window and
maximum information unit size. To achieve acceptable throughput the
receive window should be at least 2 and the maximum information unit
size be no less than 248 and a multiple of 248.

.. requirement::

   The interoperability test scenarios require that a *Default SNEP
   Server* implementation supports a *data link connection* receive
   window of 2 or more and a maximum information unit size that is a
   multiple of 248 octets.

#. As a choice of the |DIT| send either a CONNECT PDU to service
   access point address 4 or a CONNECT PDU with the service name
   ``urn:nfc:sn:snep`` to service access point 1.
#. Verify that the |DUT| replies with a Connection Complete (CC) PDU.
#. Verify that the CC PDU contains a Receive Windoe (RR) parameter
   with a value of 2 or more.
#. Verify that the CC PDU contains a Maximum Information Unit
   Extension (MIUX) parameter with a value that results in an MUI that
   is a multiple of 248.
#. :ref:`disconnect_snep_default_server`

.. _disconnect_snep_default_server:

Disconnect from the Default Server
----------------------------------

Once a client has established a connection with the server and
potentially transmitted an NDEF message it should disconnect in order
to allow the server free its resources.

#. :ref:`connect_snep_default_server`
#. Send a Disconnect (DISC) PDU on the *data link connection* with the
   *Default SNEP Server*.
#. Verify that the |DUT| confirms termination of the *data link
   connection* with a Disconnected Mode (DM) PDU and reason code 0.

Sequential Connects
-------------------

Although most current usage scenarios involve just the transfer of a
single NDEF message, a *Default SNEP Server* should be prepared to
receive another connection request once a client terminated a previous
*data link connection*.

#. :ref:`connect_snep_default_server`
#. :ref:`disconnect_snep_default_server`
#. :ref:`connect_snep_default_server`
#. :ref:`disconnect_snep_default_server`

Unfragmented Message
--------------------

A SNEP client uses the PUT command to place an NDEF message into the
*Default SNEP Server* inbox. If the NDEF message plus the SNEP
protocol header fit into a single I PDU, the server can immediately
reply with the *Success* response.

#. :ref:`connect_snep_default_server`
#. Send a PUT request with a single record text message that contains
   the string "NFC Interoperability Test Scenarios" in English
   language encoding.
#. Verify that the server replies with a *Success* response and that
   the text is shown on the |DUT|.
#. :ref:`disconnect_snep_default_server`

Fragmented Message
------------------

If the NDEF message plus the SNEP protocol header does not into a
single I PDU, the client must send the message as a sequence of
fragments. The server must wait until the last fragment is received
before sending the *Success* response. To avoid that the client
transmits more data than the server can handle, the first fragment
contains, as part of the SNEP request header, the total NDEF message
size and the server must reply to the first fragment with a *Continue*
or *Reject* response message depending on whether it can receive that
amount of data. If the client receives a *Continue* response it sends
the remaining fragments without further confirmations.

As stated before, the interoperability test scenarios require that a
|DUT| implements the *Default SNEP Server* to accept an NDEF message
of up to 20480 octets total size.

#. :ref:`connect_snep_default_server`
#. Send the first fragment of a PUT request with an NDEF message of
   20480 octet total size.
#. Verify that the server replies with a *Continue* response.
#. Send the remaining octets of the NDEF message.
#. Verify that the server replies with a *Success* response.
#. :ref:`disconnect_snep_default_server`

