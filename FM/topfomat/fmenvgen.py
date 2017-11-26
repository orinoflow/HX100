# -*- coding: utf-8 -*
from sys import argv
from os.path import exists
import os
import sys
import os.path 
import shutil 
import time,  datetime

def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print path+' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
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
            
# 定义要创建的目录
mkpath=".\\V5"
# 调用函数
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
#    for line in infile:  #对文件逐行循环
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
#    for line in infile:  #对文件逐行循环
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
