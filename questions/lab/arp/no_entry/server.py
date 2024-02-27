import random, copy
import utilIAP as iap

def generate(data):

    data['params']['icmp'] = random.randint(256, 1024)
    data['params']['delay'] = format(random.randint(1,3) + random.random(), '#.2f')

    nHosts = random.randint(3,6)

    hostSelections = iap.hostnames(nHosts)
    hostAddr = random.sample(range(1,254), nHosts+1)
    sub = random.randint(2, 254)
    data['params']['sub'] = sub
    
    
    hostsGen =  iap.hosts_in_subnet("192.168." + str(sub) + '.0', 24, nHosts+1 )
    data['params']['hosts'] = hostsGen[0:nHosts]


    data['params']['ipB'] = data['params']['hosts'][1]['ip']
    data['params']['macB'] = data['params']['hosts'][1]['mac']

    data['params']['src'] = data['params']['hosts'][0]
    data['params']['dst'] = data['params']['hosts'][1]

