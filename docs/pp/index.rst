Peer Communication
==================

Near field communication between peer devices is facilitated by the
Logical Link Control Protocol (LLCP). LLCP provides for independent
connection-less and connection-mode transport channels that allow
concurrent transfer of service data units.

Peer communication test scenarios attempt to ensure that components on
top of LLCP can communicate with peer components over the near field
communication link at the time established and benefit from the
service guarantees designed into the protocol.

In order to execute peer communication test scenarios a |DIT| must
provide a mode that allows triggering and execution of selected
scenarios in the manner and with the technical steps and details
defined.

For a |DUT| to participate in peer communication test scenarios the
:doc:`test-application` is required to provide specific test services
on top of LLCP.

.. toctree::
   :maxdepth: 2

   test-application
   link-management
   service-discovery
   cless-transport
   cmode-transport
