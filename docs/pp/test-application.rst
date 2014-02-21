.. |ETA| replace:: *Echo Test Application*
.. |CL-ETA| replace:: *Connection-less Echo Test Application*
.. |CM-ETA| replace:: *Connection-mode Echo Test Application*

Echo Test Application
=====================

The |ETA| is an application running on the |DUT| that uses
functionalities of the local LLCP implementation and API.

.. _cless_echo_test_application:

Connection-less Echo Test Application
-------------------------------------

The |CL-ETA| provides an echo service that receives service data units
on a *logical data link* initiated by the |DIT| and returns the
service data units on a *logical data link* initated by the |DUT|. The
behavior is defined by the following two procedures run concurrently.

* Receive service data units at the local service access point
  ``urn:nfc:sn:dta-cl-echo-in`` and store them as atomic entities
  into a first-in-first-out buffer that is able to hold *N* service
  data unit entities. Start a *delay timer* if the buffer was empty
  before entering a service data unit. If the buffer capacity is
  exhausted when a new service data unit is available then wait until
  it can be successfully stored before accepting a next service data
  unit from the LLC.

* When the delay timer expires retrieve all service data units from
  the buffer and send them, in the order retrieved, to the remote
  service access point ``urn:nfc:sn:dta-cl-echo-out``.

.. _cmode_echo_test_application:

Connection-mode Echo Test Application
-------------------------------------

The |CM-ETA| provides an echo service that receives service data units
on a *data link connection* established by the |DIT| and returns the
service data units on a *data link connection* established by the
|DUT|. The behavior is defined by the following two procedures run
concurrently.

* Receive service data units at the local service access point
  ``urn:nfc:sn:dta-co-echo-in`` and store them as atomic entities into
  a first-in-first-out buffer that is able to hold *N* service data
  unit entities. Start a *delay timer* if the buffer was empty before
  entering a service data unit. If the buffer capacity is exhausted
  when a new service data unit is available then wait until it can be
  successfully stored before accepting a next service data unit from
  the LLC.

* When the delay timer expires retrieve all service data units from
  the buffer and send them, in the order retrieved, to the remote
  service access point ``urn:nfc:sn:dta-co-echo-out``.

