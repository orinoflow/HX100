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

#�������ļ���ŵ� filelines ��� list ��
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
            filelines.remove(line)	#������BUF�󣬽�BUF���ڵ���ɾ����
            find_buf = 1
            break  #��ǰ���������������һ��BUF���ڵ��У�������find_buf���˳�������ת���������������������BUF
        else:
            serial = 1
    if (find_buf == 0):  #�����������ļ���������û���ҵ�BUF����˵������buf���Ѿ��������˳������ѭ��
        break
        
    #ִ�е����˵���ҵ���һ��BUF������ķ�ʽ�ǽ����BUFɾ�����Ѿ���ǰ������������������Ȼ��
    #�������ļ���Ѱ�Һ����BUF��������ӵĽڵ㣬�ҵ��󣬰�����ڵ��������ӵ�ԭ�ȵ�BUF����˽ڵ�
    for line in filelines:  
        if (line.find(buffY) > 0):
            filelines[filelines.index(line)] = line.replace(buffY, buffA)
        
for line in filelines:
    outfile.write(line)
                
outfile.close()
infile.close()

print "rm buffer done!"

