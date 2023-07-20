import random

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
ipa = 'ESign.ipa'
s = random.randint(1, 99999999999999999999999)
out = f"{s}.ipa"
osi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id}' -o {out} -z 9 {app}"
r = random.randint(1, 99999999999999999999999)
d = random.randint(1, 99999999999999999999999)
out1 = f"{r}.ipa"
out2 = f"{d}.ipa"

LRD = "Lrd.ipa"
DARK = "Dark.ipa"

LRDosi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id1}' -o {out1} -z 9 {LRD}"
DARKosi = f"./zsign -k {p12} -p {pass1} -m {prov} -b '{id2}' -o {out2} -z 9 {DARK}"
