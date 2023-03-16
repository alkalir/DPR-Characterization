#!/usr/bin/python3

import math
import sys
import getopt
import os

def main(argv):
  
  outputfile = ''
  bopt = False
  wopt = False
  ofopt = False
  platopt = False

  pythonCommandFlag = ""

  print('Start DPR Injector')

  try:
    opts, args = getopt.getopt(argv,"hb:w:o:p:",["bytesize=","wordsize=","ofile=", "platform="])
  except getopt.GetoptError:
    print('bitstream_nop_generator.py -b <size in Bytes> -w <size in Words> -o <outputfile> -p <platform>')
    sys.exit(2)

  for opt, arg in opts:
    print('opt={} arg={}'.format(opt, arg))
    if opt == '-h':
      print('bitstream_nop_generator.py -b <size in Bytes> -w <size in Words> -o <outputfile> -p <platform>')
      sys.exit()
    elif opt in ("-b", "--bytesize"):
      bopt = True
      b_size = int(arg)
      pythonCommandFlag += " -b " + arg
    elif opt in ("-w", "--wordsize"):
      wopt = True
      w_size = int(arg)
      pythonCommandFlag += " -w " + arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
      ofopt = True
      pythonCommandFlag += " -o " + arg
    elif opt in ("-p", "--platform"):
      platform = arg
      platopt = True

  #check dimension
  if not bopt and not wopt:
    print('Please specify size in Bytes (option -b) or size in Words (option -w)')
    sys.exit()
  elif bopt and wopt:
    if (w_size*4 != b_size):
      print('Please specify size in Bytes (option -b) OR size in Words (option -w)...')
      print('... OR at least be coherent!')
      sys.exit()
  elif bopt:
    w_size = math.floor(b_size/4)
    if(b_size%4 != 0):
      print('Size in Bytes should be a multiple of 32bit words, so a multiple of 4')
      print('A size of {} Bytes, {} Words, will be used'.format(w_size*4,w_size))

  #at this point we have size in words
  print("Filesize will be: {} Bytes ({} Words)".format(w_size*4,w_size))

  if not platopt:
    print('Please specify platform type (option -p)')
    print('Available platform are:')
    print('Zynq7000')
    print('ZUS')
    sys.exit()
  elif platform == "Zynq7000":
    print('Starting bitstream for Zynq7000...')
    directory = os.getcwd()
    directory += "\Zynq7000"
    os.chdir(directory)
    pythonCommand = "python DPRInject_zynq7000.py " + pythonCommandFlag
    os.system(pythonCommand)
    print('Bitstream created!!!')
  elif platform == "ZUS":
    print('Starting bitstream for ZUS...')
    directory = os.getcwd()
    directory += "\ZynqUltrascale+"
    os.chdir(directory)
    pythonCommand = "python DPRInject_zus.py " + pythonCommandFlag
    os.system(pythonCommand)
    print('Bitstream created!!!')
  else:
    print('Incorrect platform type (option -p)')
    print('Available platform are:')
    print('Zynq7000')
    print('ZUS')

  print('Stop DPR Injector')

if __name__ == "__main__":
  main(sys.argv[1:])



