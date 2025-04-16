# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]

# string = input("Введите строку: ")
# if is_palindrome(string):
#     print("Строка является палиндромом")
# else:
#     print("Строка не является палиндромом")



# def extract_digits(num):
#     if 100 <= num <= 999:
#         hundreds = num // 100
#         tens = (num % 100) // 10 
#         units = num % 10  
#         print(f"сотни - {hundreds}, десятки - {tens}, единицы - {units}")
#     else:
#         print("Число должно быть трехзначным!")
# num = int(input("введите трехзначное число: "))
# extract_digits(num)



# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))

# a = [1, 2, 3, 4, 5]
# b = [3, 5, 6, 7, 8]
# common = common_elements(a, b)
# print(f"Общие элементы: {common}")



# def pad_strings(strings):
#     if not strings:
#         return []
#     max_len = max(len(s) for s in strings)
#     padded_strings = [s + "_" * (max_len - len(s)) for s in strings]
#     return padded_strings

# my_strings = ["a", "bb", "ccc", "dddd"]
# padded_list = pad_strings(my_strings)
# print(padded_list)



# def calculate_quarterly_grade():
#     grades = list(map(int, input("Введите оценки через запятую: ").split(',')))
#     valid_grades = []
#     i = 0
#     while i < len(grades):
#         if grades[i] == 2:
#             if i + 1 < len(grades) and grades[i+1] != 2:
#                 i += 2 
#             else:
#                 valid_grades.append(grades[i])
#                 i += 1
#         else:
#             valid_grades.append(grades[i])
#             i += 1

#     if valid_grades:
#         print("Итоговая оценка:", round(sum(valid_grades) / len(valid_grades)))
#     else:
#         print("Нет оценок для расчета.")
# calculate_quarterly_grade()



# def quiz():
#     questions = {
#         "Столица Франции?": "Париж",
#         "Планет в Солнечной системе?": "Восемь",
#         "Жидкость в глазном яблоке?": "Слеза"
#     }
#     score = 0
#     for q, a in questions.items():
#         if input(q + " ").lower() == a.lower():
#             score += 1
#             print("Верно!")
#         else:
#             print("Неверно! Ответ:", a)
#     print(f"Результат: {score}/{len(questions)}")
# quiz()



# points = {
#         1: 'AEIOULNSTR',
#         2: 'DG',
#         3: 'BCMP',
#         4: 'FHVWY',
#         5: 'K',
#         8: 'JZ',
#         10: 'QZ'
#     }

# word = input("Введите слово: ")
# word = word.upper()
# total_score = 0

# for letter in word:
#     for score, letters in points.items():
#         if letter in letters:
#             total_score += score
#             break 
# print(total_score)


# def lists(list1, list2):
#     result = []
#     for i in range(max(len(list1), len(list2))):
#         if i < len(list1):
#             result.append(list1[i])
#         if i < len(list2):
#             result.append(list2[i])
#     return result

# list_a = [1, 2, 3]
# list_b = [11, 22, 33]
# interleaved_list = lists(list_a, list_b)
# print(interleaved_list)  


# def remove_by_indexes(my_list, index1, index2):
#     list_length = len(my_list)
#     if index1 >= 0 and index1 < list_length and index2 >= 0 and index2 < list_length:

#         new_list = []

#         i = 0
#         while i < list_length:
#             if i != index1 and i != index2:
#                 new_list.append(my_list[i])
#             i = i + 1
#         return new_list
#     else:
#         print("Индексы должны быть больше или равны нулю и меньше длины списка.")
#         return my_list
# my_list = [1, 44, 7, 9, 3, 2, 1, 44]
# index1 = 0
# index2 = 4
# new_list = remove_by_indexes(my_list, index1, index2)
# print(new_list)



# def count_zeros(number):

#     number_str = str(number)

#     count = 0
#     i = len(number_str) - 1

#     while i >= 0 and number_str[i] == '0':
#         count = count + 1
#         i = i - 1
#     return count
# number = int(input("Введите число: "))
# zeros = count_zeros(number)
# print("Количество нулей в конце:", zeros)



# def find_nearest_number(numbers, target):

#     if not numbers:
#         return None
    
#     nearest_number = numbers[0]
#     min_difference = abs(numbers[0] - target)
#     i = 1

#     while i < len(numbers):
#         difference = abs(numbers[i] - target)

#         if difference < min_difference:
#             min_difference = difference 
#             nearest_number = numbers[i]
#         i = i + 1
#     return nearest_number
# numbers = [17, 4, 7, 10, 11, 12]
# target = int(input("Введите искомое число: "))
# nearest = find_nearest_number(numbers, target)
# print("Ближайшее число:", nearest)




def extract_string_between_symbols(text, symbol1, symbol2):

    start_position = text.find(symbol1)
    end_position = text.find(symbol2)

    if start_position != -1 and end_position != -1:
        if end_position > start_position:
            extracted_string = text[start_position + 1:end_position]
            print("Результат:", extracted_string)
        else:
            print("Второй символ должен быть после первого.")
    else:
        print("Один или оба символа не найдены в строке.")

text = input("Введите строку: ")
symbol1 = input("Введите символ начала: ")
symbol2 = input("Введите символ конца: ")
extract_string_between_symbols(text, symbol1, symbol2)
