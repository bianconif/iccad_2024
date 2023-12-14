# Sensitivity of radiomics features to region volume: A CT phantom study

### By Usama Muhammad Khan, Francesco Bianconi, Mario L. Fravolini and Barbara Palumbo

### Submitted to the [8th International Conference on Control, Automation and DIagnosis - ICCAD'24](https://www.iccad-conf.com/)

## Supplementary material

### Data source
- [ImSURE isotropic phantom](https://figshare.com/articles/dataset/ImSURE_Isotropic_Phantom/16669228?backTo=/collections/ImSURE_Phantoms/5625439)
- [ROIs (in .nii format)](data/ROIs.zip)

### Feature extraction
- [LIFEx](https://www.lifexsoft.org/) scripts for feature extraction (for LIFEx 7.4.0)
 - [Absolute resampling](lifex_scripts/Script_ImSURE_Absolute.tex)
 - [Relative resampling](lifex_scripts/Script_ImSURE_Relatice.tex)

To execute the scripts set the `*IMAGE` path to the folder containing the DICOM files and the `*RoiVolume` path to the folder containing the ROIs.  

### Results
- LIFEx output files (settings + computed features)
 - [Absolute resampling](data/Texture_ImSure_Absolute.csv)
 - [Relative resampling](data/Texture_ImSure_Relative.csv)
- By-feature correlation table
 - [Absolute resampling](data/corr_table_absolute.csv)
 - [Relative resampling](data/corr_table_relative.csv)

#### License
Unless otherwise specified the material on this repository is available under [CC BY 4.0 Deed | Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).