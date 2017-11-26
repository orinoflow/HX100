# -*- coding: utf-8 -*
from sys import argv
from os.path import exists

script, RLS_dxj_lyt = argv

#################################################################################################
infilename = "../"+RLS_dxj_lyt+"_lib_all.v"
outfilename = RLS_dxj_lyt+"_lib_new.v"
print infilename
print outfilename

input1 = open(infilename)
output = open(outfilename, 'w')

#文件读出以后，按行循环
CellsInDesign = []
CellKinds = []
for line in input1:
    words = line.split()      
    if (len(words) <= 0) :
        serial = 1
    elif ("//" in words[0]):
        serial = 1
    elif ("timescale" in words[0]):
        serial = 1
    elif ("output" in words[0]):
        serial = 1
    elif ("input" in words[0]):
        serial = 1
    elif ("wire" in words[0]):
        serial = 1
    elif ("module" == words[0]):
        mod = []
        line = line.replace(")", " ")
        line = line.replace(",", " ")
        line = line.replace("(", " ")
        line = line.replace(";", " ")
        words = line.split()  
        mod.append(words[0])
        mod.append(words[1])
        del words[0]
        del words[0]
        words.sort()
        words.reverse()
        #print mod[0] + " " + mod[1] + " " + "( ",
        output.write(mod[0] + " " + mod[1] + " " + "( ")
        tmpi = 0
        for var in words:
            tmpi = tmpi+1
            #print var,
            output.write(var)
            if (tmpi != len(words)):
                #print ",",
                output.write(",")
        #print ");"
        output.write(");" + "\n")
        if ("Y" in words):
            #print "    output Y;"
            output.write("    output Y;" + "\n")
        if ("QN" in words):
            #print "    output reg QN;"
            output.write("    output reg QN;" + "\n")
        if ("Q" in words):
            #print "    output reg Q;"
            output.write("    output reg Q;" + "\n")
        if ("S" in words):
        	  #print "    output S;"
        	  output.write("    output S;" + "\n")
        	  
              
    else:
        #print "    " + line,
        output.write("    " + line)
        serial = 1
 
output.close()
input1.close()

print "lib fomat done!"

