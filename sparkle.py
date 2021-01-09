from string import punctuation
deadword = False
micdrop = False
badwordlist = [l[0] for l in [word.strip('\n').split(',') for word in open("deadwordlist.txt", 'r').readlines()]]
deadwordlist = ['good', 'bad', 'what', 'how', 'thing', 'anything', 'something']
print ("Welcome to the Sparkle-O-Meter -- the definitive program for finetuning your *precise and sophisticated* diction.")
essay = input("Copy and paste your essay here.").split()
badwords, x = 0, 0
for e in essay[:-2]:
    essay[x] = e.strip(punctuation).lower()
    if essay[x] in badwordlist:
        badwords += 1
        print(essay[x])
    x += 1
print("You scored " + str(100 - (badwords/len(essay)) * 100) + "%.")
