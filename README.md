# Top-philic Dark Matter to EFT
A repository to store codes and data related to the Top-philic Dark Matter model and it's EFT limit. 

## Installation
The following external packages are needed.
The Mathematica notebooks assumes that the following packages are installed (in <home folder>/.Mathematica/Applications)[^1]:

  * [FeynArts,FormCalc,LoopTools](https://feynarts.de/)
  * [FeynRules](https://feynrules.irmp.ucl.ac.be/)
  * [FeynCalc](https://feyncalc.github.io/)
  * [FeynHelpers](https://github.com/FeynCalc/feynhelpers)
  * [Package-X](https://gitlab.com/mule-tools/package-x) (use this [tarball](./packageX.tar.gz))
  * [Matchete](https://gitlab.com/matchete/matchete)

Furthermore, in order to reproduce the LHC constraints, the following external packages are needed:
  
  * [MadGraph5](https://launchpad.net/mg5amcnlo) 
  
## Recasting and Limits

Details about recasting and the calculation of limits can be found in the [Recast](./Recast) folder.


## Folders and files

Below we describe the folders stored in this repository. Additional information about each folder can be found in their README files.

 * [auxFiles](./auxFiles): Contain mostly codes for implementing bias in MG5 event generation
 ---
 * [CDE_text](./CDE_text): folder storing the text with the path integral formalism to integrate out heavy fields from a UV model
 ---
  * [mathematicaNBs](./mathematicaNBs/): contains several mathematical notebooks for loading the models and performing the matching to obtain the EFT.
 ---
  * [modelFiles](./modelFiles): stores the FeynRules files for the models
 ---
  * [plotting](./plotting): folder storing Jupyter notebooks and code used for plotting
 ---
  * [processFolders](./processFolders): stores several process and parameter cards for generating events with MadGraph
 ---
  * [Recast_CMs](./Recast_CMS): folder to store the recasting codes
 ---
   * [Scripts](./Recast_CMS): folder to store the python Scripts related to event generation and distributions computations
 ---
  * [UFOandFAModels](./Models): stores the UFO and FeynArts output for the models
 ---
  * [xsec_processFolders](./xsec_processFolders): stores several process and parameter cards for generating events with MadGraph. This events was exclusively used in the total cross section analysis
 
   

[^1]: Make sure to include the following lines to <home folder>/Mathematica/Kernel/init.m:

     ```
     $Path = Join[
             {ToFileName[$HomeDirectory, ".Mathematica/Applications/LoopTools/x86_64-Linux/bin"],
             ToFileName[$HomeDirectory, ".Mathematica/Applications/FeynRules"],
             ToFileName[$HomeDirectory, ".Mathematica/Applications/FeynArts"],
             ToFileName[$HomeDirectory, ".Mathematica/Applications/X"]
             }, $Path]

     $FeynRulesPath = SetDirectory[FileNameJoin[{$HomeDirectory, ".Mathematica/Applications/FeynRules"}]];                          
     ```     
 
