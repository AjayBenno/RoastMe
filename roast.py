import random
fi = open('insults.txt')
insults=[]
for line in fi:
    insults.append(line)
    
def lambda_handler(event,context):
    ins = random.choice(insults)
    test = {}
    test['version'] = 1.0
    test['response'] = {"outputSpeech": { "type" :"PlainText","text":ins},"shouldEndSession" :false}
    return test

