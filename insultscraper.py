from lxml import html
import requests

def getInsults(url):
    page =  requests.get(url)
    tree = html.fromstring(page.content)
    insults = tree.xpath('//a[@class="linetext"]/text()')
    ins=[]
    map((lambda x : x.strip()),insults)
    for x in xrange(0,len(insults)):
        if(x % 2 ==0):
            ins.append( insults[x])
    
    return ins

url='http://www.gotlines.com/insults/'
totalins=[]
map((lambda x: totalins.append(getInsults(url+str(x)))), xrange(1,10))
flatten= lambda l: [item for sublist in l for item in sublist]
total= flatten(totalins)
f = open('insults.txt','w')
for t in total: 
    t = t + "\n"
    f.write(t.encode('utf-8'))
