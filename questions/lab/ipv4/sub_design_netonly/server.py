import random, copy, io
import utilIAP as iap
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def file(data):
    colors = {22: 'red', 23: 'orange', 24: 'lightgreen', 25: 'green', 26: 'cyan', 27: 'blue', 28: 'purple', 29: 'pink'} 
    ipmin = data['params']['rangemin'] 
    ipmax = data['params']['rangemax'] 
    rangemin = iap.ip_dotdec_to_int(ipmin)
    rangemax = iap.ip_dotdec_to_int(ipmax)

    prefix = data['params']['prefix']
    top_range = 0
    current = rangemin
    smallest_intervals = []
    smallest_prefix =  max(prefix)
    smallest_size = 2**(32-smallest_prefix)
    while top_range < rangemax:
      net_addr = iap.netaddr_dotdec(iap.ip_int_to_dotdec(current), smallest_prefix)
      top_range = current + smallest_size
      current = top_range
      if current <= rangemax:
        smallest_intervals.append(net_addr)
    
    interval_dict = [{'prefix': p, 'width': 2**(32-p), 'start': iap.ip_dotdec_to_int(i), 'label': i }  for i in smallest_intervals for p in prefix if i == iap.netaddr_dotdec(i, p) and iap.ip_dotdec_to_int(iap.bcaddr_dotdec(i ,p) ) < rangemax]
    
    if data['filename']=='explain.png':
    
        #define Matplotlib figure and axis
        fig, ax = plt.subplots(figsize=(8, 5))
        
        #create simple line plot
        ax.plot([rangemin, rangemax],[min(prefix), max(prefix)], alpha=0)
        
        #add rectangle to plot
        for net in interval_dict:
          ax.add_patch(Rectangle((net['start'], net['prefix']-0.5), net['width']-2, 0.8, facecolor=colors[net['prefix']], edgecolor='white'))
        
        plt.yticks(ticks=prefix)
        plt.ylabel("Prefix length")
        
        x_ticks = [iap.ip_dotdec_to_int(n) for n in smallest_intervals]
        x_ticks.insert(0, rangemin)
        x_ticks.insert(-1, rangemax)
        x_labels = [n for n in smallest_intervals]
        x_labels.insert(0, ipmin)
        x_labels.insert(-1, ipmax)
        
        plt.xticks(ticks=x_ticks, labels=x_labels, rotation=90 )
        
        plt.title("Valid positions for subnets\nAddress range %s - %s" % (ipmin, ipmax))
        plt.tight_layout()
        
        # Save the figure and return it as a buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        return buf
        


def generate(data):
    

    var = random.choice([0,1, 2])
    # problem parameters
    if var == 0:
        data['params']['subnet'] = random.choice([random.randint(129,254), random.randint(12, 125)])
        data['params']['rangemin'] = "10.1.%d.160" % data['params']['subnet'] 
        data['params']['rangemax'] = "10.1.%d.176" % (data['params']['subnet']+1)
        data['params']['nhosts'] = random.sample([random.randint(17, 27), random.randint(33,59), random.randint(66, 120)], k=3)
    elif var == 1:
        data['params']['subnet'] = random.choice([random.randint(129,254), random.randint(12, 125)])
        data['params']['rangemin'] = "10.1.%d.224" % data['params']['subnet'] 
        data['params']['rangemax'] = "10.1.%d.96" % (data['params']['subnet'] + 1 )
        data['params']['nhosts'] = random.sample([random.randint(17, 27), random.randint(33,59), random.randint(9, 11)], k=3)
    elif var == 2:
        data['params']['subnet'] = random.choice([random.randrange(129,253, 2), random.randrange(11, 125, 2)])
        data['params']['rangemin'] = "10.1.%d.0" % (data['params']['subnet']) # start on the odd number. can't put the big subnet here!
        data['params']['rangemax'] = "10.1.%d.0" % (data['params']['subnet']+3)
        data['params']['nhosts'] = random.sample([random.randint(33,59), 
                                                    random.randint(70,120), 
                                                    random.randint(300, 500)], k=3)
    
    # given number of hosts, get max prefix length and corresponding netmask for each LAN
    data['params']['prefix'] = [iap.nhosts_to_prefix_length(n) for n in data['params']['nhosts']]
    data['params']['mask']   = [iap.prefix_length_to_subnet(n) for n in data['params']['prefix']]
    
    # intialize network addresses to bottom of range, but don't keep it like that!
    data['params']['netaddr'] = [data['params']['rangemin'], data['params']['rangemin'], data['params']['rangemin']]
    
    # figuring out network addresses
    # the big LAN is going to have to go last, the others can go earlier
    net_sort = np.argsort(data['params']['prefix'])
    if var == 0:
        net_order = np.array([net_sort[2], net_sort[1], net_sort[0]])
    elif var == 1:
        net_order = np.array([net_sort[1], net_sort[0], net_sort[2]])
    elif var == 2:
        net_order = np.array([net_sort[1], net_sort[2], net_sort[0]])

    hosts_per_lan = 2**(32-np.array( data['params']['prefix'] ))
    hosts_cum_sum = np.cumsum(hosts_per_lan[net_order])
    # then increment network address by number of hosts in previous LAN
    range_min_int = iap.ip_dotdec_to_int( data['params']['rangemin'] )
    range_top_net = [0, 0, 0]

    for i in range(3):
        range_top_net[net_order[i]] = range_min_int + hosts_cum_sum[i] - 1
        
    data['params']['netaddr'] = [iap.netaddr_dotdec( iap.ip_int_to_dotdec(range_top_net[i]),  data['params']['prefix'][i] ) for i in range(3) ]

    data['params']['bcastaddr'] =  [iap.bcaddr_dotdec(data['params']['netaddr'][i], data['params']['prefix'][i]) for i in range(3)]
    data['params']['minaddr'] =  [iap.min_ip_in_subnet(data['params']['netaddr'][i], data['params']['prefix'][i]) for i in range(3)]
    data['params']['maxaddr'] =  [iap.max_ip_in_subnet(data['params']['netaddr'][i], data['params']['prefix'][i]) for i in range(3)]
    

    
def parse(data):
    
    # remove whitespace
    for tag in data['submitted_answers'].keys():
        data['submitted_answers'][tag] = data['submitted_answers'][tag].strip()
        
        if not (iap.is_dotdec(data['submitted_answers'][tag]) ):
            data["format_errors"][tag] = "Not in valid dotted decimal notation."
            
            # check if subnet mask is a valid subnet mask
        else:
            if "mask" in tag and ( not iap.is_subnet_mask(data['submitted_answers'][tag]) ):
                data["format_errors"][tag] = "Not a valid subnet mask (must have all 1s on the left, all 0s on the right)."



def grade(data):

    # to make sure none of the assigned addresses are outside the range!
    range_min_int = iap.ip_dotdec_to_int( data['params']['rangemin'] )
    range_max_int = iap.ip_dotdec_to_int( data['params']['rangemax'] )

    lan_dict = [
        {'name': 'a', 'validNetAddr': False, 'enoughHosts': False, 'inRange': False},
        {'name': 'b', 'validNetAddr': False, 'enoughHosts': False, 'inRange': False},
        {'name': 'c', 'validNetAddr': False, 'enoughHosts': False, 'inRange': False}
    ]

    
    # if it is gradeable, then we know we have valid subnet masks and network addresses in dot decimal notation
    for i in range(len(lan_dict)):
        
        lan = lan_dict[i]['name']
        sub_ans = "lan" + lan + "-netmask"
        net_ans = "lan" + lan + "-network"
       
        # first, check each combination of subnet mask and network address, and make sure they are valid together
        if data['submitted_answers'][net_ans]==iap.netaddr_dotdec( data['submitted_answers'][net_ans], iap.subnet_to_prefix_length(data['submitted_answers'][sub_ans])  ):
            lan_dict[i]['validNetAddr'] = True
        
        else: # not a network address for given subnet mask
            data["feedback"][net_ans] =  "%s is not a valid network address, given the specified subnet mask (%s). A network address must have a 0 bit at each position where the subnet mask is also 0." % (data["submitted_answers"][net_ans], data["submitted_answers"][sub_ans])

        # now check if it supplies enough host addresses
        prefix = iap.subnet_to_prefix_length(data['submitted_answers'][sub_ans])
        if 2**(32-prefix ) >= data['params']['nhosts'][i] + 2:
            lan_dict[i]['enoughHosts'] = True
        else:
            data['feedback'][sub_ans] = "%s supports fewer than the required number of host addresses (%d)." % (data["submitted_answers"][sub_ans], data['params']['nhosts'][i])

        # now check if it in range
        if (
            (range_min_int <= iap.ip_dotdec_to_int(data['submitted_answers'][net_ans]) <= range_max_int) and 
            ( range_min_int <= iap.ip_dotdec_to_int(iap.bcaddr_dotdec(data['submitted_answers'][net_ans], prefix)) <= range_max_int   )
            ):
            lan_dict[i]['inRange'] = True
        
        else: # 
            data["feedback"][net_ans] =  "%s with subnet mask %s is not within the address range %s-%s" % (data["submitted_answers"][net_ans], data["submitted_answers"][sub_ans], data['params']['rangemin'], data['params']['rangemax'])
                    
        if all(  [ lan_dict[i]['validNetAddr'], lan_dict[i]['enoughHosts'], lan_dict[i]['inRange'] ]  ):
            data["partial_scores"][net_ans]['score']  = 1
            data["partial_scores"][sub_ans]['score']  = 1
        else:
            data["partial_scores"][net_ans]['score']  = 0
            data["partial_scores"][sub_ans]['score']  = 0

    # Now we check for overlap...
    intervals = [ ( iap.ip_dotdec_to_int(data['submitted_answers']['lan' + l['name'] + "-network"] ), 
                    iap.ip_dotdec_to_int(iap.bcaddr_dotdec(data['submitted_answers']['lan' + l['name'] + "-network"] , 
                                                           iap.subnet_to_prefix_length(data['submitted_answers']['lan' + l['name'] + "-netmask"] )) ) 
                                                           ) for  l in lan_dict ]
    intervals = sorted(intervals)
    disjoint = all(intervals[i+1][0] > intervals[i][1] for i in range(len(intervals) - 1))
    if disjoint:
        data['score'] = sum([data["partial_scores"][ans]['weight']*data["partial_scores"][ans]['score'] for ans in data["partial_scores"].keys()])/sum([data["partial_scores"][ans]['weight'] for ans in data["partial_scores"].keys()])
    else:
        data['score'] = 0
        data["feedback"]['overall'] = "Your subnets are not disjoint - they overlap! You must assign non-overlapping parts of the address space to each subnet." 