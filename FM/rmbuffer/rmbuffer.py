# -*- coding: utf-8 -*
from sys import argv
from os.path import exists
import os
import sys

script, RLS_dxj_lyt = argv

#################################################################################################
infilename = "../"+RLS_dxj_lyt+"_top_org.v"
outfilename = RLS_dxj_lyt+"_top_rmbuf.v"
print infilename
print outfilename

infile = open(infilename)
outfile = open(outfilename, 'w')

#将整个文件存放到 filelines 这个 list 中
filelines = []
for line in infile:
    filelines.append(line)

buffA = ""
buffY = ""

for i in range(10000):
    sys.stdout.write("\r  replace progress: %d  " % (i))
    sys.stdout.flush()
    find_buf = 0
    for line in filelines:
        words = line.split()
        if (len(words) <= 0) :
            serial = 1
        elif ("KC_BUF" in words[0]):
            for var in words:
                if ((".Y(" in var)) :
                    var = var[var.find('(')+1:var.find(')')]
                    buffY = var
                if ((".A(" in var)) :
                    var = var[var.find('(')+1:var.find(')')]
                    buffA = var
            filelines.remove(line)	#搜索到BUF后，将BUF所在的行删除！
            find_buf = 1
            break  #从前向后搜索，遇到第一个BUF所在的行，则做好find_buf后退出搜索，转到后续处理这个搜索到的BUF
        else:
            serial = 1
    if (find_buf == 0):  #如果完成整个文件的搜索都没有找到BUF，则说明所有buf都已经被处理，退出最外层循环
        break
        
    #执行到这里，说明找到了一个BUF，处理的方式是将这个BUF删除（已经在前面完成了这个动作），然后
    #在整个文件中寻找和这个BUF输出相连接的节点，找到后，把这个节点重新连接到原先的BUF输入端节点
    for line in filelines:  
        if (line.find(buffY) > 0):
            filelines[filelines.index(line)] = line.replace(buffY, buffA)
        
for line in filelines:
    outfile.write(line)
                
outfile.close()
infile.close()

print "rm buffer done!"

