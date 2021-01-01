'''
This script will check syntax, compile and run regularly and in gtkwave
'''

import sys
import os
import shutil
import subprocess

if len(sys.argv) < 3:
	print("Usage: {} <path> <test bench entity name>".format(sys.argv[0]))
	sys.exit(1)

(_, path, top_level) = sys.argv

build_path = path + '/build'
files_to_move = []


# Get a list of all the vhdl files in the current directory
vhdl_files = [fname for fname in os.listdir(path) if fname.endswith('.vhdl') or fname.endswith('.vhd')]

try:os.mkdir(build_path)
except:pass

# syntax
print('\nChecking for syntax:')
good_syntax = True
for fname in vhdl_files:
	ret_code = subprocess.call(['ghdl', '-s', fname])
	if ret_code == 0:
		print(fname, "--good syntax")
	else:
		print(fname, "--must be checked for syntax errors")
		good_syntax = False

if not good_syntax:
	print("Everything must have good syntax before analysis")
	sys.exit(1)

# analysis (compilation)
print('\nAnalyzing:')
analyzed = True
for fname in vhdl_files:
	ret_code = subprocess.call(['ghdl', '-a', fname])
	if ret_code == 0:
		print(fname, "--analized")
		files_to_move.append(fname.split('.vhd')[0] + '.o')
	else:
		analyzed = False

files_to_move.append('work-obj93.cf')

if not analyzed:
	print("Analysis Failed")
	sys.exit(1)

# Evaluation
print('\nEvaluating:')
ret_code = subprocess.call(['ghdl', '-e', top_level])
files_to_move.append(top_level)
print(top_level, '--evaluated')

# run the test bench
print('\nRunning simulation:')
vcd_file_name = top_level + '.vcd'
ret_code = subprocess.call(['ghdl', '-r', top_level, '--vcd='+vcd_file_name])
files_to_move.append('e~{}.o'.format(top_level))
files_to_move.append(vcd_file_name)

# move everything to ./build/
print('\nMoving files into the build directory:')
for fname in files_to_move:
	shutil.move(fname, os.path.abspath('{}/{}'.format(build_path, fname)))

# Run GTKWave Simulator
print('\nRunning simulation in GTKWave :)')
ret_code = subprocess.call(['gtkwave', '{}/{}.vcd'.format(build_path, top_level)])

print('\nFarewell, Mighty Coder <3')