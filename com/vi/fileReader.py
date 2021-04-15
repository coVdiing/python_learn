file_name = 'pi_digists.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print line.rstrip()