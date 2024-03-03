import json
import math
import random


def generate(data):
##########################################################
##GOAL IS TO CREATE A JSON THAT LOOKS LIKE THE FOLLOWING##
##########################################################
#  { "signal" : [
#  { "name": "clk",  "wave": "lP....." },
#  { "name": "reset",  "wave": "10..........", "period": 0.5},
#  { "name": "waddr",  "wave": "01..0..1.0..", "period": 0.5},
#  { "name": "wdata",  "wave": "=..=.=.=.=..", "data": ["0xa", "0x1", "0x5", "0xf", "0xe"], "period": 0.5},
#  { "name": "w_en", "wave": "0101.." },
#  { "name": "raddrA", "wave": "1.0..1......", "period": 0.5 },
#  { "name": "rdataA",  "wave": "=.==.=..=...", "data": ["0xa", "0x1", "0x5", "0xf", "0xe"], "period": 0.5},
#  { "name": "raddrB", "wave": "1.0..1......", "period": 0.5 },
#  { "name": "rdataB",  "wave": "=.==.=..=...", "data": ["0xa", "0x1", "0x5", "0xf", "0xe"], "period": 0.5}
#],
#  "config" : { "hscale" : 1.5 },
#   "head":{
#   tick:0
# }
#}

  # values to put in the wave portion of the JSON
  wire_val = ['0','1']
  bus_sym = ['=','.']

  #strings for data portion of the JSON
  addr_val = ['0','1','2','3']
  data_val = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

  #register file
  reg_data = ['?','?','?','?']

  ITERS = 8

  # Create the start of waveform JSONs
  # Wires and buses need to different starting and closing forms 
  wave_preamble = '{ "signal" : ['
  wave_clock = '{"name": "clk",  "wave": "lP.." },' # number of symbols in clk should be half of iters
  wave_reset = '{ "name": "reset",  "wave": "0..." },'
  wave_w_en = '{ "name": "w_en", "wave": "'
  wave_waddr = '{ "name": "waddr",  "wave": "='
  wave_wdata = '{ "name": "wdata",  "wave": "='
  wave_raddrA = '{ "name": "raddrA",  "wave": "='
  wave_raddrB = '{ "name": "raddrB",  "wave": "='
  wave_rdataA_blank = '{}, { "name": "rdataA",  "wave": "xxxx" },'
  wave_rdataB_blank = '{}, { "name": "rdataB",  "wave": "xxxx" },'

  # Create lists of values for waveforms
  w_en_vals = random.choices(wire_val, weights = [1,4], k = ITERS) # choose four random values for w_en, weight toward 1
  waddr_vals = random.choices(addr_val, weights = [1,1,1,1], k = ITERS) # choose four random values for waddr
  raddrA_vals = random.choices(addr_val, weights = [1,1,1,1], k = ITERS) # choose four random values for waddr
  raddrB_vals = random.choices(addr_val, weights = [1,1,1,1], k = ITERS) # choose four random values for waddr
  wdata_vals = random.choices(data_val, weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = ITERS) # choose four random values for wdata

  #initialize register file
  reg_data = random.choices(data_val, weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 4)

  for x in range(4):
    data["params"][f"reg{x}"] = reg_data[x]

  data["correct_answers"][f"regA_0"] = reg_data[int(raddrA_vals[0])]
  data["correct_answers"][f"regB_0"] = reg_data[int(raddrB_vals[0])]

  # Convert initial values to JSON format
  wave_w_en = wave_w_en + w_en_vals[0]
  waddr_post = '", "data": ["' + waddr_vals[0] + '"'
  wdata_post = '", "data": ["' + wdata_vals[0] + '"'
  raddrA_post = '", "data": ["' + raddrA_vals[0] + '"'
  raddrB_post = '", "data": ["' + raddrB_vals[0] + '"'

  cycle = 0
  for ii in range(1,ITERS):
    if w_en_vals[ii-1] == w_en_vals[ii]:
      wave_w_en = wave_w_en + '.'
    else:
      wave_w_en = wave_w_en + w_en_vals[ii]

    if waddr_vals[ii-1] == waddr_vals[ii]:
      wave_waddr = wave_waddr + '.'
    else:
      wave_waddr = wave_waddr + '='
      waddr_post = waddr_post + ', "' + waddr_vals[ii] + '"'

    if wdata_vals[ii-1] == wdata_vals[ii]:
      wave_wdata = wave_wdata + '.'
    else:
      wave_wdata = wave_wdata + '='
      wdata_post = wdata_post + ', "' + wdata_vals[ii] + '"'

    if raddrA_vals[ii-1] == raddrA_vals[ii]:
      wave_raddrA = wave_raddrA + '.'
    else:
      wave_raddrA = wave_raddrA + '='
      raddrA_post = raddrA_post + ', "' + raddrA_vals[ii] + '"'

    if raddrB_vals[ii-1] == raddrB_vals[ii]:
      wave_raddrB = wave_raddrB + '.'
    else:
      wave_raddrB = wave_raddrB + '='
      raddrB_post = raddrB_post + ', "' + raddrB_vals[ii] + '"'

    data["correct_answers"][f"regA_{str(ii)}"] = reg_data[int(raddrA_vals[ii])]
    data["correct_answers"][f"regB_{str(ii)}"] = reg_data[int(raddrB_vals[ii])]

    if ((ii % 2) == 1) and (ii != ITERS-1):
      if (w_en_vals[ii] == '1'):
        reg_data[int(waddr_vals[ii])] = wdata_vals[ii]


  # Period: 0.5 makes the following signals change twice as often as clk, so they need twice as many values as clk
  wave_w_en = wave_w_en + '", "period": 0.5},'
  wave_waddr = wave_waddr + waddr_post + '], "period": 0.5},'
  wave_wdata = wave_wdata + wdata_post + '], "period": 0.5},'
  wave_raddrA = wave_raddrA + raddrA_post + '], "period": 0.5},'
  wave_raddrB = wave_raddrB + raddrB_post + '], "period": 0.5},'
  wave_postlude = '],  "config" : {"hscale":4}, "head":{"tick":0}}'

  data["params"]["waveform"] = wave_preamble + wave_clock + wave_reset + wave_w_en + wave_waddr + wave_wdata + wave_raddrA + wave_raddrB + wave_rdataA_blank + wave_rdataB_blank + wave_postlude
  for ii in range(4):
    data["correct_answers"]["reg_data" + str(ii)] = reg_data[ii]

  return data
