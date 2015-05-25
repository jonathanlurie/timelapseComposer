# Timelapse Composer

Creates a timelapse sequence from jpg images.

## Features

- codecs : x264, mpeg4, uncompressed, png, vorbis, vpx
- Chose the output size
- Chose the framerate
- Chose the bitrate (x264 only)

## How to use
Launch with a double-click on `TimelapseComposer.sh` , then the GUI will display.  

![](https://www.dropbox.com/s/4kcdnzu74ald82b/timelapsecomposer.png?dl=0&raw=1) 

Only the `input` setting is necessary : chose a random jpeg file from your sequence, this will help TC to know where to find the files. Then **all the jpeg files from the same folder** will be used to make the sequence.  

`output` is the name of the output file, without extension. The default name is *out* and its extension depends on the chosen codec. The output file will be written in the input directory.

## Compatibilities
TC was developed on MacOSX 10.10 using Python 2.7. It should run on other Unix platforms without any edit.

## Dependencies

**Embedded**  
The core of Timelapse Composer is based on [MoviePy](https://github.com/Zulko/moviepy) and the GUI is automatically built thanks to [Gooey](https://github.com/chriskiehl/Gooey). Those libraries are already embedded in TC so you don't need to bother about them.

**To install**  
Since Gooey uses [wxPython](http://www.wxpython.org/), you might need to install it first.

# Licence
MIT, see LICENCE.txt for more info.