import random
import string
import math
from random import choice

DATA_MEM = []
CACHE = []
valid = []

def generate_cache(data, ways, set_bits, num_addr, generate_data = True, addr_bits = 5, block_bits = 1, show_valid = False, empty_cache = False):
  addr_hex_size = math.ceil(addr_bits / 4)
  # random.seed(4)
  ### CREATE MEMORY TABLE
  mem_table = '<thead>\
          <tr>\
          <th>Address</th>\
          <th>Data</th>\
        </tr>\
      </thead>\
      <tbody>'


  for x in range(2**addr_bits):
    address = '{0:#0{1}x}'.format(x, addr_hex_size + 2)
    DATA_MEM.append(random.randint(0,255))

    mem_table += '<tr><td>' + address + '</td><td>' + str(DATA_MEM[x]) + '</td></tr>'

  mem_table += '</tbody>'
  data['params']['mem_table'] = mem_table

  #CACHE parameters
  cache_sets = 2**set_bits
  block_size = 2**block_bits
  data['params']['memory_size'] = 2**addr_bits
  data['params']['cache_sets'] = cache_sets
  data['params']['cache_size'] = ways * cache_sets * block_size
  data['params']['ways'] = ways
  data['params']['block_size'] = block_size

  way_list = []
  for way in range(ways):
    way_list.append(way)

  tag_bits = addr_bits - set_bits - block_bits
  tag_hex_size = math.ceil(tag_bits / 4)

  max_tag = 2**tag_bits - 1

  # generate initial CACHE data

  cache_block = {}
  start_table = '<thead><tr><th rowspan="2" style="width: 50px">Set Index</th>'
  if ways == 1:
    columnSpan = 1
    if show_valid:
      start_table += '<th rowspan="2" style="width: 50px">Valid</th>'
      columnSpan += 1
    start_table += '<th rowspan="2" style="width: 50px">Tag</th>'
    if generate_data:
      columnSpan += block_size

    start_table += f'<th rowspan="1" colspan="{columnSpan}">Block Offset</th>'
    start_table += '<tr>'
    if generate_data:
      for offset in range(block_size):
        start_table += f'<th style="width: 60px">{offset}</th>'
    start_table += '</tr>'
  else:
    for way in range(ways):
      columnSpan = 1
      if generate_data:
        columnSpan += block_size
      if show_valid:
        columnSpan += 1
      start_table += f'<th colspan="{columnSpan}">Way {way}</th>'
    start_table += '<th rowspan="2" style="width: 100px">LRU FSM</th></tr><tr>'
    for way in range(ways):
      if show_valid:
        start_table += '<th style="width: 50px">Valid</th>'
      if generate_data:
        start_table += '<th style="width: 50px">Tag</th>'
        for offset in range(block_size):
          start_table += f'<th style="width: 60px">Off {offset}</th>'
      else:
        start_table += '<th style="width: 100px">Tag</th>'
  start_table += '</tr></thead><tbody>'

  input_table = start_table

  for x in range(cache_sets):
    # generate 1 tag per way
    tags = []
    valid.append([])
    blocks = [[0 for j in range(block_size)] for i in range(ways)]

    for way in range(ways):
      if empty_cache:
        valid[x].append(0)
        tags.append(0)
        for offset in range(block_size):
          blocks[way][offset] = ''
      else:
        valid[x].append(1)
        tags.append(random.randint(0, max_tag))
        if way > 0:
          while tags[way] in tags[:way]:
            tags[way] = random.randint(0, max_tag)
        addr = (tags[way] * cache_sets + x) * block_size
        for offset in range(block_size):
          blocks[way][offset] = str(DATA_MEM[addr + offset])

    # generate LRU FSM
    lru_list = random.sample(way_list,len(way_list))

    cache_block = {'tags': tags, 'lru': lru_list, 'blocks': blocks}
    CACHE.append(cache_block)

    # add to html table
    start_table += f'<tr><td>{x}</td>'
    input_table += f'<tr><td>{x}</td>'

    for y in range(ways):

      start_table += '<td>' + '{0:#0{1}x}'.format(tags[y], tag_hex_size + 2) + '</td>'
      if generate_data:
        if show_valid:
          start_table += f'<td>{valid[x][y]}</td>'
          input_table += f'<td><pl-string-embed answers-name="valid{x}_{y}" size="35" placeholder="{valid[x][y]}" prefill="{valid[x][y]}" weight=1></pl-string-embed></td>'

        if empty_cache:
          input_table += '<td>' + f'<pl-string-embed allow-blank="true" answers-name="tag{x}_{y}" display="inline" remove-spaces="true" size="35" show-help-text="false"></pl-string-embed>' + '</td>'
        else:
          input_table += '<td>' + f'<pl-string-embed answers-name="tag{x}_{y}" display="inline" remove-spaces="true" size="35" show-help-text="false" placeholder="' + '{0:#0{1}x}'.format(CACHE[x]['tags'][y], tag_hex_size + 2) + '" prefill="' + '{0:#0{1}x}'.format(CACHE[x]['tags'][y], tag_hex_size + 2) + '"></pl-string-embed>' + '</td>'
        for off in range(block_size):
          start_table += f'<td>{blocks[y][off]}</td>'
          if empty_cache:
            input_table += f'<td><pl-string-embed allow-blank="true" answers-name="block{x}_{y}_{off}" size="35" weight=1></pl-string-embed></td>'
          else:
            input_table += f'<td><pl-string-embed answers-name="block{x}_{y}_{off}" size="35" placeholder="{blocks[y][off]}" prefill="{blocks[y][off]}" weight=1></pl-string-embed></td>'
            
      else:
        input_table += '<td>' + f'<pl-string-embed answers-name="tag{x}_{y}" display="inline" remove-spaces="true" size="50" show-help-text="false" placeholder="' + '{0:#0{1}x}'.format(CACHE[x]['tags'][y], tag_hex_size + 2) + '" prefill="' + '{0:#0{1}x}'.format(CACHE[x]['tags'][y], tag_hex_size + 2) + '"></pl-string-embed>' + '</td>'

    if ways > 1:
      start_table += '<td>['
      input_table += '<td>['
      for y in range(ways):
        start_table += str(CACHE[x]['lru'][y])
        input_table += f'<pl-string-embed answers-name="lru{x}_{y}" ignore-case="true" allow-blank="true" remove-spaces="true" display="inline" size="15" show-help-text="false" placeholder="' + str(lru_list[y]) + '" prefill="' + str(lru_list[y]) + '"></pl-string-embed>'
        if y < ways - 1:
          start_table += ', '
          input_table += ','
      start_table += ']</td></tr>'
      input_table += ']</td></tr>'
    start_table += '</tr>'
    input_table += '</tr>'

  data['params']['start_table'] = start_table
  data['params']['input_table'] = input_table

###########################################
### Create addresses and simulate cache ###
###########################################
  address_table = ''

  for x in range(num_addr):
    # Generate random address and update cache
    acc_tag = random.randint(0,max_tag)
    acc_idx = random.randint(0,cache_sets-1)
    acc_off = random.randint(0,block_size-1)

    addr = (acc_tag * cache_sets + acc_idx) * block_size + acc_off
    hex_address = '{0:#0{1}x}'.format(addr, addr_hex_size + 2)
    data['params']['addr' + str(x)] = hex_address

    if (x == 0) and empty_cache:
      address_table += f'<tr><td>Load <code>{hex_address}</code></td>' \
                        f'<td><pl-multiple-choice answers-name="ac{x}" fixed-order="true" inline="true">' \
                        f'<pl-answer correct="false">Hit</pl-answer>' \
                        f'<pl-answer correct="true">Miss</pl-answer>' \
                        f'</pl-multiple-choice></td></tr>'
    else:
      hit_choice = 0
      for way in range(ways):
        if (CACHE[acc_idx]['tags'][way] == acc_tag) and (valid[acc_idx][way] == 1):
          hit_choice = 1
          break

      if hit_choice == 1:
        address_table += f'<tr><td>Load <code>{hex_address}</code></td>' \
                        f'<td><pl-multiple-choice answers-name="ac{x}" fixed-order="true" inline="true">' \
                        f'<pl-answer correct="true">Hit</pl-answer>' \
                        f'<pl-answer correct="false">Miss</pl-answer>' \
                        f'</pl-multiple-choice></td></tr>'
      else:
        address_table += f'<tr><td>Load <code>{hex_address}</code></td>' \
                        f'<td><pl-multiple-choice answers-name="ac{x}" fixed-order="true" inline="true">' \
                        f'<pl-answer correct="false">Hit</pl-answer>' \
                        f'<pl-answer correct="true">Miss</pl-answer>' \
                        f'</pl-multiple-choice></td></tr>'

    update_cache(acc_tag, acc_idx, addr)

  data['params']['address_table'] = address_table


  for x in range(cache_sets):
    for y in range(ways):
      data['correct_answers'][f'valid{x}_{y}'] = str(valid[x][y])
      if empty_cache and (valid[x][y] == 0):
        data['correct_answers'][f'tag{x}_{y}'] = ''
        data['correct_answers'][f'lru{x}_{y}'] = str(CACHE[x]['lru'][y])
      else:
        data['correct_answers'][f'tag{x}_{y}'] = '{0:#0{1}x}'.format(CACHE[x]['tags'][y], tag_hex_size + 2)
        data['correct_answers'][f'lru{x}_{y}'] = str(CACHE[x]['lru'][y])

      for off in range(block_size):
        data['correct_answers'][f'block{x}_{y}_{off}'] = str(CACHE[x]['blocks'][y][off])

  return data


def update_cache(acc_tag, acc_idx, addr):
  lru_list = CACHE[acc_idx]['lru']
  ways = len(lru_list)

  block_size = len(CACHE[acc_idx]['blocks'][lru_list[0]])
  addr = addr // block_size * block_size # strip offset

  for way in range(ways):
    if (CACHE[acc_idx]['tags'][way] == acc_tag) and (valid[acc_idx][way] == 1):
      CACHE[acc_idx]['lru'] = update_lru(way, lru_list)
      return
  replaced_way = lru_list[0]
  CACHE[acc_idx]['tags'][replaced_way] = acc_tag
  valid[acc_idx][replaced_way] = 1
  for off in range(block_size):
    CACHE[acc_idx]['blocks'][replaced_way][off] = str(DATA_MEM[addr+off])
  CACHE[acc_idx]['lru'] = update_lru(lru_list[0], lru_list)

def update_lru(way, lru_list):
  ways = len(lru_list)

  for x in range(ways-1):
    if way == lru_list[x]:
      for y in range(x,len(lru_list)-1):
        lru_list[y] = lru_list[y+1]
      lru_list[len(lru_list)-1] = way
      return lru_list
  return lru_list

def parse(data):
  cache_sets = data['params']['cache_sets']
  ways = data['params']['ways']

  for x in range(cache_sets):
    for y in range(ways):
      if data['correct_answers'][f'tag{x}_{y}'] != '' and data['submitted_answers'][f'tag{x}_{y}'] != '':
        if data['submitted_answers'][f'tag{x}_{y}'][:2] != '0x':
          data['submitted_answers'][f'tag{x}_{y}'] = '0x' + data['submitted_answers'][f'tag{x}_{y}']