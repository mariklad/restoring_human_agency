# DESIGN 6197/4197: Special Topics
## Anthropocentric Models of Making With Cooperative Robots

Spring 2025, Design Tech
Instructor: Marirena Kladeftira

![ReConfig](Resources/assistive_drafting.png)


# Getting Started
## Requirements
The project uses the following 3rd party libraries:
- Rhino 7/8 & Grasshopper
- Anaconda Python
- Visual Studio Code
- Github Desktop
- Docker Community Edition

## Dependancies
- COMPAS==1.17.5
- COMPAS FAB==0.27.0
- COMPAS RRC == 1.1.0
- roslibpy == 1.7.0


## Installation

- If you have Rhino 8 and *not* Rhino 7, get a legacy key from Rhino using your Rh8 licence.
https://www.rhino3d.com/access-rhino-7/

- Open grasshopper on Rhino8 and pull a python component and run a testcode. This step will activate your Rhino python environment and the necessary folders.


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
(design6197) conda install compas_rcc=1.1.0
```
```anaconda prompt terminal
(design6197) conda install compas_fab=0.27.0
```
```anaconda prompt terminal
(design6197) conda install roslibpy=1.7.0
```
```anaconda prompt terminal
(design6197) python -m compas_rhino.install -v 7.0
```

### 3. Check installation
 Open grasshopper in Rhino. Check for the compas installed plugins.
 Pull a "compas info" component, connect the output to a panel and check that the version is correct.

 ### 4. Install additional plugins
Download Robot Components from the package manager in your Rhino or from Food4Rhino.
Restart Rhino.

You are all setup!
