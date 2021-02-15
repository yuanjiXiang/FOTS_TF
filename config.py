# coding:utf-8
with open('ch_words.txt', 'r', encoding='utf-8') as f:
    ch_chars = f.readlines()[0]
CHAR_VECTOR = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-~`<>'.:;^/|!?$%#@&*()[]{}_+=,\\\""
# CHAR_VECTOR = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + ch_chars
CHAR_VECTOR += ch_chars
NUM_CLASSES = len(CHAR_VECTOR) + 1

# print(NUM_CLASSES)

