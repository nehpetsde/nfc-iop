Service Discovery
=================

Service discovery provides an application component a way to learn if
a corresponding application component is available on the peer device,
and under which service access point address it is expecting to
receive service data units. No distinction between connection-less and
connection-mode transport is made with regard to service discovery.

The primary method for service discovery is to send a Service Name
Lookup (SNL) PDU with one or multiple Service Discovery Request
(SDREQ) parameters to the remote service discovery component at
service access point 1. The remote service discovery component will
then return an SNL PDU with a number of Service Discovery Response
(SDRES) parameters each revealing the service access point address of
one of the requested service names. For the entire near field
communication session these results are cacheable, i.e. service access
point addresses will not change after discovery.

An alternate method for service discovery is to send Service Name (SN)
parameter within a CONNECT PDU to the remote service discovery
component, as a request for both service name lookup and connecting to
that service if it exists. This is also called *connect-by-name* and
intended to provide a fast connect method for client connectors that
are only interested in a single remote service or assume for good
reasons that the service exists.

.. _p2p_service_name_lookup:

Service Name Lookup
-------------------

Verify that a service name is correctly resolved into a service access
point address by the remote LLC. The LLCP Link must be activated prior
to running this scenario.

#. Establish Peer-To-Peer communication between the |DUT| and the |DIT|.
#. Send an SNL PDU with a single SDREQ parameter that encodes the
   value ``urn:nfc:sn:sdp`` to the remote service discovery component
#. Verify that the request is answered with an SNL PDU that contains a
   single SDRES parameter with the SAP value ``1`` and a TID value
   that is the same as the value encoded in the previously transmitted
   SDREQ parameter.
#. Send an SNL PDU with a single SDREQ parameter that encodes the
   value ``urn:nfc:sn:snep`` to the remote service discovery component
#. Verify that the request is answered with an SNL PDU that contains a
   single SDRES parameter with the SAP value ``4`` and a TID value
   that is the same as the value encoded in the previously transmitted
   SDREQ parameter.
#. Send an SNL PDU with a one SDREQ parameter that encodes the value
   ``urn:nfc:sn:sdp`` and one SDREQ parameter that encodes the value
   ``urn:nfc:sn:snep`` to the remote service discovery component
#. Verify that the request is answered with an SNL PDU that contains
   two SDRES parameters with TID values matching the previously
   transmitted TID values, resolving ``urn:nfc:sn:sdp`` to the service
   access point value ``1`` and ``urn:nfc:sn:snep`` to the service
   access point value ``4``.
#. Terminate Peer-To-Peer communication.

.. _p2p_connect_by_name:

Connect By Name
---------------

Verify that a data link connection can be established by specifying a
service name. The LLCP Link must be activated prior to running this
scenario and the connection-oriented mode echo service must be in the
unconnected state.

#. Establish Peer-To-Peer communication between the |DUT| and the |DIT|.
#. Send a CONNECT PDU with a Service Name (SN) parameter that encodes
   the value ``urn:nfc:sn:snep`` to the service discovery component on
   the |DUT|.
#. Verify that the |DUT| confirms the connect request with a
   Connection Complete (CC) PDU.
#. Terminate Peer-To-Peer communication.
