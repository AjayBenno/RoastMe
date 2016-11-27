import random
fi = open('insults.txt')
insults=[]
for line in fi:
    insults.append(line)
    
def lambda_handler(event,context):
    end = True
    if(event['request']['type'] == "IntentRequest"):
        if(event['request']['intent']['name'] == "AMAZON.HelpIntent"):
            ins = "Just ask alexa to roast you!"
            end = False
        elif(event['request']['intent']['name'] == "AMAZON.StopIntent" or event['request']['intent']['name'] == "AMAZON.CancelIntent"):
            ins = "Thanks for getting roasted, hope we never see you again!"
        else:
            ins = random.choice(insults) 
    elif(event['request']['type'] == "LaunchRequest"):
        ins = "Welcome to Roast Me, ask me to roast you!"
        end = False
    else:
        ins = "Goodbye"
    test = {}
    test['version'] = 1.0
    test['response'] = {"outputSpeech": { "type" :"PlainText","text":ins},"shouldEndSession" :end}
    return test

