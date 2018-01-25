from argmodule.ConfigReader  import ConfigReader
import importlib
import argparse

parser = argparse.ArgumentParser("description='Used to get configuration file path and configuration file type'")
parser.add_argument('--type','-t',required=True,help='Use to get configuration file type Need Type',dest='config_type')
parser.add_argument('--path','-p',required=True,help='Use to get configutaion file path',dest='config_path')
results = parser.parse_args()

print(results.config_path,results.config_type)

#configins = ConfigReader()
module = importlib.import_module('argmodule.ConfigReader')
my_class= getattr(module, 'ConfigReader')
my_instance = my_class()

func = getattr(my_instance,'readerINI','fun_when_not_find') 
func() 

def fun_when_not_find(self):
    print('Please provide a valid Type file to read ')
#def is_valid_type(parser,x):
#    lis = ['YAML','INI','JSON']
#    if (x in lis):
#        return(x)

