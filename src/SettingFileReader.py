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



from ConfigParser import *

class SettingFileReader:

    # default file address
    _fileName = 'settings/settings.ini'

    # parser object
    _parser = None


    # constructor
    def __init__(self, fileAdress = None):

        if(fileAdress):
            self._fileName = fileAdress

        self._parser = SafeConfigParser()
        self._parser.read(self._fileName)



    # Returns a param value giving its name and groupname
    def getSetting(self, group, name):

        settingValue = self._parser.get(group, name)

        # trying to cast to number
        try:
            # cast to float
            settingValue = float(settingValue)

            # if interger, cast to integer
            if(settingValue.is_integer()):
                settingValue = int(settingValue)
            else:
                None

        except ValueError as e:
            None

        return settingValue

    # return an array of all the tuples like (paramName : ParamValue)
    # present in the group of param
    def getItems(self, group):
        return self._parser.items(group)


    # update a param value within the setting.ini file.
    # if the param or group does not exist, it will be created
    def setSetting(self, group, name, value):
        self._parser.set(group,name, value)

        with open(self._fileName, 'wb') as configfile:
            self._parser.write(configfile)
