# Laser Blaster

Play the Atari 2600 with a laser gun!

<p align="center">
<img src="https://raw.githubusercontent.com/nickbild/laser_blaster/main/media/teaser.gif">
</p>

## How It Works

A Jetson Xavier NX is running the game `Atlantis` on the Stella Atari 2600 emulator.  A projector is displaying the game on a wall.

A camera connected to the Jetson is continually capturing images of the game screen.  A thresholding algorithm implemented in OpenCV searches out the red dot of a laser pointer.

A toy gun modified to "shoot" a laser beam is pointed at the game screen.  An algoritm implemented in Python matches the coordintes of the detected laser dot with coordinates in the field of game play.  When coordinates are within a certain range, actions within the game are carried out by simulating sequences of key presses on the keyboard with the `pynput` Python module.

## Media

YouTube: https://www.youtube.com/watch?v=_1XSo25VdcU

Screenshot:
![Screenshot](https://raw.githubusercontent.com/nickbild/laser_blaster/main/media/screenshot_sm2.jpg)

Blaster:
![Screenshot](https://raw.githubusercontent.com/nickbild/laser_blaster/main/media/blaster_sm.jpg)

Jetson Xavier NX:
![Screenshot](https://raw.githubusercontent.com/nickbild/laser_blaster/main/media/jetson_nx_sm.jpg)

Full setup:
![Screenshot](https://raw.githubusercontent.com/nickbild/laser_blaster/main/media/full_setup_sm2.jpg)


## Bill of Materials

- 1 x NVIDIA Jetson Xavier NX
- 1 x Raspberry Pi Camera v2
- 1 x CSI cable
- 1 x Projector
- 1 x Red laser diode
- 1 x Push button
- 1 x 4.5V battery pack
- 1 x Toy gun
- Miscellaneous wires

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
