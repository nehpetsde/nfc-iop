.. |ETA| replace:: *Connection-less Echo Test Application*

Connection-less Transport
=========================

Connection-less transport provides best effort delivery of service
data units between a local and a remote service access point in either
direction. An connection-less transport channel is termed a *logical
data link* and implied by a pair of local and remote service access
point adress values used in a Unnumbered Information (UI) PDU. No
setup or termination procedure exisits for a *logical data link*.

Due to the Medium Access (MAC) layer guarantees any outbound LLCP PDU,
includinga UI PDU, will arrive at the remote LLC layer. However, a
local LLC or remote LLC may drop a UI PDU at any point in time without
notification.

The scenarios in this section require that the |DUT| has the |ETA|
installed and accessible under the service name
``urn:nfc:sn:dta-cl-echo-in``.

.. _p2p_cless_eta_sot:

Start of Test Sequence
----------------------

The *start of test* sequence is common to all further test scenarios
for connection-less transport mode. Run as a dedicated test scenario,
the following steps verify that the |DUT| has the |ETA| installed and
accessible, and that the |ETA| attempts to discover the service access
point address for returning data packets to the |DIT|.

#. Perform service discovery to learn the remote service access point
   address value for the service name ``urn:nfc:sn:dta-cl-echo-in``.
#. Send a service data unit with the ASCII string "SOT" to the |ETA|
   to indicate the start of test.
#. Verify that the |ETA| performs service discovery to learn the
   service access point address value for the service name
   ``urn:nfc:sn:dta-cl-echo-out`` on the |DIT|.

Guaranteed Information Size
---------------------------

The guaranteed information size for an outbound Unnumbered Information
(UI) PDU is 128 octets. Although implementations should support a
larger number of information octets, an application designed to work
with a variety of peer devices must be able to function even if only
the guaranteed information size is available.

#. Perform the :ref:`p2p_cless_eta_sot`
#. Send a service data unit with 128 random octets to the |ETA|.
#. Verify that the |ETA| sends the same service data unit to the local
   service access point bound to ``urn:nfc:sn:dta-cl-echo-out``.

Maximum Information Size
------------------------

The maximum information size of any outbound Unnumbered Information
(UI) PDU is determined by the Link MIU value that the remote device
transmitted during LLCP Link Activation. The purpose of this scenario
is to verify that the |DUT| accepts a UI PDU with a number of
information octets equal to the device's Link MIU. Note that in order
to run this test the |DIT| must have a Link MIU that is equal or
greater than the Link MIU of the |DUT| because otherwise the |ETA|
will not be able to return the service data unit.

#. Perform the :ref:`p2p_cless_eta_sot`
#. Send a service data unit with **N** random octets to the |ETA|, with
   the value of **N** being equal to the Link MIU of the |DUT|.
#. Verify that the |ETA| sends the same service data unit to the local
   service access point bound to ``urn:nfc:sn:dta-cl-echo-out``.

Packet Loss Stimulation
-----------------------

#. Determine the echo buffer capacity **C** and delay **D** of the
   |ETA| running on the |DUT|.
#. Perform the :ref:`p2p_cless_eta_sot`
#. Within **D** seconds send **C + 1** service data units of 128
   octets to the |ETA|.
#. Verify that the |ETA| returns the first **C** service data units to
   the local service access point at ``urn:nfc:sn:dta-cl-echo-out``.
#. Send one service data unit of 128 octets to the |ETA|.
#. Verify that the |ETA| returns the service data unit to the local
   service access point at ``urn:nfc:sn:dta-cl-echo-out``.

Link MIU Adherence
------------------

The maximum information size of an outbound Unnumbered Information PDU
must not exceed the Link MIU of the remote device. This test scenario
verifies that the |DUT| observes the Link MIU value of the |DIT| by
sending a service data unit that is one octet larger than the |DIT|
will be able to receive. The test requires that the |DUT| has a Link
MIU of at least 129 octets and that the |DIT| is able to configure its
own Link MIU prior to running the test.

#. Determine the Link MIU of the |DUT| as **N** and configure the
   |DIT| to use a Link MIU of **N - 1**.
#. Perform the :ref:`p2p_cless_eta_sot`
#. Send a service data unit of **N** octets to the |ETA|.
#. Verify that the |ETA| does not return the service data unit to the
   local service access point at ``urn:nfc:sn:dta-cl-echo-out`` after
   the echo buffer delay time.
#. Send a service data unit of **N - 1** octets to the |ETA|.
#. Verify that the |ETA| returns the service data unit to the
   local service access point at ``urn:nfc:sn:dta-cl-echo-out``.
