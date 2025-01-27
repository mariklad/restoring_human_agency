# DESIGN 6197/4197: Special Topics
Anthropocentric Models of Making With Cooperative Robots

Spring 2025, Design Tech

Instructor: Marirena Kladeftira

![RECONFIG]([https://github.com/mariklad/restoring_human_agency/blob/main/Resources/assistive_drafting.png])

# Getting Started
## Requirements
The project uses the following 3rd party libraries:
- Rhino 7/8 & Grasshopper
- Anaconda Python
- Visual Studio Code
- Github Desktop
- Docker Community Edition

## Dependancies
- COMPAS==1.17.10
- COMPAS FAB==0.27.0
- COMPAS RRC == 1.1.0
- open3d
- opencv
- numpy==2.0.0


## Installation

### 1. Setting up the Anaconda environment with COMPAS, COMPAS_FAB AND COMPAS_RRC
```anaconda prompt terminal
(base) conda config --add channels conda-forge
```
```anaconda prompt terminal
(base) conda create -n design6197 python=3.9 -y
```
```anaconda prompt terminal
(base) conda activate design6197
```
```anaconda prompt terminal
(design6197) conda install compas-rrc
```
```anaconda prompt terminal
(design6197) conda install compas_fab==0.27.0
```
```anaconda prompt terminal
(design6197) python -m compas_rhino.install
```
### 2. Install design6197 library
```anaconda prompt terminal
(design6197) cd C:\Users\eleni\Documents\GitHub\Undo>
```
```terminal
(undo) C:\Users\eleni\Documents\GitHub\Undo> pip install -e.
```
### 3. Install Metashape module as a regular wheel package which you downloaded from [here](https://agisoft.freshdesk.com/support/solutions/articles/31000148930-how-to-install-metashape-stand-alone-python-module)
on Windows (64-bit)
```terminal
(undo) python3.exe -m pip install Metashape-2.1.2-cp37.cp38.cp39.cp310.cp311-none-win_amd64.whl
```
on mac
first, rename the wheel file you downloaded to the following: Metashape-2.1.3-cp37.cp38.cp39.cp310.cp311-abi3-macosx_11_0_universal2.macosx_10_13_x86_64.whl

```terminal
(undo) python3 -m pip install Metashape-2.1.3-cp37.cp38.cp39.cp310.cp311-abi3-macosx_11_0_universal2.macosx_10_13_x86_64.whl
```
