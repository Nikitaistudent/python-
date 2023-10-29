
def find_common_participants(group_1, group_2, separ=","):
    split_1 = group_1.split(separ)
    split_2 = group_2.split(separ)
    ans_1 = list(set(split_1).intersection(set(split_2)))
    ans_1.sort()
    return ans_1


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print("Общие участники", find_common_participants(participants_first_group, participants_second_group,"|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
