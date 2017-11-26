# -*- coding: utf-8 -*
from sys import argv
from os.path import exists
import os
import sys
import os.path 
import shutil 
import time,  datetime

def mkdir(path):
    # ����ģ��
    import os
    # ȥ����λ�ո�
    path=path.strip()
    # ȥ��β�� \ ����
    path=path.rstrip("\\")
    # �ж�·���Ƿ����
    # ����     True
    # ������   False
    isExists=os.path.exists(path)
    # �жϽ��
    if not isExists:
        # ����������򴴽�Ŀ¼
        # ����Ŀ¼��������
        os.makedirs(path) 
 
        print path+' �����ɹ�'
        return True
    else:
        # ���Ŀ¼�����򲻴���������ʾĿ¼�Ѵ���
        print path+' Ŀ¼�Ѵ���'
        return False
        
def copyFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                    open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)
            
# ����Ҫ������Ŀ¼
mkpath=".\\V5"
# ���ú���
if (mkdir(mkpath)):
    copyFiles("../fmenvref", "./V5")
    shutil.copy('./fm_org.tcl', './V5/fm_org.tcl')
    
#    #################################################
#    infilename = "../dxj_top_org.v"
#    outfilename = "./V5/dxj/dxj_top_org.v"
#    print "input  file is : ", infilename
#    print "output file is : ", outfilename
#
#    infile = open(infilename)
#    outfile = open(outfilename, 'w')         
#
#    for line in infile:  #���ļ�����ѭ��
#        outfile.write(line)
#    outfile.close()
#    infile.close()
#
#
#    #################################################
#    infilename = "../lyt_top_org.v"
#    outfilename = "./V5/lyt/lyt_top_org.v"
#    print "input  file is : ", infilename
#    print "output file is : ", outfilename
#
#    infile = open(infilename)
#    outfile = open(outfilename, 'w')         
#
#    for line in infile:  #���ļ�����ѭ��
##        if ("KC_INV_X1 T5735 ( .Y(T5735_Y), .A(T10536_Y));" in line):
##            print "replace line : KC_INV_X1 T5735 ( .Y(T5735_Y), .A(T10536_Y));"
##            outfile.write("//KC_INV_X1 T5735 ( .Y(T5735_Y), .A(T10536_Y));\n")
##            outfile.write("KC_INV_X1        T5735     ( .Y(T5735_Y)     , .A(T15689_Y)    );\n")
##        elif ("KC_AOI21B_X2 T10537 ( .A0(T15689_Y), .BN(T10536_Y), .Y(T10537_Y),     .A1(T2649_Y));" in line):
##            print "replace line : KC_AOI21B_X2 T10537 ( .A0(T15689_Y), .BN(T10536_Y), .Y(T10537_Y),     .A1(T2649_Y));"
##            outfile.write("//KC_AOI21B_X2 T10537 ( .A0(T15689_Y), .BN(T10536_Y), .Y(T10537_Y),     .A1(T2649_Y));\n")
##            outfile.write("KC_AOI21B_X2     T10537    ( .Y(T10537_Y)    , .A1(T2649_Y)    , .A0(T15689_Y)   , .BN(T15689_Y)   );\n")
##        else:
#            outfile.write(line)
#    outfile.close()
#    infile.close()
