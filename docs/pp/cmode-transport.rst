.. |ETA| replace:: *Connection-mode Echo Test Application*

Connection-mode Transport
=========================

.. note::

   The scenarios in this section require that the |DUT| has the
   :ref:`cmode_echo_test_application` installed and accessible under
   the service name ``urn:nfc:sn:dta-co-echo-in``.

Connection-mode transport provides sequenced and guaranteed delivery
of service data units between a local and a remote service access
point in either direction. An established connection-mode transport
channel is termed a *data link connection*. A request for a *data link
connection* is made by sending a CONNECT PDU to the remote service
access point. A request for a *data link connection* is either
confirmed with a Connect Complete (CC) PDU, or rejected with a
Disconnected Mode (DM) PDU. Once established, service data units can
be moved over a *data link connection* using sequentially numbered
Information (I) PDUs.

The flow of I PDUs from sender to receiver is regulated by a sliding
window control scheme. A receive window (RW) that is announced during
connection setup informs the sender of the number of I PDUs it may
send before there comes acknowledgement. Conceptually this is best
imagined as a receive buffer to hold up to RW number of I PDUs that
fills when I PDUs are received from the remote endpoint and empties
when they get dispatched to the upper layer service user. The sender
incrementall count of outbound I PDUs is transmitted in the *send
sequence number* N(S) field of the I PDU. The receiver populates the
*receive sequence number* N(R) field of outbound Information (I) or
Receive Ready (RR) or Receive Not Ready (RNR) PDUs with the N(S) of
the last I PDU successfully dispatched to the service user, thereby
providing acknowledgement and an update of the receive buffer fill
status.

To fit into transmissions, the send and receive sequence numbers must
be limited using modular arithmetic. LLCP has choosen the modulus 16
so that the send and receive sequence number can be transmitted in a
single octet, each consuming 4 bits. Consequently the largest possible
receive window size is 15. With the sequence number of the next
in-sequence I PDU to be sent denoted by the *send state variable* V(S)
and the most recently received N(R) value kept in the *send
acknowledgement state variable* V(SA), both initialized with 0 after
connection setup, then **V(S) - V(SA) = RW (mod 16)** means that the
remote endpoint's receive window is exhausted and an I PDU can not be
send. If an I PDU can be send then the *send state variable* V(S)
becomes **V(S) + 1 (mod 16)** after transmission.

As *data link connections* are bi-directional acknowledgement, by
means of the *receive sequence number*, is ideally transmitted with
the I PDUs flowing back and forth. However, if there's no information
to send but acknowledgement due, Receive Ready (RR) or Receive Not
Ready (RNR) PDUs must be used to convey a new N(R) value to the remote
endpoint. For the purpose of sending acknowledgement and flow control
there is no difference between sending RR versus RNR. The difference
is that sending RNR indicates that the local service user is
temporarily unable to consume further data and it's advisable that the
remote service user stops generating (or whatever is appropriate). For
example, the :ref:`cmode_echo_test_application` operates a buffer for
data units that regulates how many I PDUs can be dispatched from the
receive window. If the receive window would be 3 and the buffer
capacity 2, then in total 5 I PDUs may be send by the remote endpoint
before all gets stuck. By transmitting the busy signal when the echo
buffer becomes full, the remote party can adjust and stop generating.

LLCP requires that the MAC layer is reliable, i.e. data send by a
local LLC is guaranteed to arrive at the remote LLC. For *data link
connections* this means that a sender does not need to memorize
outbound I PDUs for potential retransmission and no mechanism exists
that would allow a receiver to request retransmission of an I
PDU. What though may happen is that *send sequence numbers* received
from the remote endpoint are not monotonically increasing (modulo 16)
due to implementation errors in the remote send or the local receive
unit. If that happens, the receiver will send a Frame Reject (FRMR)
PDU to notify the sender and immediately regard the *data link
connection* as terminated.

.. _cmode_eta_connect:

Connection Establishment
------------------------

A *data link connection* must be established between a local and a
remote service access point before Information PDUs can be
exchanged. A connection is requested with a CONNECT PDU to the remote
service access point and confirmed with a Connection Complete (CC) PDU
to the service access point from which the CONNECT PDU was sent. The
address of the remote service access point can be learned through
explicit service discovery sending a Service Name Lookup (SNL) PDU
with a service name parameter to the remote service discovery
component and learning the address from a response SNL PDU, or by
implicit service discovery where the service name is provided as a
parameter with a CONNECT PDU to the service discovery component
address. The test scenario allows either method to be used by the
|DIT| and |DUT| because it is not an interoperability concern which
method an implementation prefers.

The |ETA| is designed as a service that first accepts a connection
request on the local service access point bound to the service name
``urn:nfc:sn:dta-co-echo-in``, and then issues a connection request to
the remote service access point that is identified by the service name
``urn:nfc:sn:dta-co-echo-out``. The steps below verify this behavior
and serve as a *start of test* sequence.

#. Request a *data link connection* with the |ETA|. It is an
   implementation choice of the |DIT| whether the remote service name
   ``urn:nfc:sn:dta-co-echo-in`` is first resolved into the service
   access point address and followed by a CONNECT PDU to that address,
   or a CONNECT PDU is send to the service discovery component with
   the service name ``urn:nfc:sn:dta-co-echo-in`` provided as a
   parameter.
#. Verify that the connect request is confirmed by the |ETA| with a
   Connection Complete (CC) PDU. If the CONNECT PDU was sent to the
   service discovery component verify that the CC PDU source service
   access point (SSAP) address is different from 1.
#. Wait until the |DUT| requests a *data link connection* with the
   service access point that is bound to the service name
   ``urn:nfc:sn:dta-co-echo-out`` on the |DIT|.  It is an
   implementation choice of the |DUT| whether it first resolves the
   service name into a service access point address and then sends a
   CONNECT PDU to that address, or sends a CONNECT PDU with the
   service name provided as a parameter to the service discovery
   component on the |DIT|.
#. Confirm the connect request with a Connection Complete (CC) PDU.

The *data link connection* requested by the |DIT| is further referred
to as the *outbound data link connection*. The *data link connection*
requested by the |DUT| is further referred to as the *inbound data
link connection*.

.. _cmode_eta_disconnect:

Connection Termination
----------------------

A *data link connection* may at any time be terminated from either
side of the connection. The party wishing to terminate must send a
Disconnect (DISC) PDU to the remote service access point of the *data
link connection*, which the receiver answers with a Disconnected
Mode (DM) PDU. The *data link connection* is then terminated and
applications on both sides notified.

#. Perform :ref:`cmode_eta_connect`.
#. Terminate the *outbound data link connection*.
#. Verify that the |ETA| confirms termination of the *outbound data
   link connection*.
#. Wait until the |ETA| terminates the *inbound data link connection*.
#. Confirm termination of the *inbound data link connection*.

Guaranteed Information Size
---------------------------

The guaranteed information size for an outbound Information (I) PDU is
128 octets. Although implementations should support a larger number of
information octets, an application designed to work with a variety of
peer devices must be able to function even if only the guaranteed
information size is available.

#. Perform :ref:`cmode_eta_connect`.
#. Send a service data unit of 128 octets over the *outbound data link
   connection* to the |ETA|.
#. Verify that receipt of the service data unit is acknowledged by the
   |DUT|.
#. Verify that the |ETA| returns the service data unit over the
   *inbound data link connection* after the echo buffer delay time.
#. Perform :ref:`cmode_eta_disconnect`.

Maximum Information Size
------------------------

The maximum information size of an outbound Information (I) PDU is
determined by the *data link connection* MIU value that the remote
service access point transmitted during connection establishment. The
purpose of this scenario is to verify that the |DUT| accepts an
Information PDU with a number of information octets equal to the MIU
of the remote service access point on the *outbound data link
connection*. Note that in order to run this test, the |DIT| must
provide the same MIU on the *inbound data link connection* because
otherwise the |ETA| will not be able to return the service data unit.

#. Perform :ref:`cmode_eta_connect`.
#. Send a service data unit with **N** random octets on the *outbound
   data link connection* to the |ETA|, with the value of **N** being
   equal to the remote MIU of the *outbound data link connection*.
#. Verify that receipt of the service data unit is acknowledged by the
   |DUT|.
#. Verify that the |ETA| returns the service data unit over the
   *inbound data link connection* after the echo buffer delay time.
#. Perform :ref:`cmode_eta_disconnect`.

Sequence Number Cycling
-----------------------

Information (I), Receive Ready (RR), and Receive Not Ready (RNR) PDUs
carry send and receive sequence numbers for the purpose of flow
control and to acknowledge when the information field of an I PDU has
been dispatched to the service user. Sequence numbers start at zero
for a new *data link connection* and then increment with **(N + 1) mod
16**. The purpose of this test scenario is to cycle through all
possible sequence number values and verify the |DUT| behavior.

#. Perform :ref:`cmode_eta_connect`.
#. Send 17 service data units with 128 octets each on the *outbound
   data link connection* to the |ETA|.
#. Verify that all service data units are acknowledged by the |DUT|
   and successively returned on the *inbound data link connection*.
#. Perform :ref:`cmode_eta_disconnect`.

Receiver Busy Condition
-----------------------

The purpose of this test scenario is to verify that the |ETA| busy
state is signaled by the |DUT| when it is no longer able to retrieve
service data units from the LLC. The condition is forced by the |DIT|
when it stops retrieving service data units on the *inbound data link
connection* (the |ETA| will then not be able to return all service
data units to the |DIT|).

#. Perform :ref:`cmode_eta_connect`.
#. Send one service data unit over the *outbound data link
   connection* to the |DUT|.
#. Verify that the same service data unit is received on the *inbound
   data link connection* from the |DUT| after the |ETA| buffer delay
   time.
#. Stop retrieving service data units from the *inbound data link
   connection* (the LLC layer will still receive Information PDUs
   until the Receive Window (RW) is exhausted).
#. Continuously send service data units over the *outbound data link
   connection* to the |DUT| until the remote Receive Window (RW) is
   exhausted and verify that the |ETA| has entered the busy state and
   caused its LLC to send Receive Not Ready (RNR) PDUs on the
   *outbound data link connection*.
#. Resume retrieving service data units from the *inbound data link
   connection* and verify that all service data units previously sent
   over the *outbound data link connection* are received in
   order. This may take two or more times the |ETA| buffer delay time
   depending on the *outbound data link connection* remote Receive
   Window (RW) and the |ETA| echo buffer capacity.
#. Verify that |ETA| has left the busy state and caused its LLC to
   send a Receive Ready (RR) PDU on the *outbound data link
   connection*.
#. Perform :ref:`cmode_eta_disconnect`.
