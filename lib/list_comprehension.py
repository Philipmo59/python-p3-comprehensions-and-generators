#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]
    return even_nums

def make_exclamation(sentence_list):
    # new_sentence = [word + "!" for word in sentence_list]
    new_sentence = [[] if word == "" else word + "!" for word in sentence_list]
    return new_sentence

make_exclamation([])