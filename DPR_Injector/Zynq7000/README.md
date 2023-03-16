# DPR Injector for Xilinx Zynq Ultrascale +


To run the DPR_Injector for Xilinx Zynq Ultrascale+ platforms, install Python 3 and execute:

```
python3 DPRInject.py -b <sizeBytesOf_pBS>
```
or
```
python3 DPRInject.py -w <sizeWordsOf_pBS>
```

where:
- \<sizeBytesOf_pBS\> is the size of pBS in Bytes
- \<sizeBytesOf_pBS\> is the size of pBS in Words (Words are 4 Bytes for Xilinx Zynq Ultrascale+).

The resulting pBS will be stored in the working folder.
