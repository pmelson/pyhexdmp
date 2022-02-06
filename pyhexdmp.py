"""Print the contents of any variable in hex dump format"""
# pyhexdmp Python hex dump module
#
# Copyright 2021
# Author: Paul Melson

from sys import exit as sysexit


# convert str type to bytearray
def _str2ba(s):
  ba = bytearray()
  for i in range(0, len(s)):
    b = ord(s[i])
    ba.append(b)
  return ba


# convert bytes type to bytearray
def _bytes2ba(b):
  ba = bytearray()
  for i in range(0, len(b)):
    ba.append(b[i])
  return ba


# convert bytearray to printable ASCII string
def _ba2asciibytes(ba):
  ac = ''
  for i in range(0, len(ba)):
    c = ba[i]
    if 32 <= c <= 126:
      ac += chr(c)
    else:
      ac += '.'
  return ac


# main exported function, print hex dump output of data
def hexdmp(data, offsets='on', start=0, showascii='on', width=16):

  # detect data type and convert data to bytearray, else exit
  if isinstance(data, str):
    inputba = _str2ba(data)
  elif isinstance(data, bytes):
    inputba = _bytes2ba(data)
  elif isinstance(data, bytearray):
    inputba = data
  else:
    # needs proper error handling with except, this is just for debugging
    print(f"Unsupported data type: {type(data)}")
    sysexit(1)

  # check if start is set and concat inputba with start value
  if not isinstance(start, int) or start < 0:
    # reinitialize the variable instead of failing
    start = 0
    # put code here to raise an error and continue
  elif start > 0:
    inputba = inputba[start:]
  else:
    pass

  # print output loop
  # this is slow with very large (300MB+) variables, can it be made faster?
  for i in range(0, len(inputba), width):
    chunk = inputba[i:i+width]

    # right column offsets, on by default
    if offsets == 'on':
      print(f"{i+start:08x}: ", end="")

    # this line prints the actual hex bytes
    print(' '.join("{:02x}".format(k[1]) for k in enumerate(chunk)), end="")

    # prints ASCII character or . for each byte
    if showascii == 'on':
      asciichars = _ba2asciibytes(chunk)
      padding = '  '
      if len(asciichars) < width:
        spccount = (width - len(chunk))*3
        padding = padding.ljust(spccount + len(padding), ' ')
      print(f"{padding}{asciichars}")
    else:
      print()


def strhexdmp(data, offsets='on', start=0, showascii='on', width=16):

  # detect data type and convert data to bytearray, else exit
  if isinstance(data, str):
    inputba = _str2ba(data)
  elif isinstance(data, bytes):
    inputba = _bytes2ba(data)
  elif isinstance(data, bytearray):
    inputba = data
  else:
    # needs proper error handling with except, this is just for debugging
    print(f"Unsupported data type: {type(data)}")
    sysexit(1)

  # check if start is set and concat inputba with start value
  if not isinstance(start, int) or start < 0:
    # reinitialize the variable instead of failing
    start = 0
    # put code here to raise an error and continue
  elif start > 0:
    inputba = inputba[start:]
  else:
    pass

  # string construction loop
  out_string = ''
  for i in range(0, len(inputba), width):
    chunk = inputba[i:i+width]

    # right column offsets, on by default
    if offsets == 'on':
      out_string += f"{i+start:08x}: "

    # this line prints the actual hex bytes
    out_string += ' '.join("{:02x}".format(k[1]) for k in enumerate(chunk))

    # prints ASCII character or . for each byte
    if showascii == 'on':
      asciichars = _ba2asciibytes(chunk)
      padding = '  '
      if len(asciichars) < width:
        spccount = (width - len(chunk))*3
        padding = padding.ljust(spccount + len(padding), ' ')
      out_string += f"{padding}{asciichars}"
      out_string += "\n"
    else:
      out_string += "\n"

  return out_string
