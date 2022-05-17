'''
17.05.2022
Developed to be used for bachelor thesis on SNPs analysis

by Askhat Aubakirov
e-mail: askhat.aubakirov@yahoo.com
linkedIn: https://www.linkedin.com/in/askhattio/
'''

import  re

#for default algorithm:
pur_AG = re.compile("\tA\tG") # #
pur_GA = re.compile("\tG\tA") # #
pyr_TC = re.compile("\tT\tC") # #
pyr_CT = re.compile("\tC\tT") # #

pupy_AT = re.compile("\tA\tT") # #
pupy_AC = re.compile("\tA\tC") # #
pupy_GT = re.compile("\tG\tT") # #
pupy_GC = re.compile("\tG\tC") # #

pypu_TA = re.compile("\tT\tA") # #
pypu_TG = re.compile("\tT\tG") # #
pypu_CA = re.compile("\tC\tA") # #
pypu_CG = re.compile("\tC\tG") # #

'''
#for samtools algorithm:
sam_pur_AR = re.compile("\tA\tR") #
sam_pur_GR = re.compile("\tG\tR") #
sam_pyr_TY = re.compile("\tT\tY") #
sam_pyr_CY = re.compile("\tC\tY") #

sam_pupy_AY = re.compile("\tA\tY") #
sam_pupy_GY = re.compile("\tG\tY") #

sam_pypu_TR = re.compile("\tT\tR") #
sam_pypu_CR = re.compile("\tC\tR") #
'''

#for deletion points in any algoritm:
del_points = re.compile("\t-")

file = open("all_snps.txt", "r")
#file = open("kazakh/kazakh.txt", "r")
#file = open("indian/indian.txt", "r")


file_str = file.read()
file.close()

file_str = file_str.split("\n")

#counters for default algorithm:
pur_AG_count = 0
pur_GA_count = 0
pyr_TC_count = 0
pyr_CT_count = 0

pupy_AT_count = 0
pupy_AC_count = 0
pupy_GT_count = 0
pupy_GC_count = 0

pypu_TA_count = 0
pypu_TG_count = 0
pypu_CA_count = 0
pypu_CG_count = 0

'''
#counters for samtools algorithm:
sam_pur_AR_count = 0
sam_pur_GR_count = 0
sam_pyr_TY_count = 0
sam_pyr_CY_count = 0

sam_pupy_AY_count = 0
sam_pupy_GY_count = 0

sam_pypu_TR_count = 0
sam_pypu_CR_count = 0
'''

#counter for deletions
del_points_count = 0

not_found = 0

for elem in file_str:
    #for default:
    if pur_AG.search(elem):
        pur_AG_count += 1
    elif pur_GA.search(elem):
        pur_GA_count += 1
    elif pyr_TC.search(elem):
        pyr_TC_count += 1
    elif pyr_CT.search(elem):
        pyr_CT_count += 1
    elif pupy_AT.search(elem):
        pupy_AT_count += 1
    elif pupy_AC.search(elem):
        pupy_AC_count += 1
    elif pupy_GT.search(elem):
        pupy_GT_count += 1
    elif pupy_GC.search(elem):
        pupy_GC_count += 1
    elif pypu_TA.search(elem):
        pypu_TA_count += 1
    elif pypu_TG.search(elem):
        pypu_TG_count += 1
    elif pypu_CA.search(elem):
        pypu_CA_count += 1
    elif pypu_CG.search(elem):
        pypu_CG_count += 1
    #for deletion points:
    elif del_points.search(elem):
        del_points_count += 1
    else:
        not_found += 1
       
consensus_diff = del_points_count + pypu_CG_count + pypu_CA_count + pypu_TG_count + pypu_TA_count + pupy_GC_count + pupy_GT_count + pupy_AC_count + pupy_AT_count + pyr_CT_count + pyr_TC_count + pur_GA_count + pur_AG_count
total_snps = pypu_CG_count + pypu_CA_count + pypu_TG_count + pypu_TA_count + pupy_GC_count + pupy_GT_count + pupy_AC_count + pupy_AT_count + pyr_CT_count + pyr_TC_count + pur_GA_count + pur_AG_count

print("\n-------------- General information (OVERALL) -----------------")
print(f"Consensus differences: {consensus_diff}")
print(f"Amount of SNPs: {total_snps}")
print(f"Deletion Points: {del_points_count}")

print("\n-------------- PUR >> PUR AND PYR >> PYR -----------------")
print(f"pur >> pur (A >> G): {pur_AG_count}")
print(f"pur >> pur (G >> A): {pur_GA_count}")
print(f"pur >> pur OVERALL: {pur_AG_count + pur_GA_count} \n")

print(f"pyr >> pyr (T >> C): {pyr_TC_count}")
print(f"pyr >> pyr (C >> T): {pyr_CT_count}")
print(f"pyr >> pyr OVERALL: {pyr_TC_count + pyr_CT_count}")
print("\n-------------- PUR >> PYR -----------------")
print(f"pur >> pyr (A >> T): {pupy_AT_count}")
print(f"pur >> pyr (A >> C): {pupy_AC_count}")
print(f"pur >> pyr (G >> T): {pupy_GT_count}")
print(f"pur >> pyr (G >> C): {pupy_GC_count}")
print(f"pur >> pyr OVERALL: {pupy_AT_count + pupy_AC_count + pupy_GT_count + pupy_GC_count}")
print("\n-------------- PYR >> PUR -----------------")
print(f"pyr >> pyr (T >> A): {pypu_TA_count}")
print(f"pyr >> pyr (T >> G): {pypu_TG_count}")
print(f"pyr >> pyr (C >> A): {pypu_CA_count}")
print(f"pyr >> pyr (C >> G): {pypu_CG_count}")
print(f"pyr >> pur OVERALL: {pypu_TA_count + pypu_TG_count + pypu_CA_count + pypu_CG_count}")

print(f"\nnot found: {not_found}")
