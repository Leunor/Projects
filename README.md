# Practise Crypto

def cipher_coder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

def cipher_decoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message

def vigenere_coder(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    decoded_message = ""
    key_word_phrase = ""
    value = 0
    for i in range(0, len(message)):
        if message[i] in punctuation:
            key_word_phrase += message[i]
        else:
            key_word_phrase += keyword[value]
            value = (value+1)%len(keyword)
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            combined_letter_value = alphabet.find(message[i]) + alphabet.find(key_word_phrase[i])
            decoded_message += alphabet[combined_letter_value % 26]
        else:
            decoded_message += message[i]
    return decoded_message

def vigenere_decoder(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ""
    key_word_phrase = ""
    value = 0                #possibly that value should equal to -1 otherwise keywordphrase will not include first letter of keyword
    for i in range(0, len(message)):
        if message[i] in punctuation:
            key_word_phrase += message[i]
        else:
            key_word_phrase += keyword[value] #if line 13 and line 14 was swapped then value must equal to -1 and not 0
            value = (value+1)%len(keyword)    #this is because line 14 would be executed first meaning value = 1 not 0. however if the 2 lines are note swapped and stays in this order then the value = 0 then it will equal 1 then 2 and so on
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            combined_letter_value = alphabet.find(message[i]) - alphabet.find(key_word_phrase[i])
            translated_message += alphabet[combined_letter_value % 26]
        else:
            translated_message += message[i]
    return translated_message
