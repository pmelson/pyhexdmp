# pyhexdmp Python hex dump module
  #### Copyright 2021
  #### Author: Paul Melson

## Author notes:
  * Accept single variable as input, plus optional config arguments
  * Detect data type of input
  * Supported data types: str, bytes, bytearray
  * Unsupported data types: complex, bool, int, float
  * Undecided (currently unsupported): list, dict, range, tuple, memoryview
  * Convert input to bytearray()
  * Print hex output format, supported optional arguments:

    * **offsets**: on/off, default=on, print the distance of the first byte
      of each line in hex notation on the left
       ```python
       hexdmp(test_data, offsets='off')
       ```
      
    * **showascii**: on/off, default=on, print the ASCII characters of each
      byte on the right (print periods for hi/lo bytes)
       ```python
       hexdmp(test_data, showascii='off')
       ```

    * **start**: int, manually set offsets start value
      ```python
      hexdmp(test_data, start=2)
      ```

    * **width**: positive int, default=16, let the user set the number of
      bytes per line to print
       ```python
       hexdmp(test_data, width=8)
       ```
 
## Usage:
```
>>> from pyhexdmp import hexdmp
>>> with open('/home/paul/sample.exe', 'rb') as f:
...     raw = f.read()
... 
>>> test_data = raw[:128]
>>> hexdmp(test_data)
00000000: 4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00  MZ..............
00000010: b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00  ........@.......
00000020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000030: 00 00 00 00 00 00 00 00 00 00 00 00 f8 00 00 00  ................
00000040: 0e 1f ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68  ........!..L.!Th
00000050: 69 73 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f  is program canno
00000060: 74 20 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20  t be run in DOS 
00000070: 6d 6f 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00  mode....$.......
>>> hexdmp(test_data, offsets='off')
4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00  MZ..............
b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00  ........@.......
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00 00 00 00 00 00 00 00 00 00 00 00 f8 00 00 00  ................
0e 1f ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68  ........!..L.!Th
69 73 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f  is program canno
74 20 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20  t be run in DOS 
6d 6f 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00  mode....$.......
>>> hexdmp(test_data, showascii='off')
00000000: 4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00
00000010: b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00
00000020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00000030: 00 00 00 00 00 00 00 00 00 00 00 00 f8 00 00 00
00000040: 0e 1f ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68
00000050: 69 73 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f
00000060: 74 20 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20
00000070: 6d 6f 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00
>>> hexdmp(test_data, start=2)
00000002: 90 00 03 00 00 00 04 00 00 00 ff ff 00 00 b8 00  ................
00000012: 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00  ......@.........
00000022: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000032: 00 00 00 00 00 00 00 00 00 00 f8 00 00 00 0e 1f  ................
00000042: ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68 69 73  ......!..L.!This
00000052: 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f 74 20   program cannot 
00000062: 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20 6d 6f  be run in DOS mo
00000072: 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00        de....$.......
>>> hexdmp(test_data, width=8)
00000000: 4d 5a 90 00 03 00 00 00  MZ......
00000008: 04 00 00 00 ff ff 00 00  ........
00000010: b8 00 00 00 00 00 00 00  ........
00000018: 40 00 00 00 00 00 00 00  @.......
00000020: 00 00 00 00 00 00 00 00  ........
00000028: 00 00 00 00 00 00 00 00  ........
00000030: 00 00 00 00 00 00 00 00  ........
00000038: 00 00 00 00 f8 00 00 00  ........
00000040: 0e 1f ba 0e 00 b4 09 cd  ........
00000048: 21 b8 01 4c cd 21 54 68  !..L.!Th
00000050: 69 73 20 70 72 6f 67 72  is progr
00000058: 61 6d 20 63 61 6e 6e 6f  am canno
00000060: 74 20 62 65 20 72 75 6e  t be run
00000068: 20 69 6e 20 44 4f 53 20   in DOS 
00000070: 6d 6f 64 65 2e 0d 0d 0a  mode....
00000078: 24 00 00 00 00 00 00 00  $.......
>>> hexdmp(test_data, offsets='off', showascii='off', start=16, width=32)
b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 f8 00 00 00 0e 1f ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68
69 73 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f 74 20 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20
6d 6f 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00p
>>> from pyhexdmp import strhexdmp
>>> test_hexdump_string = strhexdmp(test_data)
>>> print(test_hexdump_string)
00000000: 4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00  MZ..............
00000010: b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00  ........@.......
00000020: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
00000030: 00 00 00 00 00 00 00 00 00 00 00 00 f8 00 00 00  ................
00000040: 0e 1f ba 0e 00 b4 09 cd 21 b8 01 4c cd 21 54 68  ........!..L.!Th
00000050: 69 73 20 70 72 6f 67 72 61 6d 20 63 61 6e 6e 6f  is program canno
00000060: 74 20 62 65 20 72 75 6e 20 69 6e 20 44 4f 53 20  t be run in DOS 
00000070: 6d 6f 64 65 2e 0d 0d 0a 24 00 00 00 00 00 00 00  mode....$.......

>>> 
```
