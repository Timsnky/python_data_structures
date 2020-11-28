# Put your code here
input_file = input("Enter the input file: ")
output_file = input("Enter the output file: ")

f_input = open(input_file, "r")
f_output = open(output_file, "w")

line_number = 1
for line in f_input:
    line = str(line_number) + "> " + line
    f_output.write(line.rjust(len(line) + 4))
    line_number += 1

f_input.close()
f_output.close()