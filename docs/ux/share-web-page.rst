Share a web page address
========================

An NFC device with the ability to navigate and render web pages shall
be able to receive and open a web page address that is transferred
using near field communication. It shall also be able to send the
address of a web page that is currently visited and displayed on the
device screen.

A web page address shall be exchanged as an NDEF message with the NFC
Forum Well Known Type "urn:nfc:wkt:U" encoded as defined in the NFC
Forum URI RTD specification.

Test data
---------

* http://www.w3.org
* https://www.ssllabs.com
* http://nfc-forum.org
* https://github.com/

Send a web page address
-----------------------

#. With a web browser open the page at http://www.w3.org
#. Touch the other NFC device and verify the same page is opened.

#. With a web browser open the page at https://www.ssllabs.com
#. Touch the other NFC device and verify the same page is opened.

#. With a web browser open the page at http://nfc-forum.org
#. Touch the other NFC device and verify the same page is opened.

#. With a web browser open the page at https://github.com/
#. Touch the other NFC device and verify the same page is opened.

Receive a web page address
--------------------------

#. Use a web browser on the test device to open the page at
   http://www.w3.org
#. Touch the test device and verify the same page is opened on the
   device under test.

#. Use a web browser on the test device to open the page at
   https://www.ssllabs.com
#. Touch the test device and verify the same page is opened on the
   device under test.

#. Use a web browser on the test device to open the page at
   http://nfc-forum.org
#. Touch the test device and verify the same page is opened on the
   device under test.

#. Use a web browser on the test device to open the page at
   https://github.com/
#. Touch the test device and verify the same page is opened on the
   device under test.

