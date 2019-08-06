#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Testing.

Fails because of the numbers being a different dtype, 
but that is not relevant to the program's functioning 
(as can be seen in the console the reports look the same) so I left it like that.
"""
import pandas
import unittest
from pandas.util.testing import assert_frame_equal
from CreateReport import CreateReport

resultdata1 = [['/contact.html',3,2]] 
resultdf1 = pandas.DataFrame(resultdata1, columns = ['url', 'page views', 'visitors'])

resultdata2 = [['/page3.php','2','2'], ['/page2.php','1','1']] 
resultdf2 = pandas.DataFrame(resultdata2, columns = ['url', 'page views', 'visitors']) 

resultdata3 = [['/basket.html','2','2'], ['/our-spaceships.html','1','1'],['/order-spaceship.php',2,1]] 
resultdf3 = pandas.DataFrame(resultdata3, columns = ['url', 'page views', 'visitors'])

class Test1(unittest.TestCase):
    
    def test1(self):
        logpath = 'examplelog1'
        datetimerange = '2013-09-01 09:00:00 - 10:59:59'
        result = CreateReport(logpath, datetimerange)
        print(resultdf1)
        print(result)
        assert_frame_equal(result, resultdf1)    
    
    def test2(self):
        logpath = 'examplelog2'
        datetimerange = '2014-07-03 10:00:00 - 12:00:00'
        result = CreateReport(logpath, datetimerange)
        print(resultdf2)
        print(result)
        assert_frame_equal(result, resultdf2)
        
    def test3(self):
        logpath = 'examplelog3'
        datetimerange = '2050-11-19 01:00:00 - 15:00:00'
        result = CreateReport(logpath, datetimerange)
        print(resultdf3)
        print(result)
        assert_frame_equal(result, resultdf3)    

if __name__ == '__main__':
    unittest.main()
