import random, copy
import utilIAP as iap

def generate(data):

    nHosts = 3
    sub = random.randint(2, 254)
    data['params']['sub'] = sub
    
    data['params']['hosts']  =  iap.hosts_in_subnet("192.168." + str(sub) + '.0', 24, nHosts)
    order = random.sample(range(nHosts), k=nHosts)
    
    data['params']['dstaddr'] = data['params']['hosts'][order[0]]['mac'].replace(":", " ")
    data['params']['srcaddr'] = iap.macs(1)[0].replace(":", " ")
    data['params']['type'] = random.choice(["08 00", "86 dd"])

    data['params']['opts'] = [{'host': data['params']['hosts'][i]['name'], 
                                'pass': i==order[0],
                                'ignore':  i!=order[0]} for i in range(3)]
