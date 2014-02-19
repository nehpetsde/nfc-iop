Share an image or photo
=======================

An NFC device with the ability to capture photographs or otherwise
hold and display pictures shall be able to share them with another
device if both devices feature a common alternative high-speed carrier
technology. The default context for initiating a share action shall be
the visual rendering of an image on the source device. Sharing is then
initiated when near field communication with another device is
established and common alternative carrier discovered.

Send an image
-------------

#. Choose an image on the |DUT| and make it render on the screen or
   otherwise selected for sharing when near field commication will be
   established.

#. Establish near field communication between the |DUT| and |DIT| and
   verify that the |DUT| starts sending the image.

Receive an image
----------------

#. Choose an image on the |DIT| and make selected for sharing when
   near field commication will be established.

#. Establish near field communication between the |DUT| and |DIT| and
   verify that the image is received by the |DUT| immediately or after
   a single confirmation. If a Bluetooth alternative carrier is used
   for the data transfer the user shall not be requested to confirm
   device pairing.
