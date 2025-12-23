# Recast

Contains python scripts and config files used to run scans or to get distributions of the MC events

## Folders and files

* [runScanMG5.py](runScanMG5.py): python code for running scans over the parameter space and generating events with MadGraph
 * [setenv.sh](setenv.sh): bash script for setting the environment variables needed for running runScanMG5.py
 * [configParserWrapper.py](configParserWrapper.py): auxiliary parser used by runScanMG5.py
 * scan_parameters_xx.ini: several parameter files for running scans
 
  * [GetDists.py](GetDists.py): python script to extract distribution from the MC eventts
  
  * [getXsec.py](getXsec.py): python script to extract the cross section computed by MG5
