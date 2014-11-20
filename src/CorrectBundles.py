'''
Created on Nov 17, 2014

@author: ess0006
'''
import re

if __name__ == '__main__':
    pass
actIntentRegex = "(.*?)=(.*?)(this.)getIntent();"
getExtrasRegex = " (.*?)=(.*?).getExtras\(\)"
actIntents = [] #activity intents, eg Intent intent = this.getIntent();
bundles = [] #bundles populated using getIntent().getExtras()

path =  'C:\\apks\\BundleApp\\src\\com\\example\\bundleapp\\Activity1.java'
with open(path) as f:
    for line in f:
        matches = re.findall(actIntentRegex, line)
        if(len(matches) > 0):
            print matches[0]
            actIntents.append(matches[0][0].strip())
            #rebuild regex for getExtras
            getExtrasRegex = " (.*?)=(getIntent\(\)|this.getIntent\(\)"
            for ai in actIntents:
                getExtrasRegex.append("|" + ai)
            getExtrasRegex.append(")")
        
        matches = re.findall(getExtrasRegex, line)
        if(len(matches) > 0):
            print matches[0]
            bundles.append(matches[0][0].strip())
            
    print "bundles: " + str(bundles)

#now we have a list of bundles that could be null - read the file again and make sure that when they are used, they are checked

#state variables
tryNestingLevel = 0 #need to keep nesting level so we know which exceptions are being caught
inIfNull = False
inComment = False

tryRegex = "try(.*?){"
catchRegex = "catch(.?*){"
ifNullRegex = ""
ifNotNullRegex =  ""

with open(path) as f:
    for line in f:
        matches = re.findall(tryRegex, line)
        if(len(matches) > 0):
            tryNestingLevel = tryNestingLevel + 1
            print "try nesting level: " + str(tryNestingLevel)
        
        
        matches = re.findall(catchRegex, line)
        if(len(matches) > 0):
            tryNestingLevel = tryNestingLevel - 1
            print "try nesting level: " + str(tryNestingLevel)