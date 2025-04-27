files = ['1.txt', '2.txt', '3.txt']
file_data = []

for file_name in files:
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file_data.append((file_name, len(lines), lines))

file_data.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in file_data:
        result_file.write(f"{file_name}\n{line_count}\n")
        result_file.writelines(lines)