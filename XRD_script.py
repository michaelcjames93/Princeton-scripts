"""
A script that takes a .xy XRD file and outputs the normalized intensity
$python XRD_script.py input.xy
"""
import sys
if len(sys.argv)!=2:
    sys.exit("Enter correct number of command-line arguments.")
try:
    data=[]
    with open(sys.argv[1], "r") as f:
        for line in f:
            line=line.strip("\n")
            a, b = line.split(" ")
            data.append(b)
except FileNotFoundError:
    sys.exit("Invalid inputs")

data=data[1:]
float_data=[]
for line in data:
    line=float(line)
    float_data.append(line)
max_value = max(float_data)
norm_data=[]
for line in float_data:
    line=line/max_value
    norm_data.append(line)
with open("output.txt", "w") as f:
    for line in norm_data:
        f.writelines(str(line)+"\n")
