def read_subjects_from_file(filename):
    subjects = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            name, time = line.split(':')
            total_hours = 0
            time = time.split()
            for activity in time:
                hours = int(''.join(filter(str.isdigit, activity)))
                total_hours += hours
            subjects[name.strip()] = total_hours
    return subjects

filename = 'subjects.txt'
subjects_dict = read_subjects_from_file(filename)
print(subjects_dict)