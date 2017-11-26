# -*- coding: utf-8 -*
from sys import argv
from os.path import exists

script, RLS_dxj_lyt = argv

#################################################################################################

#infilename = "../rmbuffer/"+RLS_dxj_lyt+"_top_rmbuf.v"
infilename = "../"+RLS_dxj_lyt+"_top_org.v"
outfilename = RLS_dxj_lyt+"CellCnt.txt"
print infilename
print outfilename

infile = open(infilename)
outfile = open(outfilename, 'w')

CellsInDesign = []
CellKinds = []
for line in infile:
    words = line.split()
    if (len(words) > 0) :
        #以下为原始分类
        CellsInDesign.append(words[0])
        #以下为不考虑驱动级别的分类
        #var = words[0]
        #CellsInDesign.append(var[0:-3])  # 0:-3表示截取从0到尾部倒数第三个字符
        
for Cell in CellsInDesign:
    if (Cell not in CellKinds):
        CellKinds.append(Cell) 

CellKinds.sort()
CellKinds.reverse()
        
for Cell in CellKinds:
    if ("KC_" in Cell):        
        print Cell + ' '*(20 - len(Cell)),
        print "  :  ",
        print CellsInDesign.count(Cell)
        outfile.write(Cell + ' '*(20 - len(Cell)) + "  :  " + str(CellsInDesign.count(Cell)) + "\n")

 

infile.close()
outfile.close()

raw_input()
