#!/usr/bin/env python
def break_words(stuff):
    """
    This function will break up words for us.
    这个功能会为我们打破单词
    """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """
    Sorts the words.
    对单词进行排序。
    """
    return sorted(words)

def print_first_word(words):
    """
    Prints the frist word after popping it off
    弹出后打印第一个单词。
    """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """
    Prints the last word after popping it off.
    弹出后打印最后一个单词。
    """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """
    Takes in a full sentence and returns the sorted words.
     接受完整的句子并返回已排序的单词。
    """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """
    Prints the first and last words of the sentence.
    打印句子的第一个和最后一个单词。
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """
    Sorts the words then prints the first and last one.
    对单词进行排序然后打印第一个和最后一个。
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
