#!/usr/bin/python3
def multiple_returns(sentence):
    tupla_len = len(sentence)
    if tupla_len == 0:
        tupla_final = (tupla_len, None)
    else:
        tupla_letra = sentence[0]
        tupla_final = (tupla_len, tupla_letra)
    return tupla_final
