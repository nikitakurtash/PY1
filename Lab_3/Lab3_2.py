def find_common_participants(str1, str2, delimiter=','):
    sim_1 = str1.split(delimiter)
    sim_2 = str2.split(delimiter)
    common_participants = list(set(sim_1) & set(sim_2))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие: ", find_common_participants(participants_first_group, participants_second_group, '|'))
