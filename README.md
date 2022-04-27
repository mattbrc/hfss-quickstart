# hfss-quickstart
Python HFSS Interface to quickly get started with design + analysis. 

Ansys High Frequency Simulation Software (HFSS) is a 3D design + analysis program for the electromagnetic spectrum. One common type of antenna that requires digital analysis prior to producing the hardware is the E-patch antenna, shown below. 

![epatch](https://user-images.githubusercontent.com/30867190/165522180-15c2fc7a-e2e5-4033-a3cd-3df839d8a16e.png)

This is a simple gui written in python that pairs with the software to quickly build an E-patch antenna in HFSS so you can focus on moving from design to testing to build. The inputs required are: the frequency (Ghz), Er1 (Dielectric constant), Height 1 (m), Er2, and Height 2 (m).

For quick start (HFSS required), type in your CLI:

```
python hfssgui.py
```
