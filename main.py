
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#text = 'Напишите напишитеабв програбвмму программу, удаляющую из \
    #этого текста абв все вабвс слова, содержащиеабв содержащие "абв"'

# 1
#def delete_words(text):
#    text = list(filter(lambda x: 'абв' not in x, text.split()))
#    return " ".join(text)

#text = delete_words(text)
#print(text)


# 2
# result = ' '.join(filter(lambda w: w[0] not in ['абв'], text.split()))
# print(result)

# игра крестики-нолики

# print("*" * 10, "Крестики-нолики", "*" * 10)
#
# board = list(range(1,10))
# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-" * 13)
# #draw_board(board) посмотреть поле
#
# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставить: " + player_token + "? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Неверный ввод.")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if(str(board[player_answer - 1]) not in "XO"):
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка занята")
#         else:
#             print("Введите число от 1 до 9")
#
# def check_win(board):
#     win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#         return False
#
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "Ты выиграл")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья")
#             break
#     draw_board(board)
# main(board)


#  RLE алгоритм

# def encode(s):
#     encoding = ""
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         encoding += str(count) + s[i]
#         i = i + 1
#     return encoding
# if __name__ == '__main__':
#     s = 'ABBCCCD'
#     print(encode(s))



