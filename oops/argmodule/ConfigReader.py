import configparser

class ConfigReader:

    def __init__(self):
        print('I am Getting initialized : ConfigReaderClass')

    def readerINI(self):
        print('I am reader for INI File')
        cp = configparser.ConfigParser() 
        cp.read('/Users/kalai/Documents/JupyterNotebook/data_utils/config_resource/sampleconfig.ini')
        for sec in cp.sections():
            print(sec)
            for opt in cp.options(sec):
                print(opt)
                print(cp.get(sec, opt))

    def readerYAML(self):
        print('I am reader for YAML File')

    def readerJSON(self):
        print('I am reader for JSON File')
