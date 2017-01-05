#!/usr/bin/env python
# coding: utf-8
''' This is part of the MSS Python's module.
    Source: https://github.com/BoboTiG/python-mss
'''

from mss.exception import ScreenshotError
from mss.factory import mss
from PIL import Image
import io

def main():
    # type: () -> int
    ''' PIL example using frombytes(). '''

    try:
        with mss() as sct:
            # We retrieve monitors informations:
            monitors = sct.enum_display_monitors()

            # Get rid of the first, as it represents the "All in One" monitor:
            for num, monitor in enumerate(monitors[1:], 1):
                # Get raw pixels from the screen.
                # This method will store screen size into `width` and `height`
                # and raw pixels into `image`.
                sct.get_pixels(monitor)

                # Create an Image:
                size = (sct.width, sct.height)
                img = Image.frombytes('RGB', size, sct.image)

		# TL;DR: sct.image is a unicode string. It has, at some point, been encoded from bytes. What format do I WANT it in? An array of array of bytes. Probably, array of bytesarrays.
		# Next question: WHY is it a string? Shouldn't it be an array of bytes?? Kinda weird.
		print(img)

		# METHODS OF ACCESSING INDIVIDUAL PIXELS
		# 1) img.getpixel (works)
		# 2) img.getdata (in documentation, not actually present on the PIL.Image module??)

            return 0
    except ScreenshotError as ex:
        print(ex)

    return 1


if __name__ == '__main__':
    exit(main())
