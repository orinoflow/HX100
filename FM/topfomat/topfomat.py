# -*- coding: utf-8 -*
from sys import argv
from os.path import exists
import os
import sys

script, RLS_dxj_lyt, expmod, thecellname = argv

if (expmod == "singlecell") or (expmod == "allport"):
    #################################################################################################
    #��һ�����ȶ����е�������Ϣ(Ҳ���ǵ���������Ϣ)�������򣬰�����ŵ���һ���������밴��ĸ��������
    #infilename = "../"+RLS_dxj_lyt+"_top_org.v"
    infilename = "../rmbuffer/"+RLS_dxj_lyt+"_top_rmbuf.v"
    outfilename = RLS_dxj_lyt+"_top_tmp1.v"
    print "input  file is : ", infilename
    print "output file is : ", outfilename

    infile = open(infilename)
    outfile = open(outfilename, 'w')

    #2�������������Ҳ���ǵ�������������������һ�׶ε�����ļ��� dxj/lyt_top_tmp1.v
    #   ���磺
    #   C_OAI22_X3      T16170  ( .A1(T1352_Y)   , .B0(T5307_Y)   , .B1(T9166_Y)   , .A0(T5335_Y)   , .Y(T16170_Y)   );
    #   ������Ϊ��
    #   KC_OAI22_X3     T16170  ( .Y(T16170_Y)   , .B1(T9166_Y)   , .B0(T5307_Y)   , .A0(T5335_Y)   , .A1(T1352_Y)   );
    #   ������������ͬʱ�������е�������¼�����������
    #   1������Գƹܽ�˳�����
    #   2��������ǶʽINVERTER�Ĳ��
    #   3��������CELL�Ĳ��
    #   

    def exchange_2_ports_of_ref(dxj_or_lyt, ref_name, port1, port2):
        if (RLS_dxj_lyt == dxj_or_lyt):
            if (mod[0] == ref_name):
                words[port1],words[port2] = words[port2],words[port1]   #�±��Ӧ��Ҫ������Ԫ�أ�Ҳ��������ܽ���ţ�(�������)��������
                
    def exchange_3_ports_of_ref(dxj_or_lyt, ref_name, port1, port2, port3, port4):
        if (RLS_dxj_lyt == dxj_or_lyt):
            if (mod[0] == ref_name):
                words[port1],words[port2] = words[port2],words[port1]   #�±��Ӧ��Ҫ������Ԫ�أ�Ҳ��������ܽ���ţ�(�������)��������
                words[port3],words[port4] = words[port4],words[port3]   #�±��Ӧ��Ҫ������Ԫ�أ�Ҳ��������ܽ���ţ�(�������)��������
                
    def exchange_4_ports_of_ref(dxj_or_lyt, ref_name, port1, port2, port3, port4, port5, port6):
        if (RLS_dxj_lyt == dxj_or_lyt):
            if (mod[0] == ref_name):
                words[port1],words[port2] = words[port2],words[port1]   #�±��Ӧ��Ҫ������Ԫ�أ�Ҳ��������ܽ���ţ�(�������)��������
                words[port3],words[port4] = words[port4],words[port3]   #�±��Ӧ��Ҫ������Ԫ�أ�Ҳ��������ܽ���ţ�(�������)��������
                words[port5],words[port6] = words[port6],words[port5]   #�±��Ӧ��Ҫ������Ԫ�أ�Ҳ��������ܽ���ţ�(�������)��������
                
                
    def extract_1_inner_inv_of_ref(dxj_or_lyt, ref_name, inv_port, inv_pin_name):
        if (RLS_dxj_lyt == dxj_or_lyt):
            if (mod[0] == ref_name):
                mod[0] = mod[0]+"_W"      #�̶�����
                invCell = mod[1]+"_INV"                 #�̶����䣬��ʾ�������ķ�����CELL����
                invwire = words[inv_port]               #�±��ʾ��Ҫ����������������ܽ���ţ���0����
                invwire = invwire.replace(inv_pin_name, "")   #�±��Ϊ��Ҫ����������������ܽ�����
                invwire = invwire.replace(")", "")      #�̶�����
                if (inv_port > 0):
                    tmpstr = "KC_INV_W %s ( .Y(%s_W) , .A(%s) );\n"%(invCell,invwire,invwire)     #�̶�����
                else:
                    tmpstr = "KC_INV_W %s ( .Y(%s) , .A(%s_W) );\n"%(invCell,invwire,invwire)     #�̶�����
                outfile.write(tmpstr)     #�̶�����
                words[inv_port] = words[inv_port].replace(")","_W)")  #�±��ʾ��Ҫ����������������ܽ���ţ���0����
            
    def extract_2_inner_inv_of_ref(dxj_or_lyt, ref_name, inv_port1, inv_pin_name1, inv_port2, inv_pin_name2):
        if (RLS_dxj_lyt == dxj_or_lyt):
            if (mod[0] == ref_name):
                mod[0] = mod[0]+"_W"      #�̶�����
                
                invCell1 = mod[1]+"_INV1"  #�̶����䣬��ʾ�������ķ�����CELL����
                invwire1 = words[inv_port1]        #�±��ʾ��Ҫ����������������ܽ���ţ���0����
                invwire1 = invwire1.replace(inv_pin_name1, "")  #�±��Ϊ��Ҫ����������������ܽ�����
                invwire1 = invwire1.replace(")", "")     #�̶�����
                tmpstr1 = "KC_INV_W %s ( .Y(%s_W) , .A(%s) );\n"%(invCell1,invwire1,invwire1)     #�̶�����
                outfile.write(tmpstr1)     #�̶�����
                words[inv_port1] = words[inv_port1].replace(")","_W)")  #�±��ʾ��Ҫ����������������ܽ���ţ���0����
                
                invCell2 = mod[1]+"_INV2"  #�̶����䣬��ʾ�������ķ�����CELL����
                invwire2 = words[inv_port2]       #�±��ʾ��Ҫ����������������ܽ���ţ���0����
                invwire2 = invwire2.replace(inv_pin_name2, "")  #�±��Ϊ��Ҫ����������������ܽ�����
                invwire2 = invwire2.replace(")", "")     #�̶�����
                tmpstr2 = "KC_INV_W %s ( .Y(%s_W) , .A(%s) );\n"%(invCell2,invwire2,invwire2)     #�̶�����
                outfile.write(tmpstr2)     #�̶�����            mod[0] = mod[0]+"_W"     #�̶�����
                words[inv_port2] = words[inv_port2].replace(")","_W)")  #�±��ʾ��Ҫ����������������ܽ���ţ���0����
            
    for line in infile:
        words = line.split()
        if (len(words) <= 0) :
            serial = 1
        elif ("KC_" in words[0]):
            mod = []
            line = line.replace(",", " ")
            line = line.replace(";", " ")
            line = line.replace("))", ")")
            words = line.split()
            

            mod.append(words[0])
            mod.append(words[1])
            del words[0]
            del words[0]
            words.remove("(")
            words.sort()
            words.reverse()

            #������󣬴��������ײ�LIB CELL��һ������
            extract_1_inner_inv_of_ref("dxj", "KC_NOR3B_X1", 1, ".CN(")
            
            exchange_2_ports_of_ref("lyt", "KC_AND2B_X2", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_TINV_X2", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_AND2B_X1", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_MXI2B_X4", 2, 3)
            exchange_2_ports_of_ref("lyt", "KC_ADD_C_X1", 1, 3)
            exchange_2_ports_of_ref("lyt", "KC_OAI211B_X1", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_OAI22_X3", 3, 4)
            exchange_2_ports_of_ref("lyt", "KC_XNOR2_X1", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_DFFRNHQ_X3", 2, 3)
            exchange_2_ports_of_ref("lyt", "KC_DFFSNHQ_X3", 2, 3)
            exchange_2_ports_of_ref("lyt", "KC_TLAT_X2", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_AND2_X3", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_AO12B_X1", 2, 3)
            exchange_2_ports_of_ref("lyt", "KC_XOR2_X4", 1, 2)
            exchange_2_ports_of_ref("lyt", "KC_OAI22_X2", 2, 4)
            
            exchange_2_ports_of_ref("lyt", "KC_ADD_C_B_X1", 1, 3)
            exchange_2_ports_of_ref("lyt", "KC_XNOR2_X4", 1, 2)
            
            exchange_3_ports_of_ref("lyt", "KC_AOI21BB_X1", 1, 3, 2, 1)
            exchange_3_ports_of_ref("lyt", "KC_AOI21B_X2", 1, 3, 2, 1)
            exchange_3_ports_of_ref("lyt", "KC_OAI21_X1", 1, 3, 2, 1)
            exchange_3_ports_of_ref("lyt", "KC_AOI21_X1", 1, 3, 2, 1)
            exchange_3_ports_of_ref("lyt", "KC_DFFRNHQ_X4", 1, 3, 2, 3)
            
            exchange_4_ports_of_ref("lyt", "KC_OAI13_X3", 1, 4, 2, 4, 3, 4)

            extract_1_inner_inv_of_ref("lyt", "KC_AOI22B_X2", 4, ".A0N(")
            extract_1_inner_inv_of_ref("lyt", "KC_NAND3BB_X1", 2, ".BN(")
            extract_1_inner_inv_of_ref("lyt", "KC_NOR2B_X2", 2, ".AN(")
            extract_1_inner_inv_of_ref("lyt", "KC_OAI211B_X2", 4, ".AN(")
            extract_1_inner_inv_of_ref("lyt", "KC_OAI112B_X2", 4, ".AN(")
            extract_1_inner_inv_of_ref("lyt", "KC_AOI112B_X1", 1, ".C1N(")
            extract_1_inner_inv_of_ref("lyt", "KC_NOR3B_X1", 1, ".CN(")
            extract_1_inner_inv_of_ref("lyt", "KC_NOR2B_X4", 2, ".AN(")
            extract_1_inner_inv_of_ref("lyt", "KC_OAI21B_X3", 1, ".BN(")
            extract_1_inner_inv_of_ref("lyt", "KC_NAND3B_X2", 1, ".CN(")
            extract_1_inner_inv_of_ref("lyt", "KC_OAI112B_X1", 3, ".BN(")
            extract_2_inner_inv_of_ref("lyt", "KC_AOI22BB_X1", 2, ".B0N(", 4, ".A0N(")
            extract_2_inner_inv_of_ref("lyt", "KC_AOI21BB_X1", 1, ".A1N(", 3, ".BN(")

            extract_2_inner_inv_of_ref("lyt", "KC_OAI112BB_X1", 2, ".C0N(", 4, ".AN(")

            if (RLS_dxj_lyt == "lyt"):
                #�������ĳ��������Ԫ�ľ���������Ҫ����˳�����಻��Ҫ��һ����˵����Ӧ���ǶԳƵ�Ԫ��Ԫ�ĶԳƹܽ�
                if (mod[1] == "T233"):  
                    exchange_2_ports_of_ref("lyt", "KC_XNOR2_X8", 1, 2)
                if (mod[1] == "T2347"):
                    exchange_3_ports_of_ref("lyt", "KC_AOI21B_X1", 2, 3, 1, 3)
                    extract_1_inner_inv_of_ref("lyt", "KC_AOI21B_X1", 2, ".A0N(")
                if (mod[1] == "T16128"):
                   extract_1_inner_inv_of_ref("lyt", "KC_OA22_X1", 0, ".Y(")
                if (mod[1] == "T15898"):
                    extract_1_inner_inv_of_ref("lyt", "KC_OA22_X1", 0, ".Y(")
#                if ((mod[1] == "T15992") or (mod[1] == "T15874") or (mod[1] == "T15927") or (mod[1] == "T15915")): 
#                    exchange_2_ports_of_ref("lyt", "KC_ADD_C_B_X1", 1, 3)
#                if (mod[1] == "T12460"): 
#                    exchange_2_ports_of_ref("lyt", "KC_XNOR2_X4", 1, 2)
                if (mod[1] == "T15759"):  #KC_AO12B_X1 T15759 ( .Y(T15759_Y), .B(T13324_Q), .A(T11680_Y),     .C(T4738_Y));
                    outfile.write("KC_NAND2_X1_W     T15759_W1     ( .Y(T15759_Y)    , .B(T4738_Y)     , .A(T15759_Y_W)    );\n")
                    outfile.write("KC_NAND2_X1_W     T15759_W2     ( .Y(T15759_Y_W)    , .B(T11680_Y)     , .A(T13324_Q)    );\n")
                    continue
                if (mod[1] == "T8398"):
                    exchange_3_ports_of_ref("lyt", "KC_OA21_X1", 1, 3, 1, 2)
                    extract_1_inner_inv_of_ref("lyt", "KC_OA21_X1", 0, ".Y(")
                if (mod[1] == "T8317"):
                    #KC_OR4_X1        T8317     ( .Y(T8317_Y)     , .D(T8240_Y)     , .C(T8473_Y)     , .B(T8328_Y)     , .A(T8343_Y)     );
                    outfile.write("KC_NAND2_X1      T8317     ( .Y(T8317_Y)        , .B(T8317_Y_W1)  , .A(T8317_Y_W2)  );\n")
                    outfile.write("KC_NOR2_X1       T8317_W1  ( .Y(T8317_Y_W1)     , .B(T8240_Y)     , .A(T8473_Y)     );\n")
                    outfile.write("KC_NOR2_X1       T8317_W2  ( .Y(T8317_Y_W2)     , .B(T8328_Y)     , .A(T8343_Y)     );\n")
                    continue

                  
                #    T16080 
                #    T8398
                
            if (RLS_dxj_lyt == "dxj"):
                #����CELL���
                #KC_OA12B_X1
                if ("KC_MX2_X3" in mod[0]):  #
                    #print words  #['.Y(T8638_Y)', '.D1(T288_Q)', '.D0(T12440_Y)', '.C1(T5241_Q)', '.C0(T12411_Y)', '.B1(T5226_Q)', '.B0(T12413_Y)', '.A1(T293_Q)', '.A0(T12412_Y)']
                    strY  = words[0][words[0].find('(')+1:words[0].find(')')]
                    strY1 = mod[1]+"L1"  #��ֵ�Ԫ���ڲ�����
                    strC = words[1][words[1].find('(')+1:words[1].find(')')] #S0
                    strB = words[2][words[2].find('(')+1:words[2].find(')')] #B
                    strA = words[3][words[3].find('(')+1:words[3].find(')')] #A
                    strCellname = mod[1]
                    #print strCellname
                    tmpstr1 = "KC_XNOR2_X1     %s     ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY, strY1,strB)
                    tmpstr2 = "KC_XNOR2_X1     %s_W1  ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY1,strC, strA)
                    outfile.write(tmpstr1)
                    outfile.write(tmpstr2)
                    continue
                
            if (RLS_dxj_lyt == "lyt"):
                #����CELL���
                if ("KC_AO12B_X2" in mod[0]):  #
                    strY1 = mod[1]+"L1"  #��ֵ�Ԫ���ڲ�����
                    strY = words[0][words[0].find('(')+1:words[0].find(')')]
                    strC = words[1][words[1].find('(')+1:words[1].find(')')]
                    strB = words[2][words[2].find('(')+1:words[2].find(')')]
                    strA = words[3][words[3].find('(')+1:words[3].find(')')]
                    strCellname = mod[1]
                    #print strCellname
                    tmpstr1 = "KC_NAND2_X3     %s     ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY,strC,strY1)
                    tmpstr2 = "KC_NAND2_X1     %s_W1  ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY1,strB,strA)
                    outfile.write(tmpstr1)
                    outfile.write(tmpstr2)
                    continue
                #KC_ADDH_X1
                if ("KC_ADDH_X1" in mod[0]):  #KC_ADDH_X1 T9142 ( .S(T9142_S), .Co(T9142_Co),     .B(T9141_Co), .A(T5406_Q));
                    #print words
                    strY = words[0][words[0].find('(')+1:words[0].find(')')]
                    strY1 = mod[1]+"L1"  #��ֵ�Ԫ���ڲ�����
                    strC = words[1][words[1].find('(')+1:words[1].find(')')]
                    strB = words[2][words[2].find('(')+1:words[2].find(')')]
                    strA = words[3][words[3].find('(')+1:words[3].find(')')]
                    strCellname = mod[1]
                    #print strCellname
                    tmpstr1 = "KC_OA21_X1      %s_W1     ( .Y(%s)   , .B(%s)   , .A1(%s)   , .A0(%s)   );\n"%(strCellname, strY,  strY1, strB, strA)
                    tmpstr2 = "KC_NAND2_X1     %s_W2     ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname,  strY1,  strB, strA)
                    tmpstr3 = "KC_INV_X1       %s_W3     ( .Y(%s)   , .A(%s)   );\n"%(strCellname, strC,  strY1)
                    outfile.write(tmpstr1)
                    outfile.write(tmpstr2)
                    outfile.write(tmpstr3)
                    continue
                #KC_OA12B_X1
                if ("KC_OA12B_X1" in mod[0]):  #
                    #print words  #['.Y(T8638_Y)', '.D1(T288_Q)', '.D0(T12440_Y)', '.C1(T5241_Q)', '.C0(T12411_Y)', '.B1(T5226_Q)', '.B0(T12413_Y)', '.A1(T293_Q)', '.A0(T12412_Y)']
                    strY = words[0][words[0].find('(')+1:words[0].find(')')]
                    strY1 = mod[1]+"L1"  #��ֵ�Ԫ���ڲ�����
                    strC = words[1][words[1].find('(')+1:words[1].find(')')]
                    strB = words[2][words[2].find('(')+1:words[2].find(')')]
                    strA = words[3][words[3].find('(')+1:words[3].find(')')]
                    strCellname = mod[1]
                    #print strCellname
                    tmpstr1 = "KC_NOR2_X1     %s     ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY,strC,strY1)
                    tmpstr2 = "KC_NOR2_X1     %s_W1  ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY1,strB,strA)
                    outfile.write(tmpstr1)
                    outfile.write(tmpstr2)
                    continue
                #KC_AO2222_X1
                if ("KC_AO2222_X" in mod[0]):  #KC_AO2222_X1    T8833   ( .Y(T8833_Y)    , .D1(T8811_Y)   , .D0(T8635_Y)   , .C1(T231_Y)    , .C0(T8867_Y)   , .B1(T8812_Y)   , .B0(T7912_Y)   , .A1(T8868_Y)   , .A0(T8917_Y)   );
                    #print words  #['.Y(T8638_Y)', '.D1(T288_Q)', '.D0(T12440_Y)', '.C1(T5241_Q)', '.C0(T12411_Y)', '.B1(T5226_Q)', '.B0(T12413_Y)', '.A1(T293_Q)', '.A0(T12412_Y)']
                    strY  = words[0][words[0].find('(')+1:words[0].find(')')]
                    strY1 = mod[1]+"L1"
                    strY2 = mod[1]+"L2"
                    strD1 = words[1][words[1].find('(')+1:words[1].find(')')]
                    strD0 = words[2][words[2].find('(')+1:words[2].find(')')]
                    strC1 = words[3][words[3].find('(')+1:words[3].find(')')] 
                    strC0 = words[4][words[4].find('(')+1:words[4].find(')')] 
                    strB1 = words[5][words[5].find('(')+1:words[5].find(')')] 
                    strB0 = words[6][words[6].find('(')+1:words[6].find(')')] 
                    strA1 = words[7][words[7].find('(')+1:words[7].find(')')] 
                    strA0 = words[8][words[8].find('(')+1:words[8].find(')')] 
                    strCellname = mod[1]
                    #KC_NAND2_X4     T7813     ( .Y(813_Y))   , .B(T7813L1)   , .A(T7813L2)   );
                    tmpstr1 = "KC_NAND2_X4     %s     ( .Y(%s)   , .B(%s)   , .A(%s)   );\n"%(strCellname, strY,strY1,strY2)
                    tmpstr2 = "KC_AOI22_X2     %s_W1  ( .Y(%s)   , .B1(%s)  , .B0(%s)   , .A1(%s)  , .A0(%s)  );\n"%(strCellname, strY1,strD1,strD0,strC1,strC0)
                    tmpstr3 = "KC_AOI22_X2     %s_W2  ( .Y(%s)   , .B1(%s)  , .B0(%s)   , .A1(%s)  , .A0(%s)  );\n"%(strCellname, strY2,strB1,strB0,strA1,strA0)
                    
                    outfile.write(tmpstr1)
                    outfile.write(tmpstr2)
                    outfile.write(tmpstr3)
                    continue
                #��������䲻һ�£���������ʽ��֤��ͨ����ԭ��
                if (mod[1] == "T10537"):
                    outfile.write("KC_AOI21B_X2     T10537    ( .Y(T10537_Y)    , .A1(T2649_Y)    , .A0(T15689_Y)   , .BN(T15689_Y)   );\n")
                    continue
                if (mod[1] == "T5735"):
                    outfile.write("KC_INV_X1        T5735     ( .Y(T5735_Y)     , .A(T15689_Y)    );\n")
                    continue           
            #print mod[0] + " " + mod[1] + " " + "( ",
            outfile.write(mod[0] + " " + ' '*(16 - len(mod[0])) + mod[1] + " " + ' '*(8 - len(mod[1])) + " " + "( ")
            #���ҵ����������PIN��������ļ�
            for var1 in words:
                if ((".Q(" in var1) or (".QN(" in var1) or (".Y(" in var1) or (".co(" in var1) or (".S(" in var1)) :
                    outfile.write(var1 + ' '*(15 - len(var1)) + " ")
                    outfile.write(", ")
                    words.remove(var1)  #���PINд��֮��ɾ�����PIN��ֻʣ������PIN
            tmpi = 0
            #Ȼ�������������PIN������ļ�
            for var2 in words:
                tmpi = tmpi+1
                #print var2,
                outfile.write(var2 + ' '*(15 - len(var2)) + " ")
                if (tmpi != len(words)):
                    #print ", ",
                    outfile.write(", ")
            #print ");"
            outfile.write(");" + "\n")
        else:
            #print "    " + line,
            outfile.write(line)
            serial = 1
    outfile.close()
    infile.close()

##################################################################################################  
##�������������������ӿɱ���
#infilename = RLS_dxj_lyt+"_top_tmp1.v"
#outfilename = RLS_dxj_lyt+"_top_tmp2.v"
#print "input  file is : ", infilename
#print "output file is : ", outfilename
#
#infile = open(infilename)
#outfile = open(outfilename, 'w')
#
#for line in infile:
#    if ("CELL" in line):
#        line = line.replace("CELL", "DFFCELL")
#        line = line.replace(".Y(", ".Q(")
#    if ("KC_TLAT_X3" in line):
#        line = line.replace(".Q(", ".Y(")
#    outfile.write(line)
#    serial = 1

#################################################################################################
if (expmod == "singlecell"):
    looptimes1 = 1
    looptimes2 = 62
elif (expmod == "allport"):
    looptimes1 = 1
    looptimes2 = 62
elif (expmod == "loopcells"):
    looptimes1 = 62
    looptimes2 = 90
        
for i in range(looptimes1, looptimes2):
    #��ǰ��ѭ��������ļ���Ϊ���룬����һ�����ļ���Ϊ���
    infilename = RLS_dxj_lyt + "_top_tmp" + str(i) + ".v"
    outfilename = RLS_dxj_lyt + "_top_tmp" + str(i+1) + ".v"

    infile = open(infilename)
    outfile = open(outfilename, 'w')
    #print "input  file is : ", infilename
    #print "output file is : ", outfilename
    sys.stdout.write("   *** stage%d ***   \n" % (i-1))
    sys.stdout.flush()
        
    #��ǰ��������ļ������ϣ��������������ͳһ���������
    #��Ҫע����ǣ���һ�����ڶ˿��Ͻ��еģ���Ҫ���⴦��
    Expanding_Pin_List = []
    if (i==1):
        if (expmod == "allport"):
            for line in infile:
               words = line.split()
               if ("output" in words[0]):
                   Expanding_Pin_List.append(words[1])
        if (expmod == "singlecell"):
            for line in infile:
                words = line.split()
                if (len(words) <= 1) :
                    serial = 1
                elif (thecellname == words[1]):
                    #print line
                    outfile.write("/*stage0*/  " + line)
                    for var3 in words:
                        if (("." in var3) and (".Y(" not in var3) and (".Q(" not in var3) and (".S(" not in var3) and (".QN(" not in var3)):
                            var3 = var3[var3.find('(')+1:var3.find(')')]
                            if (var3 not in Expanding_Pin_List):
                                #print var3
                                Expanding_Pin_List.append(var3)
    elif (i == 62):
        if (RLS_dxj_lyt == "lyt"):
            #Expanding_Pin_List.append("T161_Q")
            Expanding_Pin_List.append("T15286_Q")
            Expanding_Pin_List.append("T15284_Q")
            Expanding_Pin_List.append("T15285_Q")
            Expanding_Pin_List.append("T15288_Q")
            Expanding_Pin_List.append("T15287_Q")
            Expanding_Pin_List.append("T5594_Q") 
            Expanding_Pin_List.append("T28_Q")   
            Expanding_Pin_List.append("T15307_Q")
            Expanding_Pin_List.append("T15299_Q")
            Expanding_Pin_List.append("T15292_Q")
            Expanding_Pin_List.append("T15291_Q")
            Expanding_Pin_List.append("T15305_Q")
            Expanding_Pin_List.append("T15304_Q")
            Expanding_Pin_List.append("T115_Q")  
            Expanding_Pin_List.append("T15289_Q")
            Expanding_Pin_List.append("T15302_Q")
            Expanding_Pin_List.append("T15306_Q")
            Expanding_Pin_List.append("T15309_Q")
            Expanding_Pin_List.append("T15300_Q")
            Expanding_Pin_List.append("T15295_Q")
            Expanding_Pin_List.append("T15293_Q")
            Expanding_Pin_List.append("T15303_Q")
            Expanding_Pin_List.append("T15301_Q")
            Expanding_Pin_List.append("T5595_Q") 
            Expanding_Pin_List.append("T15296_Q")   #T15263_Q
            Expanding_Pin_List.append("T15269_Q")
            Expanding_Pin_List.append("T15268_Q")
            Expanding_Pin_List.append("T15282_Q")
            Expanding_Pin_List.append("T15273_Q")
            Expanding_Pin_List.append("T15272_Q")
            Expanding_Pin_List.append("T15279_Q")
            Expanding_Pin_List.append("T15278_Q")
            Expanding_Pin_List.append("T15265_Q")
            Expanding_Pin_List.append("T15264_Q")
            Expanding_Pin_List.append("T15274_Q")
            Expanding_Pin_List.append("T15259_Q")
            Expanding_Pin_List.append("T15258_Q")
            Expanding_Pin_List.append("T15261_Q")
            Expanding_Pin_List.append("T15260_Q")
            Expanding_Pin_List.append("T15271_Q")
            Expanding_Pin_List.append("T15270_Q")
            Expanding_Pin_List.append("T15281_Q")
            Expanding_Pin_List.append("T15290_Q")
            Expanding_Pin_List.append("T15280_Q")  #T15283_Q
            Expanding_Pin_List.append("T15283_Q")  #T15280_Q
            Expanding_Pin_List.append("T15294_Q")
            Expanding_Pin_List.append("T15262_Q")
            Expanding_Pin_List.append("T15263_Q")  #T15296_Q
            Expanding_Pin_List.append("T15308_Q")
            Expanding_Pin_List.append("T15298_Q")
            Expanding_Pin_List.append("T15297_Q")
            Expanding_Pin_List.append("T15267_Q")
            Expanding_Pin_List.append("T15266_Q")
            Expanding_Pin_List.append("T15275_Q")
            Expanding_Pin_List.append("T15277_Q")
            Expanding_Pin_List.append("T15276_Q")    
                   
            Expanding_Pin_List.append("T13216_Q")
            Expanding_Pin_List.append("T13229_Q")
            Expanding_Pin_List.append("T135_Q")  
            Expanding_Pin_List.append("T132_Q")  
            Expanding_Pin_List.append("T161_Q")  
        if (RLS_dxj_lyt == "dxj"):
            Expanding_Pin_List.append("D16718_Q")  
            Expanding_Pin_List.append("D16717_Q")  
            Expanding_Pin_List.append("D16710_Q")  
            Expanding_Pin_List.append("D16635_Q")  
            Expanding_Pin_List.append("D16634_Q")  
            Expanding_Pin_List.append("D16566_Q")  
            Expanding_Pin_List.append("D16565_Q")  
            Expanding_Pin_List.append("D16332_Q")  
            Expanding_Pin_List.append("D16331_Q")  
            Expanding_Pin_List.append("D15153_Q")  
            Expanding_Pin_List.append("D15152_Q")  
            Expanding_Pin_List.append("D14702_Q")  
            Expanding_Pin_List.append("D14701_Q")  
            Expanding_Pin_List.append("D13837_Q")  
            Expanding_Pin_List.append("D13836_Q")  
            Expanding_Pin_List.append("D12366_Q")  
            Expanding_Pin_List.append("D12291_Q")  
            Expanding_Pin_List.append("D11606_Q")  
            Expanding_Pin_List.append("D11413_Q")  
            Expanding_Pin_List.append("D11051_Q")  
            Expanding_Pin_List.append("D11050_Q")  
            Expanding_Pin_List.append("D10828_Q")  
            Expanding_Pin_List.append("D10826_Q")  
            Expanding_Pin_List.append("D9918_Q")   
            Expanding_Pin_List.append("D8605_Q")   
            Expanding_Pin_List.append("D8159_Q")   
            Expanding_Pin_List.append("D8158_Q")   
            Expanding_Pin_List.append("D6616_Q")   
            Expanding_Pin_List.append("D6402_Q")   
            Expanding_Pin_List.append("D6401_Q")   
            Expanding_Pin_List.append("D5815_Q")   
            Expanding_Pin_List.append("D5814_Q")   
            Expanding_Pin_List.append("D5416_Q")   
            Expanding_Pin_List.append("D5415_Q")   
            Expanding_Pin_List.append("D4647_Q")   
            Expanding_Pin_List.append("D4066_Q")   
            Expanding_Pin_List.append("D4065_Q")   
            Expanding_Pin_List.append("D4024_Q")   
            Expanding_Pin_List.append("D4023_Q")   
            Expanding_Pin_List.append("D3758_Q")   
            Expanding_Pin_List.append("D3757_Q")   
            Expanding_Pin_List.append("D1806_Q")   
            Expanding_Pin_List.append("D1394_Q")   
            Expanding_Pin_List.append("D1393_Q")   
            Expanding_Pin_List.append("D1392_Q")   
            Expanding_Pin_List.append("D1243_Q")   
            Expanding_Pin_List.append("D1242_Q")   
            Expanding_Pin_List.append("D1162_Q")   
            Expanding_Pin_List.append("D1064_Q")   
            Expanding_Pin_List.append("D1063_Q")   
            Expanding_Pin_List.append("D1062_Q")   
            Expanding_Pin_List.append("D944_Q")    
            Expanding_Pin_List.append("D943_Q")    
            Expanding_Pin_List.append("D361_Q")    
            Expanding_Pin_List.append("D331_Q")    
            Expanding_Pin_List.append("D330_Q")    
            
            Expanding_Pin_List.append("D16483_Q")
            Expanding_Pin_List.append("D16399_Q")
            Expanding_Pin_List.append("D16474_Q")
            Expanding_Pin_List.append("D16472_Q")
            Expanding_Pin_List.append("D16386_Q")

    else:
        stagex = "stage"+str(i-1)
        for line in infile:
            words = line.split()
            if (stagex in words[0]):
                #print line
                for var4 in words:
                    if (("." in var4) and (".Y(" not in var4) and (".Q(" not in var4) and (".S(" not in var4) and (".QN(" not in var4)):
                        var4 = var4[var4.find('(')+1:var4.find(')')]
                        if (var4 not in Expanding_Pin_List):
                            #print var4
                            Expanding_Pin_List.append(var4)
    #print Expanding_Pin_List
    
    #���������ڴ�ʱ��Expanding_Pin_List ���Ѿ��������Ҫ�ں����в��ҵĶ˿��б�
    #����б���Դ��ǰһ��stage����������������˿ڵļ���(������ȥ�ظ�)
    #���ǣ���Ҫע�⣺�����б��е�ÿһ������ں������ҵ���֮��Ӧ������˿ڣ�����Ϊһ������������������ӵ�������������룬
    #���ԣ���ǰ��չ�б��е�ĳ���˿ڶ�Ӧ��������������ǰ���ִ������Ѿ����ŵ�ĳ��state��ȥ��
    
    #������䣺��ĳ��wire�Ƿ���������չ�б���
    #if ("T7672_Y_W" in Expanding_Pin_List):
    #    print Expanding_Pin_List
    infile.close()
    infile = open(infilename)
    
    linebuff_1 = ["N*C"]*20000
    linebuff_2 = []
    
    for line in infile:  #��ǰһ������ļ�����ѭ��
        words = line.split()  #words ����ʽ�磺 ['KC_NOR2_X2', 'D7164', '(', '.Y(D7164_Y)', ',', '.B(D7252_Y)', ',', '.A(D5756_Y)', ');']
        propagateflag = 0
        if (len(words) <= 0) : #�������Ǹ����У���ʲô������
            serial = 1
        elif ("KC_" in words[0]):  #��������˵����һ���ǻ�û�о������������������ǰ׺ stagex��
            words[3] = words[3][words[3].find('(')+1:words[3].find(')')] #Ϊ�˼��ٳ��������Ȱ�words[3]���ɾ�
            for var5 in range (0,len(Expanding_Pin_List)):  #��0����չ�б����һ�����ѭ��
                if (Expanding_Pin_List[var5] == words[3]):  #��չ�б��У�����һ�����������˿��ź���ƥ��
                    #������䣺��ĳ��wire�Ƿ���չ���
                    #if ("T7672_Y_W" == words[3]):
                        #print var5
                        #print words[3]
                        #print line
                        #print Expanding_Pin_List
                    linebuff_1[var5] = line
                    propagateflag = 1
                    continue
            if (propagateflag == 0):
                linebuff_2.append(line)
                propagateflag = 1
        elif ("endmodule" not in words[0]):
            if (expmod == "allport"):
                outfile.write(line)
            if (expmod == "singlecell"):
                if ("put" not in words[0]):
                    outfile.write(line)
            if (expmod == "loopcells"):
                outfile.write(line)
            serial = 1
        elif ("endmodule" in words[0]):
            for var6 in linebuff_1:
                if (var6 != "N*C"):
                    outfile.write("/*stage" + str(i) + "*/  " + var6)
            for var7 in linebuff_2:
                outfile.write(var7)
            outfile.write("endmodule")
    outfile.close()
    infile.close()
    os.remove(infilename)
