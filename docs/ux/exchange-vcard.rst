Exchange contact information
============================

An NFC device with the ability to handle contact information shall be
able to receive and persistently add contact information when touched
to another NFC device or tag that presents such information. It shall
also be able to send contact information to another NFC device if the
user intends to do so. The user's intention to share contact
information shall be assumed if a contact is displayed. The user's
consent to send contact information should be implied by the fact
that (a) contact information is displayed and (b) the device has
established near field communication with another device. The user's
consent to receive contact information should be implied by the fact
that near field communication was established. Prior to both sending
and receiving contact information a confirmation dialog may be
displayed.

Personal contact information shall be send to a SNEP Default Server as
an NDEF message with media type "text/vcard". The NDEF message should
contain no more than one record with media type "text/vcard". If the
message contains more than one media type "text/vcard" record only the
first shall be processed.

The payload of an NDEF record with media type "text/vcard" shall
contain a vCard data object that complies with :rfc:`6350`.

Example vCard for test
----------------------

::

   BEGIN:VCARD
   VERSION:4.0
   N:Gump;Forrest;;;
   FN:Forrest Gump
   ORG:Bubba Gump Shrimp Co.
   TITLE:Shrimp Man
   PHOTO;MEDIATYPE=image/gif:http://www.example.com/dir_photos/my_photo.gif
   TEL;TYPE=work,voice;VALUE=uri:tel:+1-111-555-1212
   TEL;TYPE=home,voice;VALUE=uri:tel:+1-404-555-1212
   ADR;TYPE=work;LABEL="100 Waters Edge\nBaytown, LA 30314\nUnited States of America"
     :;;100 Waters Edge;Baytown;LA;30314;United States of America
   ADR;TYPE=home;LABEL="42 Plantation St.\nBaytown, LA 30314\nUnited States of America"
     :;;42 Plantation St.;Baytown;LA;30314;United States of America
   EMAIL:forrestgump@example.com
   END:VCARD

Read vCard from tag
-------------------

#. Write the example vCard to an NFC tag.

#. Read from the vCard from the NFC tag. All properties except PHOTO
   must be imported successfully.

Send vCard to device
--------------------

#. Open the contact manager application and display a single entry.

#. Perform any required user interface operations to start sharing the
   contact entry.

#. Touch the other device to send the contact information.

#. Verify that the other device has received the vCard.

Receive vCard from device
-------------------------

#. Close all applications on the device under test.

#. Prepare the other device to send contact information when near
   field communication is established.

#. Touch both devices to establish near field communication.

#. Verify that a vCard is received and properly saved (optionally
   after confirmation).

Mutually exchange vCard
-----------------------

#. Prepare both devices to share contact information when near field
   communication is established.

#. Touch both devices to establish near field communication.

#. Verify that both devices received and properly saved a vCard.
