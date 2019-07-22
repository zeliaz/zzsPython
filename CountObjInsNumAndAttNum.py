#!/usr/bin/env python
import os
import fileinput
import re

print "This is for counting instance number and attributes number in database.xml. Need InitClazzXref.h file and database.xml two files under D:\\"

# abstract all classref name strings from InitClazzXref_method.h
origClassFile = file('D:\InitClazzXref_method.h','r') # open for reading file
result = []
while True:
    lineInorigClassFile = origClassFile.readline()
    if len(lineInorigClassFile)==0:
        break
    it2 = 0
    it2 = re.finditer(r"(?<=\[ENB_)[^\]]+", lineInorigClassFile)
    for match in it2:
        result.append(match.group())
        print match.group()

origClassFile.close()

print "classRef number:"
print len(result)
#print result

# count number of object instances and number of attributes
ctClassRef = 0
ctSi = 0
databaseFile = file('D:\\database.xml','r')
countResult = [len(result)]
while True:
    lineInDatabaseFile = databaseFile.readline()
    if len(lineInDatabaseFile)==0:
        break
    m = 0
    for m in range(len(result)):
        ctClassRef += lineInDatabaseFile.count('</'+result[m])
    if not lineInDatabaseFile.count('</attributes>'):
            ctSi += lineInDatabaseFile.count('</')
databaseFile.close()

ctSi -= ctClassRef
#print "classRef in system is:"
#print  countResult

print '\n'
print "Object instance number is:"
print ctClassRef
print "attributes number is:"
print ctSi
