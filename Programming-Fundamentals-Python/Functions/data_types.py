def action(data_type, num_or_str):
    if data_type == 'int':
        result = int(num_or_str) * 2
        print(result)
    elif data_type == 'real':
        result = float(num_or_str) * 1.5
        print(f'{result:.2f}')
    elif data_type == 'string':
        result = f'${num_or_str}$'
        print(result)


input_data = input()
second_input = input()
action(input_data, second_input)
