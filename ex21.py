#!/usr/bin/python
# Title: Functions Can Return Something
# Author:lbli

def add ( a, b ):
    print "ADDING %d + %d" % ( a, b )
    return a + b

def subtract ( a, b ):
    print "SUBTRACT %d - %d" % ( a, b )
    return a - b

def multiply ( a, b ):
    print "MULTIPLY %d * %d" % ( a, b )
    return a * b

def divide ( a, b ):
    print "DIVIDE %d / %d" % ( a, b )
    return a / b

print "Let's do some math with just function!"

age = add ( 30, 5 )
height =  subtract ( 78, 4 )
weight = multiply ( 90, 2 )
iq = divide ( 100, 2 )

print "Age:%d,Height:%d,Weight:%d,IQ:%d" % ( age, height, weight, iq )

# A puzzle for the extra credit,type it in anyway.
print "Here is a puzzle."

what = add ( age,subtract ( height, multiply ( weight, divide ( iq, 2 ) ) ) )

print "THat beacome:", what, "Can dou do it by hannd?"
