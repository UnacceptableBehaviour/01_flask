#! /usr/bin/env python

from pprint import pprint # giza a look

#from helpers import *
# call get_nutridata()
#
# or 
#
#import helpers
# call helpers.get_nutridata()

#from helpers import *
import helpers

def main():
    print(f"RUNNING TEST PEN")
    
    info = helpers.get_nutridata()
 
    #pprint(info)
 
    for k,v in info.items():        
        print(f"{ k } = { v }")
        
    print(f"__name__ is: {__name__}")
    print(f"__file__ is: {__file__}")
    print(f"__loader__ is: {__loader__}")
    print(f"__package__ is: {__package__}")
        
    info['n_EnkJ'] = str( round( float( info['n_En'] ) * 4.184 ) )
    info['serving_size'] = str( round( float( info['serving_size'] ) ) )
    
    print(f"n_EnkJ:       {info['n_EnkJ']}")
    print(f"serving_size: {info['serving_size']}")
    
    print(f"{1}")
    
    helpers.get_nutrients_per_serving()
    
    helpers.load_csv_data()
    

if __name__ == '__main__':
    main()                      # call main if this is being executed directly 
