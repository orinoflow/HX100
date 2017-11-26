
# -*- coding: utf-8 -*
from sys import argv
from os.path import exists
import os
import sys

#################################################################################################
#cutpoints 要加在loop起点以及所有loop分叉的地方，
####

infilename = "loopsoflyt.txt"
outfilename = "cutpointsTmp.txt"

print "input file1 is : ", infilename
print "output file is : ", outfilename

infile = open(infilename)
outfile = open(outfilename, 'w')

looppointsflag = 0
branchcnt = 0
branchline = ""

for var in range (0,780000):
    line = infile.readline() 
    words = line.split()
    #print words
#    if (len(words) >= 2):   #loop起点处理部分
#        if (("Loop" in line) and (looppointsflag == 0)):
#            loopserial = line.replace("\n", "")
#            looppointsflag = 1
#            continue
#        if (("_Y" in line) and (looppointsflag == 1)):
#            if ("_Y" in line):
#                looppointsflag = 0
#                #outfile.write(line.replace("\n", "") + "  " + loopserial + "\n")
#                outfile.write(line)
    if (len(words) >= 2):   #loop分叉处理部分
#        if ("Loop" in line):
#            outfile.write(line)
        if ("==>" not in line):
            if (branchcnt >= 2):
                if ("_Y" in branchline):
                    outfile.write(branchline)
            branchline = line
            branchcnt = 0
        else:
            branchcnt = branchcnt + 1
            
infile.close()
outfile.close()

#################################################################################################

infilename = "cutpointsTmp.txt"
outfilename = "cutpointsoflyt.txt"

print "input file1 is : ", infilename
print "output file is : ", outfilename

infile = open(infilename)
outfile = open(outfilename, 'w')

cutpointlist = []
for line in infile:
    #print "line : " + line 
    #print cutpointlist
    if (line not in cutpointlist):
        cutpointlist.append(line)
        #print "here"

for var in range(len(cutpointlist)):
    words = cutpointlist[var].split()
    #print words[1]
    words[1] = words[1].replace("i:/WORK/lyt_top/", "")
    words[1] = words[1].replace("_Y", "")
    outfile.write(words[1] + "\n")
    
infile.close()
outfile.close()
os.remove(infilename)
