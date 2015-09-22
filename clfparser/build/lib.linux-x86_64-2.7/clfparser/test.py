from clfparser import CLFParser

test = '10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209'
print (CLFParser.logDict(test))
print (CLFParser.logParts(test, '%h %t %time'))

with open('/home/nnon/dev/data/access_logSmall', 'rb') as log:
     recs = []
     for rec in log:
         w = CLFParser.logParts(rec, '("%h", "%t", %time, %timezone)')
         recs.append(w)
     print len(recs)

