# iy-vhdl
## Scripts and tools for VHDL

I am using **GHDL** as my analyzer<br>
and **GTKWave** as my simulator.

This project contains a python script, which checks for syntax and compiles all the vhdl files.
It also runs a testbench, regularly (ghdl -r), and also via gtkwave.

## Using the Script
Type in the shell:
>python3 vhdl.py . full_adder_tb

to see an example of a full-adder compiled by the script