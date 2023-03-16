# DPR Injector for Xilinx Zynq Ultrascale +


To run the DPR_Injector for Xilinx Zynq Ultrascale+ platforms, first install Python 3.  
To have a pBS of a given size in bytes, execute:

```
python3 DPRInject.py -b <sizeBytesOf_pBS>
```
where the \<sizeBytesOf_pBS\> is the size of pBS in Bytes.  
To have a pBS of a given size in Words (Words are 4 Bytes for Xilinx Zynq Ultrascale+), execute:

```
python3 DPRInject.py -w <sizeWordsOf_pBS>
```

where \<sizeBytesOf_pBS\> is the size of pBS in Words.

The resulting pBS will be stored in the working folder.
