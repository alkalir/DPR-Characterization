# DPR Injector for Xilinx Zynq7000


To run the DPR_Injector for Xilinx Zynq7000 platforms, install Python 3 and execute:

```
python3 DPRInject_zynq7000.py -b <sizeBytesOf_pBS>
```
or
```
python3 DPRInject_zynq7000.py -w <sizeWordsOf_pBS>
```

where:
- \<sizeBytesOf_pBS\> is the size of pBS in Bytes
- \<sizeBytesOf_pBS\> is the size of pBS in Words (Words are 4 Bytes for Xilinx Zynq7000).

The resulting pBS will be stored in the working folder.
