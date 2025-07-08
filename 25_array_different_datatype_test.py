from array import *

print("Example of unsigned integer:->")
mark = array('I',[88,56,68,90,67]) #here I represnt array of unsigned integer only support positive number
print(mark)

print("Example of signed integer:->")
mark = array('i',[88,56,68,-90,67]) #here i represnt array of signed integer support both positive and negative number
print(mark)

print("Example of short unsigned integer:->")
mark = array('H',[88,56,68,90,67]); #here H represnt array of short unsigned integer only support positive number
print(mark);

print("Example of short signed integer:->")
mark = array('h',[88,56,-68,90,67]); #here h represnt array of short signed integer support both positive and negative number 
print(mark);

print("Example of unsigned long integer:->")
mark = array('L',[8458,5634,6845,9033,6457]); #here L represnt array of long unsigned integer only support positive number
print(mark);

print("Example of signed long integer:->")
mark = array('l',[8458,-5634,6845,9033,6457]); #here l represnt array of long signed integer support both positive and negative number
print(mark);

print("Example of unsigned long long integer:->")
mark = array('Q',[845118,562234,682245,903333,645557]); #here Q represnt array of long long unsigned integer support only positive number
print(mark);

print("Example of signed long long integer:->")
mark = array('q',[845118,-562234,682245,903333,645557]); #here q represnt array of long long signed integer support both positive and negative number
print(mark);

print("Example of float :->")
mark = array('f',[8458.56,-5634.45,6845,9033,6457]); #here f represnt array of float support both positive and negative number
print(mark);

print("Example of double :->")
mark = array('d',[8458.56,-5634.45,6845,9033,6457]); #here d represnt array of double support both positive and negative number
print(mark);

print("Example of unicode character :->")
name = array('u',['b','h','u','s','h','a','n']) #here u represnt array of character
print(name)