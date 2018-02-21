'''
Created on 6 Feb 2018

@author: Pavinee Kavanagh comp30670
'''
import platform

def get_platform(): 
    s = "Platform is: {}".format(platform.platform())
    return s


if __name__ == '__main__':
    print(get_platform())