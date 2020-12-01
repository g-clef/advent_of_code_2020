input_file = "input.txt"

inputs = list()

with open(input_file) as filehandle:
    for line in filehandle:
        inputs.append(int(line.strip()))

inputs_as_set = set(inputs)

inputs.sort()

done = False

for start_val in inputs:
    compliment = 2020 - start_val
    if compliment in inputs_as_set:
        print(start_val * compliment)
        break


done = False
inner_done = False
for start_index in range(len(inputs)):
    start_val = inputs[start_index]
    start_compliment = 2020 - start_val
    for end_index in range(len(inputs)-1, start_index, -1):
        end_val = inputs[end_index]
        if end_val > start_compliment:
            continue
        end_compliment = start_compliment - end_val
        if end_compliment in inputs_as_set:
            print(start_val * end_val * end_compliment)
            done = True
            break
        if done is True:
            break
    if done is True:
        break
