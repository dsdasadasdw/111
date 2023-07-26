import random
b = 2

# Картинка
name = "iPhone Distribution:\nMigu Digital Media Co. Ltd"

name2 = "iPhone Distribution:<br>Migu Digital Media Co. Ltd."
name1 = "iPhone Distribution: Migu Digital Media Co. Ltd."
pass1 = "AppleP12.com"
p12 = "1.p12"
prov = "2.mobileprovision"

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



ipa = 'ESign.ipa'


s = random.randint(1, 99999999999999999999999)
out = "1.ipa"
osi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id}' -o {out} -z 9 {app}"
r = random.randint(1, 99999999999999999999999)
d = random.randint(1, 99999999999999999999999)
out1 = "2.ipa"
out2 = "3.ipa"

LRD = "Lrd.ipa"
DARK = "Dark.ipa"

LRDosi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id1}' -o {out1} -z 9 {LRD}"
DARKosi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id2}' -o {out2} -z 9 {DARK}"

s1 = "s3cmd put 1.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"
s2 = "s3cmd put 2.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"
s3 = "s3cmd put 3.ipa s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc"

deletes1 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/1.ipa"
deletes2 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/2.ipa"
deletes3 = "s3cmd del s3://242be58c-a70cd3c6-e9a8-49a5-9ac5-c5fb1c3718bc/3.ipa"
