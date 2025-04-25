import json

def parse_file_to_firms(filename):
    firms = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 4:
                name, _, revenue, costs = parts
                revenue, costs = int(revenue), int(costs)
                profit = revenue - costs
                firms.append((name, profit))
    return firms

def count_average_profit(firms):
    total_profit = 0
    profitable_count = 0

    for _, profit in firms:
        if profit > 0:
            total_profit += profit
            profitable_count += 1

    average_profit = total_profit / profitable_count
    return average_profit

def create_result_data(firms):
    firms_dict = {name: profit for name, profit in firms}
    average_profit = count_average_profit(firms)
    result = [firms_dict, {"average_profit": average_profit}]
    return result

def save_result_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

input_filename = 'firms.txt'
output_filename = 'firms_profit.json'

firms = parse_file_to_firms(input_filename)
result_data = create_result_data(firms)

save_result_to_json(result_data, output_filename)
print(f"Результаты сохранены в файл {output_filename}")