import subprocess


print(subprocess.check_output(['sysctl', '-n', 'machdep.cpu.brand_string']))
print(subprocess.check_output([
    'top', '-l', '1', '|', 'head', '-n', '10', '|', 'grep', 'PhysMem'
]))
