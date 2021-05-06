import random

# first section, 8 sets of predifined 8 numbers integer
firstsecnum = ["19303829",
                "29401930",
                "48265454",
                "19305533",
                "79183053",
                "01093725",
                "90184431",
                "19321525",
                ]
firstsecrand = random.choice(firstsecnum)
# second section, which is random 8 num int

secsecnum = random.randrange(10000000, 99999999)

# thrid section, random 4 num int

thirdsecnum = random.randrange(1000, 9999)

# fourth section, 12 sets of predifined 12 numbers integer

fourthsecnum = ["158190927278",
                "518540776483",
                "105380983493",
                "937115997851",
                "182029438459",
                "717078082316",
                "527740326237",
                "414714541837",
                "381370558578",
                "347862452401",
                "400820191263",
                "962635909965"
                ]
fourthsecrand = random.choice(fourthsecnum)
# join the numbers
def gen():
    joinednum = str(firstsecrand) + str(secsecnum) + str(thirdsecnum) + str(fourthsecrand)
    return joinednum
