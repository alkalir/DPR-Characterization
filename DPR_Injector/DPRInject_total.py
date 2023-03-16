#!/usr/bin/python3
import math
import struct
import binascii
import sys, getopt
import pathlib

BIT = 0x00
BIN = 0xff

BIT_STREAM_MAX_BYTES  =  0x01130000  
XST_FAILURE = 1
GLOBAL_bitOrBin = BIN



class BSINFO:
  size_b = 0
  size_w = 0
  ddr_address = 0x00200000 
  valid = False
  bsname = "somename"
  

def HeadGeneration():
  headIndex = 0
  headBuf = [0 for i in range(30)]
  headIndex = 0
  headBuf[headIndex] = 0xFFFFFFFF  # /*  01 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  02 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  03 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  04 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  05 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  06 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  07 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  08 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  09 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  10 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  11 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  12 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  13 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  14 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  15 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  16 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0x000000BB  # /*  17 */  /* Bus Width Sync Word */
  headIndex += 1
  headBuf[headIndex] = 0x11220044  # /*  18 */  /* Bus Width Detect */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  19 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xFFFFFFFF  # /*  20 */  /* Dummy Word */
  headIndex += 1
  headBuf[headIndex] = 0xAA995566  # /*  21 */  /* Sync Word */
  headIndex += 1
  headBuf[headIndex] = 0x20000000  # /*  22 */  /* Type 1 NOOP Word 0 */
  headIndex += 1
  return headBuf,headIndex


def TailGeneration():
  tailIndex = 0
  tailBuf = [0 for i in range(30)]
  tailIndex = 0
  tailBuf[tailIndex] = 0x30008001 # /*  01 */  /* Type 1 write CMD register */
  tailIndex += 1
  tailBuf[tailIndex] = 0x0000000D # /*  02 */  /* DESYNC */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  03 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  04 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  05 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  06 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  07 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  08 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  09 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  10 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  11 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  12 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  13 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  14 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  15 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  16 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  17 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  tailBuf[tailIndex] = 0x20000000 # /*  18 */  /* Type 1 NOOP Word 0 */
  tailIndex += 1
  return tailBuf,tailIndex


def write_word(fout, word):
  if fout:
    if(GLOBAL_bitOrBin == BIN):
      word = word[::-1] #reverse endianness
    fout.write(word)



def Generate_NOP_BS(sizeWords, bsnfo):
  nops_count = 0
  nop = 0x20000000


  bsnfo.valid = False
  if((sizeWords < 40) | ((sizeWords * 4) > BIT_STREAM_MAX_BYTES)):
    print("ERROR::Generate_NOP_BS: 40 < sizeWords < 4505600 !!!")
    return XST_FAILURE
  
  print("have to generate {} words".format(sizeWords))

  #head
  [headBuf,headIndex] = HeadGeneration()
  
  #tail
  [tailBuf,tailIndex] = TailGeneration()

  
  #NOPs
  nops_count = sizeWords - (headIndex + tailIndex)
  print("nops_count={}".format(nops_count))


  for i in range(headIndex):
    write_word(bsnfo.f_handle, struct.pack('>I', headBuf[i])) 


  for i in range(nops_count):
    write_word(bsnfo.f_handle, struct.pack('>I', nop)) 


  for i in range(tailIndex):
    write_word(bsnfo.f_handle, struct.pack('>I', tailBuf[i])) 




def query_yes_no(question, default="yes"):
  """Ask a yes/no question via raw_input() and return their answer.
  
  "question" is a string that is presented to the user.
  "default" is the presumed answer if the user just hits <Enter>.
          It must be "yes" (the default), "no" or None (meaning
          an answer is required of the user).
  
  The "answer" return value is True for "yes" or False for "no".
  """
  valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
  if default is None:
    prompt = " [y/n] "
  elif default == "yes":
    prompt = " [Y/n] "
  elif default == "no":
    prompt = " [y/N] "
  else:
    raise ValueError("invalid default answer: '%s'" % default)
  
  while True:
    sys.stdout.write(question + prompt)
    choice = input().lower()
    if default is not None and choice == "":
      return valid[default]
    elif choice in valid:
      return valid[choice]
    else:
      sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")


def main(argv):
  
  outputfile = ''
  bopt = False
  wopt = False  
  ofopt = False
  platopt = False
  
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
    elif opt in ("-w", "--wordsize"):
      wopt = True
      w_size = int(arg)
    elif opt in ("-o", "--ofile"):
      outputfile = arg
      ofopt = True
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
  
  if not ofopt:
    floc = pathlib.Path(".").parent
    outputfile = pathlib.Path(floc) / 'F{}w.bin'.format(w_size)
  else:
    outputfile = pathlib.Path(outputfile)
  
  #prevent to overwrite something
  if outputfile.exists():
    if not query_yes_no('\nOUT FILE:{} already exists! Overwrite it?'.format(outputfile), default="no"):
      sys.exit()
    print('')
  else:
    print('\nOUT FILE: {}\n'.format(outputfile))
  
  fo = open(outputfile, "wb")

  bi = BSINFO()
  bi.bsname = outputfile
  bi.f_handle = fo
  
  Generate_NOP_BS(w_size, bi)
  
  if not fo is None:
    fo.close()
    

if __name__ == "__main__":
  main(sys.argv[1:])
