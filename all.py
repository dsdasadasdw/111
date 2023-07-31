import random
b = 2

# Картинка
name = "iPhone Distribution: HDFC Life\nInsurance Company Limited"
name2 = "iPhone Distribution: HDFC Life<br>Insurance Company Limited"
name1 = "iPhone Distribution: HDFC Life Insurance Company Limited"
name4 = " HDFC Life Insurance Company Limited"
pass1 = "TrollStore"

p12 = "1.p12"
prov = "2.mobileprovision"
p12_ = "3.p12"
prov_ = "4.mobileprovision"
bundl = random.randint(1, 99999999999999999999999)
id = f"ttskarl.esign.{bundl}"
id1 = f"com.zhiliaoapp.musically.lrd.ttskarl.{bundl}"
id2 = f"com.zhiliaoapp.musically.dark.ttskarl.{bundl}"


app = "ESign.ipa"
plist = 'ESign.plist'
plist1 = 'Lrd.plist'
plist2 = 'Dark.plist'
eplist = 'ESign1.plist'
eplist1 = 'Lrd1.plist'
eplist2 = 'Dark1.plist'
epliste = 'ESign2.plist'
eplistl = 'Lrd2.plist'
eplistd = 'Dark2.plist'


app = "ESign.ipa"
plist = 'ESign.plist'
plist1 = 'Lrd.plist'
plist2 = 'Dark.plist'
eplist = 'ESign1.plist'
eplist1 = 'Lrd1.plist'
eplist2 = 'Dark1.plist'
epliste = 'ESign2.plist'
eplistl = 'Lrd2.plist'
eplistd = 'Dark2.plist'



ipa = 'ESign.ipa'


out3 = "4.ipa"
out4 = "5.ipa"
out5 = "6.ipa"
s = random.randint(1, 99999999999999999999999)
out = "1.ipa"
osi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id}' -o {out} -z 9 {app}"
osi1 = f"./zsign -k {p12_} -p {pass1} -m {prov_} -b '{id}' -o {out3} -z 9 {app}"
r = random.randint(1, 99999999999999999999999)
d = random.randint(1, 99999999999999999999999)
out1 = "2.ipa"
out2 = "3.ipa"





LRD = "Lrd.ipa"
DARK = "Dark.ipa"
LRD1 = "Lrd1.ipa"
DARK1 = "Dark1.ipa"

LRDosi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id1}' -o {out1} -z 9 {LRD}"
DARKosi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id2}' -o {out2} -z 9 {DARK}"
LRDosi1 = f"./zsign -k {p12_} -p {pass1} -m {prov_} -b '{id1}' -o {out4} -z 9 {LRD1}"
DARKosi1 = f"./zsign -k {p12_} -p {pass1} -m {prov_} -b '{id2}' -o {out5} -z 9 {DARK1}"

s1 = "s3cmd put 1.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"
s2 = "s3cmd put 2.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"
s3 = "s3cmd put 3.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"

deletes1 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/1.ipa"
deletes2 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/2.ipa"
deletes3 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/3.ipa"


s4 = "s3cmd put 4.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"
s5 = "s3cmd put 5.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"
s6 = "s3cmd put 6.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"

deletes4 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/4.ipa"
deletes5 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/5.ipa"
deletes6 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/6.ipa"

