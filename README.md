# DPR Characterization

This repository contains the tools to characterize the Dynamic Partial Reconfiguration (DPR) behavior on Heterogeneous System-on-Chip targets having this feature.  
The folder is organized as follows:
- *DPR_Injector*: folder containing the DPR Injector SW-module
- *CharacterizationResults*: folder containing the results of characterization for selected targets


## DPR Injector
The *DPR Injector* is an open-source SW-module that supports on the generation of synthetic DPR traffic. The process of DPR works by transferring a partial bitstream (pBS) from a storage memory to a reconfiguration memory of an FPGA, through a reconfiguration path.
Given as input the required pBS size (in Bytes or in Words), the DPR Injector allows to generate a pBS of the required size without performing the long and tedious DPR flow (synthesis, drawing of reconfiguration areas, implementation, and pBS generation) [1].


The module is available for two platforms: Xilinx Zynq7000 and Xilinx Zynq Ultrascale+.  
To get started:
- install python3
- clone this repository
- access the folder DPR_Injector
- access the folder of the selected target
- follow the README inside each folder


## Characterization Results
The folder contains the characterization results for Zynq Ultrascale+ target.

References:  
[1] Kizheppatt Vipin and Suhaib A. Fahmy. 2018. FPGA Dynamic and Partial Reconfiguration: A Survey of Architectures, Methods, and Applications. ACM Comput. Surv. 51, 4, Article 72 (July 2019), 39 pages.
