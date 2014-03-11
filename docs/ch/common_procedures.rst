Common Procedures
=================

The Connection Handover specification defines a framework that allows
two implentations to exchange information about alternative carriers
and perform a selection process. The protocol follows a client-server
model and does not require the server to keep state information
between successive client requests.

Connection handover protocol messages are exchanged over an LLCP *data
link connection* and thus require connection setup before the handover
message exchange. The service access point of a remote handover server
application is determined by the NFC Forum registered service name
``urn:nfc:sn:handover``.

For performance reasons, the *data link connection* should allow LLCP
Information (I) PDUs to utilize at least the full transport capacity
of an NFC-DEP MAC layer PDU.

.. requirement::

   The interoperability test scenarios require that a connection
   handover implementation provides a data link connection MIU of at
   least 248 octets.

.. _ch_establish_connection:

Establish Connection with Server
--------------------------------

The purpose this test scenario is to verify that a handover server
implementation accepts a *data link connection* request from a remote
client and provides a reasonable *data link connection* MIU. The
reason why this is separate from :ref:`ch_terminate_connection` is to
be re-usable in other test scenarios.

#. Establish a *data link connection* with the ``urn:nfc:sn:handover``
   service on the |DUT|. It is an implementation choice of the |DIT|
   whether the service name is first resolved into the service access
   point address and followed by a CONNECT PDU to that address, or a
   CONNECT PDU is send to the service discovery component with the
   service name provided as a parameter.
#. Verify that the remote *Maximum Information Unit* MIU of the *data
   link connection* is 248 or more octets.
#. Perform :ref:`ch_terminate_connection`

.. _ch_terminate_connection:

Terminate Connection with Server
--------------------------------

The purpose this test scenario is to verify that a handover server
implementation allows the client to orderly terminate the *data link
connection*. The reason why this is separated from
:ref:`ch_establish_connection` is to be re-usable in other test
scenarios.

#. Perform :ref:`ch_establish_connection`
#. Send a Disconnect (DISC) PDU to terminate the *data link
   connection* with the connection handover service on the |DUT|.
#. Verify that the |DUT| replies with a Disconnected Mode (DM) PDU.

Sequentially Establish Connection
---------------------------------

The purpose of this test scenario is to ensure that a handover server
implementation returns to the connectable state after the client has
closed the *data link connection*.

#. Perform :ref:`ch_establish_connection`
#. Perform :ref:`ch_terminate_connection`
#. Perform :ref:`ch_establish_connection`
#. Perform :ref:`ch_terminate_connection`

Multiple Messages from Client
-----------------------------

The purpose of this test scenario is to ensure that the handover
server implementation keeps the *data link connection* and responds to
handover messages until the client terminates. This allows a handover
requester to ask for only a specific subset of alternative carriers in
a first message to impose a strong preference on the handover
selector. It also allows a handover mediator to send a handover
initiate message after receiving a handover select message over the
same *data link connection*.

#. Perform :ref:`ch_establish_connection`
#. Send a handover request message with a single alternative carrier
   of type ``urn:nfc:ext:nfc-forum.org:x-unknown-carrier-type-1``.
#. Verify that the |DUT| returns a Handover Select Message with an
   empty alternative carrier selection.
#. Send a handover request message with a single alternative carrier
   of type ``urn:nfc:ext:nfc-forum.org:x-unknown-carrier-type-2``.
#. Verify that the |DUT| returns a Handover Select Message with an
   empty alternative carrier selection.
#. Perform :ref:`ch_terminate_connection`

.. _ch_accept_connection:

Accept Connection from Client
-----------------------------

The purpose of this test scenario is to ensure that a handover client
implementation on the |DUT| establishes the *data link connection*
with an MIU of at least 248 octets.

#. Activate the local handover server and wait for a *data link
   connection* request from the |DUT|.
#. Verify that the remote *Maximum Information Unit* MIU committed
   with the *data link connection* request is 248 or more octets.
#. Confirm the *data link connection*.
#. Receive and reply connection handover protocol messages until the
   client terminates the *data link connection*.

Handover Request Collision
--------------------------

The connection handover protocol is run by a local client against with
a remote server on behalf of an, explicit or implicit, user intention
for data sharing. If both devices intend to share data, the local
connection handover clients will both connect to the remote servers to
send a handover request message and attempt to perform the role of a
Handover Requester. In order to proceed with connection handover, one
device must switch role to become the Handover Selector and avoid that
both devices eventually try to establish the alternative carrier
connection. In case that one device has received the handover request
message early enough to stop sending, that device will simply switch
role and become the Handover Selector. However, if both devices have
sent the handover request message, the conflict is resolved by
comparing a local and a remote random number that have been mutually
exchanged with the handover request messages.

If the sent and received random number are equal, both devices need to
again send a handover request message with a newly generated random
number. Otherwise, the random numbers are compared to determine the
roles, using both the numerical value represented by all 16 bits of
the random number and the value of the least significant bit in
spearate comparisions. If the least significant bit of both numbers
are equal, the device that sent the numerically greater random number
continues as the Handover Selector. If the least significant bit of
both numbers are different, the device that sent the numerically lower
random number continues as the Handover Selector.

#. Activate the local handover server and wait until *data link
   connection 1* has been established by the |DUT|.
#. Perform :ref:`ch_establish_connection` to get *data link connection 2*.
#. Wait to receive a Handover Request Message from the |DUT| over
   *data link connection 1*.
#. Send a Handover Request Message with the same random number as
   received from the |DUT| (using *data link connection 2*).
#. Verify that the |DUT| sends a further Handover Request Message with
   a different random number (using *data link connection 1*).
#. If possible, send a Handover Request Message with a random number
   that assigns the role of Handover Selector to the |DUT| (using
   *data link connection 2*). Otherwise return to step 4.
#. Verify that the |DUT| closes *data link connection 1* and returns a
   Handover Select Message over *data link connection 2*.
#. Perform :ref:`ch_terminate_connection` to close *data link connection 2*.
