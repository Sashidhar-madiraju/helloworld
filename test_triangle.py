# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','201,201,201 should be Invalid input')
    
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,199,199),'InvalidInput','201,199,199 should be Invalid input')
    
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(199,201,199),'InvalidInput','199,201,199 should be Invalid input')
    
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(199,200,201),'InvalidInput','199,200,201 should be Invalid input')
    
    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(0,-1,1),'InvalidInput','0,-1,1 should be Invalid input')
    
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','5,3,4 is a Scalene triangle')
    
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,4),'Isoceles','3,4,4 is a Isoceles triangle')
    
    def testInvalidInputCharacters(self):
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','a,b,c should be Invalid input')
    
    def testInvalidInputCharactersA(self):
        self.assertEqual(classifyTriangle('a',1,2),'InvalidInput','a,1,2 should be Invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

