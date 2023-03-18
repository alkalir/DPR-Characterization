# DPR Injector


This folder contains the DPR_Injector SW-module. It is organized as follows:
- *DPRInject_total.py* - Main Python script
- *Zynq7000* - Folder for Xilinx Zynq7000 functions. It contains also pBS results.
- *Zynq UltraScale+* - Folder for Xilinx Zynq Ultrascale+ functions. It contains also pBS results.

To run the DPR_Injector, first install Python 3.  
To have a pBS of a given size in bytes, for a given platform, execute (from this folder):

```
python3 DPRInject_total.py -b <sizeBytesOf_pBS> -p <platform>
```
where:
- *\<sizeBytesOf_pBS\>* is the size of pBS in Bytes
- *platform* is the type of platform, that can be:
  - *Zynq7000*, to generate the pBS for a Xilinx Zynq7000;
  - *ZUS+*, to generate the pBS for a Xilinx Zynq Ultrascale+;

To have a pBS of a given size in Words, for a given platform, execute:

```
python3 DPRInject_total.py -w <sizeWordsOf_pBS> -p <platform>
```

where *\<sizeWordsOf_pBS\>* is the size of pBS in Words.  
Please note that the size of a Word depends on the selected platform. For both Xilinx Zynq7000 and Xilinx Zynq Ultrascale+ the size of a Word is 4 Bytes.

The resulting pBS will be stored in the corresponding platform folder.
