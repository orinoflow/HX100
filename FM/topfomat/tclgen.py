
# -*- coding: utf-8 -*
from sys import argv
from os.path import exists
import os
import sys

#tclgen需要完成的任务：
#   1，脚本固定部分的输出
#   2，set_user_match 端口部分，也是直接输出
#   3，set_user_match 寄存器部分，根据 lyt_top_tmp90.v 和 dxj_top_tmp90.v 搜索匹配
#   4，cutpoint 部分，根据 cutpointsoflyt.txt 中列出的CELL添加 cutpoints 并设置比较点

#########################################################################################
outfilename   = "fm_org.tcl"
print "output file is : ", outfilename
outfile = open(outfilename, 'w')

outfile.write("read_verilog -r ./dxj/dxj_lib_all.v\      \n")
outfile.write("read_verilog -r ./dxj/dxj_top_org.v\      \n")
outfile.write("set_top r:/WORK/dxj_top                   \n")
outfile.write("read_verilog -i ./lyt/lyt_lib_all.v\      \n")
outfile.write("read_verilog -i ./lyt/lyt_top_org.v       \n")
outfile.write("set_top i:/WORK/lyt_top                 \n\n")

outfile.write("set_constant  r:/WORK/dxj_top/VDD    1    \n")
outfile.write("set_constant  r:/WORK/dxj_top/GND    0    \n")

outfile.write("set_constant  i:/WORK/lyt_top/VDD    1    \n")
outfile.write("set_constant  i:/WORK/lyt_top/GND    0    \n")

########################################################################################
outfile.write("##########cutpoint 部分#############################################\n")
#   4，cutpoint 部分，根据 cutpointsoflyt.txt 中列出的CELL添加 cutpoints 并设置比较点
infilenamelyt = "lyt_top_tmp90.v"
infilenamedxj = "dxj_top_tmp90.v"
print "input file1 is : ", infilenamelyt
print "input file2 is : ", infilenamedxj
infile1lyt = open(infilenamelyt)
infile1dxj = open(infilenamedxj)

infilenamecutpoint = "../setcutpoints/cutpointsoflyt.txt"
infilecutpoint = open(infilenamecutpoint)
looplist = []
for line in infilecutpoint:
    looplist.append(line.replace("\n",""))
print looplist

for var in range (0,20000):
    linelyt = infile1lyt.readline() 
    linedxj = infile1dxj.readline()  
    wordslyt = linelyt.split()
    wordsdxj = linedxj.split()
    #print wordslyt
    #print wordsdxj
    if (len(wordslyt) >= 4):
        for varloop in looplist:
            if (wordslyt[2] == varloop):
            	  if ("_Y" in wordsdxj[4]):  #只有输出信号为 **_Y 的才被纳入cutpoint
		                print wordslyt
		                outfile.write("set_cutpoint  r:/WORK/dxj_top/" + wordsdxj[2] + "_Y \n")
		                outfile.write("set_cutpoint  i:/WORK/lyt_top/" + wordslyt[2] + "_Y \n")
		                outfile.write("set_user_match  r:/WORK/dxj_top/" + wordsdxj[2] + "_Y"   + "    i:/WORK/lyt_top/" + wordslyt[2] + "_Y \n")

infile1lyt.close()
infile1dxj.close()

########################################################################################
outfile.write("##########set_user_match 寄存器部分###############################\n")
#   3，set_user_match 寄存器部分，根据 lyt_top_tmp90.v 和 dxj_top_tmp90.v 搜索匹配
infile1lyt = open(infilenamelyt)
infile1dxj = open(infilenamedxj)

for var in range (0,20000):  #从0到扩展列表最后一项逐个循环
    linelyt = infile1lyt.readline() 
    linedxj = infile1dxj.readline()  
    wordslyt = linelyt.split()
    wordsdxj = linedxj.split()
    if (len(wordslyt) >= 4):
        if ((".Q(" in linelyt) and ("KC_TLAT_X3" not in linelyt)):
            outfile.write("set_user_match  r:/WORK/dxj_top/" + wordsdxj[2] + "/Q_reg_reg"  + "    i:/WORK/lyt_top/" + wordslyt[2] + "/Q_reg_reg"  + "\n")

########################################################################################
outfile.write("##########set_user_match 端口部分###############################\n")
#   2，set_user_match 端口部分，也是直接输出
outfile.write("set_user_match  r:/WORK/dxj_top/D11636_SN   i:/WORK/lyt_top/T13053_SN\n")
outfile.write("set_user_match  r:/WORK/dxj_top/D505_B      i:/WORK/lyt_top/T9218_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D540_GN     i:/WORK/lyt_top/T15168_CK\n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2636_B     i:/WORK/lyt_top/T9484_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2667_B     i:/WORK/lyt_top/T9495_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2668_B     i:/WORK/lyt_top/T9496_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2670_B     i:/WORK/lyt_top/T9493_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2671_B     i:/WORK/lyt_top/T9494_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D8695_A     i:/WORK/lyt_top/T2377_A  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D8696_A     i:/WORK/lyt_top/T2378_A  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9934_A     i:/WORK/lyt_top/T1845_A  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9942_A     i:/WORK/lyt_top/T1835_A  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9947_A     i:/WORK/lyt_top/T1855_A  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D11631_A    i:/WORK/lyt_top/T15190_A \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D11632_A    i:/WORK/lyt_top/T15167_A \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D12177_RN   i:/WORK/lyt_top/T1283_RN \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D13846_A    i:/WORK/lyt_top/T209_A   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D13859_A    i:/WORK/lyt_top/T15004_A \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15251_B    i:/WORK/lyt_top/T9198_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15252_B    i:/WORK/lyt_top/T9197_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16018_B    i:/WORK/lyt_top/T9214_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16019_B    i:/WORK/lyt_top/T9215_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16020_B    i:/WORK/lyt_top/T9216_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16021_B    i:/WORK/lyt_top/T9217_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16022_B    i:/WORK/lyt_top/T9209_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16023_B    i:/WORK/lyt_top/T9210_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16024_B    i:/WORK/lyt_top/T9211_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16025_B    i:/WORK/lyt_top/T9212_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16026_B    i:/WORK/lyt_top/T9213_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16027_B    i:/WORK/lyt_top/T9237_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16028_B    i:/WORK/lyt_top/T9236_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16029_B    i:/WORK/lyt_top/T9238_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16030_B    i:/WORK/lyt_top/T9250_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16031_B    i:/WORK/lyt_top/T9248_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16032_B    i:/WORK/lyt_top/T9206_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16033_B    i:/WORK/lyt_top/T9207_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16034_B    i:/WORK/lyt_top/T9205_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16035_B    i:/WORK/lyt_top/T9201_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16036_B    i:/WORK/lyt_top/T9208_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16037_B    i:/WORK/lyt_top/T9203_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16038_B    i:/WORK/lyt_top/T9204_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16039_B    i:/WORK/lyt_top/T9202_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16046_B    i:/WORK/lyt_top/T9249_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16073_B    i:/WORK/lyt_top/T9134_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16074_B    i:/WORK/lyt_top/T9499_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16075_B    i:/WORK/lyt_top/T9492_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16076_B    i:/WORK/lyt_top/T9491_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16081_B    i:/WORK/lyt_top/T9183_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16083_B    i:/WORK/lyt_top/T9084_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16084_B    i:/WORK/lyt_top/T9083_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16099_B    i:/WORK/lyt_top/T9179_B  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16138_AN   i:/WORK/lyt_top/T238_AN  \n")  
outfile.write("set_user_match  r:/WORK/dxj_top/D499_Y      i:/WORK/lyt_top/T5422_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D547_Y      i:/WORK/lyt_top/T16170_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2144_Y     i:/WORK/lyt_top/T4929_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2356_Y     i:/WORK/lyt_top/T4879_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9348_Y     i:/WORK/lyt_top/T2075_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9936_Y     i:/WORK/lyt_top/T1851_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9937_Y     i:/WORK/lyt_top/T1853_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9938_Y     i:/WORK/lyt_top/T1852_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9939_Y     i:/WORK/lyt_top/T1854_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9944_Y     i:/WORK/lyt_top/T1848_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9945_Y     i:/WORK/lyt_top/T1849_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9952_Y     i:/WORK/lyt_top/T15717_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9953_Y     i:/WORK/lyt_top/T15716_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9954_Y     i:/WORK/lyt_top/T6497_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10115_Y    i:/WORK/lyt_top/T15925_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10140_Y    i:/WORK/lyt_top/T1754_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10148_Y    i:/WORK/lyt_top/T1756_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10149_Y    i:/WORK/lyt_top/T1755_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10156_Y    i:/WORK/lyt_top/T1747_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10163_Y    i:/WORK/lyt_top/T1745_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10373_Y    i:/WORK/lyt_top/T845_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10660_Y    i:/WORK/lyt_top/T1616_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D12654_Y    i:/WORK/lyt_top/T1170_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D12655_Y    i:/WORK/lyt_top/T1169_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D12670_Y    i:/WORK/lyt_top/T1145_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D13153_Y    i:/WORK/lyt_top/T213_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D13155_Y    i:/WORK/lyt_top/T1023_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D13172_Y    i:/WORK/lyt_top/T1024_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14584_Y    i:/WORK/lyt_top/T586_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14585_Y    i:/WORK/lyt_top/T593_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14594_Y    i:/WORK/lyt_top/T11900_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14599_Y    i:/WORK/lyt_top/T16188_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14610_Y    i:/WORK/lyt_top/T141_Q   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D7464_Y     i:/WORK/lyt_top/T13264_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15245_Y    i:/WORK/lyt_top/T429_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15247_Y    i:/WORK/lyt_top/T428_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15442_Y    i:/WORK/lyt_top/T395_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16311_Y    i:/WORK/lyt_top/T199_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16403_Y    i:/WORK/lyt_top/T152_Y   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9951_Y     i:/WORK/lyt_top/T15718_Y \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9323_Q     i:/WORK/lyt_top/T16487_Q \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9353_Q     i:/WORK/lyt_top/T16488_Q \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9322_Q     i:/WORK/lyt_top/T16483_Q \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9318_Q     i:/WORK/lyt_top/T16486_Q \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9336_Q     i:/WORK/lyt_top/T2091_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9324_Q     i:/WORK/lyt_top/T16485_Q \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D9267_Y     i:/WORK/lyt_top/T2125_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D453_Y      i:/WORK/lyt_top/T5443_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D10164_Y    i:/WORK/lyt_top/T1746_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D13204_Y    i:/WORK/lyt_top/T1006_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2470_Y     i:/WORK/lyt_top/T4409_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16288_Q    i:/WORK/lyt_top/T211_Q   \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16404_Y    i:/WORK/lyt_top/T6359_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15710_Y    i:/WORK/lyt_top/T6417_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2686_Y     i:/WORK/lyt_top/T6730_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16300_Y    i:/WORK/lyt_top/T6425_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16371_Y    i:/WORK/lyt_top/T6364_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15956_Y    i:/WORK/lyt_top/T6432_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D15957_Y    i:/WORK/lyt_top/T6361_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D959_Y      i:/WORK/lyt_top/T6415_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16302_Y    i:/WORK/lyt_top/T6423_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16367_Y    i:/WORK/lyt_top/T6371_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D2687_Y     i:/WORK/lyt_top/T6479_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16401_Y    i:/WORK/lyt_top/T6358_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16301_Y    i:/WORK/lyt_top/T6424_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D16338_Y    i:/WORK/lyt_top/T6391_Q  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14774_Y    i:/WORK/lyt_top/T7899_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14810_Y    i:/WORK/lyt_top/T7815_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14759_Y    i:/WORK/lyt_top/T7811_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14773_Y    i:/WORK/lyt_top/T7853_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14771_Y    i:/WORK/lyt_top/T7854_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14772_Y    i:/WORK/lyt_top/T7859_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D14811_Y    i:/WORK/lyt_top/T7809_Y  \n")
outfile.write("set_user_match  r:/WORK/dxj_top/D3707_Y     i:/WORK/lyt_top/T16480_Q \n")

outfile.write("                                                           \n")                                 
outfile.write("match                                                      \n")
outfile.write("                                                           \n")
outfile.write("verify                                                     \n")
outfile.write("                                                           \n")
outfile.write("report_black_boxes > ./$report/syn_bb.rpt                  \n")
outfile.write("report_unmatched > ./$report/syn_unmatched.rpt             \n")
outfile.write("report_unmatched -status unread > ./$report/syn_unread.rpt \n")
outfile.write("report_failing_points > ./$report/syn_verify_result.rpt    \n")
outfile.write("report_aborted_points >> ./$report/syn_verify_result.rpt   \n")
outfile.write("report_passing_points > ./$report/syn_passing_points.rpt   \n")


infile1lyt.close()
infile1dxj.close()
outfile.close()

