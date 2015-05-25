"""
The MIT License (MIT)

Copyright (c) 2015 Jonathan Lurie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import glob
import argparse
import os
import datetime
import sys



from gooey import Gooey, GooeyParser


from SettingFileReader import *
import Utils




@Gooey(advanced=True , show_config=True, program_name='Timelapse Composer', default_size=(600, 500), required_cols=1, optional_cols=1, dump_build_config=False )
def main():

    # get some default settings from setting file
    settings = SettingFileReader()
    defaultOutput = settings.getSetting("defaultSettings", "output")
    defaultWidth = settings.getSetting("defaultSettings", "width")
    defaultFramerate = settings.getSetting("defaultSettings", "framerate")
    defaultBitrateKb = settings.getSetting("defaultSettings", "bitratekb")
    description = settings.getSetting("defaultSettings", "description")



    codecList = ["libx264", "mpeg4", "rawvideo", "png", "libvorbis", "libvpx"]
    codecDesc = ["libx264 : default codec, lossy compression", "mpeg4 : higher quality", "rawvideo : perfect quality, huge size ", "png : perfect quality, reasonable size", "libvorbis : good quality, rare codec ", "libvpx : good for the Web"]
    codecExt  = [".mp4", ".mp4", ".avi", ".avi", ".ogv", ".webm"]

    # dealing with the parser
    parser = GooeyParser(description=description)
    parser.add_argument('-input', required=True, type=argparse.FileType('r'), help='A jpeg file from the sequence' , widget="FileChooser")
    parser.add_argument('-output', required=False, default=defaultOutput, help='Output sequence file name (default : ' + defaultOutput + '). The file will be saved in the input folder.' )
    parser.add_argument('-codec', choices=codecList, help=" - ".join(codecDesc) + " (default : libx264)", default=codecList[0])
    parser.add_argument('-width', required=False, default=defaultWidth, type=int, help='Width of the output sequence in pixels (default : ' + str(defaultWidth) + ')' )
    parser.add_argument('-height', required=False, type=int, help='height of the output sequence in pixels (default : keeps proportions to width)' )
    parser.add_argument('-framerate', required=False, default=defaultFramerate, type=int, help='Number of frame per second of the output sequence (default : ' + str(defaultFramerate) + ')' )
    parser.add_argument('-bitrate', required=False, default=defaultBitrateKb, type=int, help='Bitrate of the output sequence in kb/s (default : ' + str(defaultBitrateKb) + 'kb/s). Only compatible with libx264 codec.' )

    args = parser.parse_args()

    '''
    print args.input.name
    print args.output
    print args.width
    print args.height
    print args.framerate
    print args.bitrate
    print args.codec
    '''

    # getting all the jpg from this folder
    imgFolder = Utils.getFolderName(args.input.name)
    imgExt = Utils.getFileExt(args.input.name)

    print("Folder :")
    print("\t" + imgFolder + "\n")
    print("Image extension :")
    print("\t" + imgExt + "\n")
    print("Looking for files...")

    # looking for files
    jpgList = sorted(glob.glob( imgFolder + os.sep + '*' + imgExt))

    print("\t" + str(len(jpgList)) + " files where found.\n")

    if(len(jpgList) == 0):
        print("ERROR : unable to continue, 0 image files where found.")
        exit()

    # importing moviepy
    try:
        from moviepy.editor import *

        # getting codec info
        codecIndex = codecList.index(args.codec)
        outputExtension = codecExt[codecIndex]

        outputFile = imgFolder + os.sep  + args.output + outputExtension

        print("Codec :")
        print("\t" + args.codec + "\n")
        print("output file :")
        print("\t" + outputFile + "\n")

        tl = ImageSequenceClip(jpgList, fps=args.framerate)

        # dealing with image proportions
        if(args.height):
            tlhd = tl.resize(width=args.width, height=args.height)
        else:
            tlhd = tl.resize(width=args.width)

        bitrate = str(args.bitrate * 1024)

        a = datetime.datetime.now()
        tlhd.write_videofile(outputFile, codec=args.codec , fps=args.framerate, bitrate=bitrate, threads=2, write_logfile=True)
        b = datetime.datetime.now()

        print("Processing time : " + str( (b-a).seconds) + " seconds")

    # iport failled
    except ImportError:
        print("ERROR : impossible to import Moviepy module.")




if __name__ == '__main__':
    # prioritize the local libraries in case of doubt
    sys.path.insert(0, "./lib/python")

    main()
