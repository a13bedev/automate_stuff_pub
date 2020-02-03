# '_elementary' in the file name means that program is quite naive.
# the logic is straight forward
# it doesn't use regex
# it uses simple python functions and slices
# code is suitable for beginners
"""
What program do:
-  reads in the text file
-  lets the USER add their own text anywhere the words ADJECTIVE, NOUN, ADVERB or VERB
   appear in the text file.
"""

import os

try:
    # Read a file and stores it's content as a string.
    path = input("Enter a path to the file.")
    textFile = open(path)
    text = textFile.read()
    textFile.close()

    # Find all occurrences of words 'ADJECTIVE', 'NOUN', 'ADVERB', 'VERB'.
    # Store them in variable 'matches'
    words = {'ADJECTIVE', 'ADVERB', 'NOUN', 'VERB'}
    matches = []
    for word in words:
        start_index = 0
        word_length = len(word)
        while start_index < len(text):
            if text[start_index: start_index + word_length] == word:
                matches.append((start_index, start_index + word_length, word.lower()))
                start_index += word_length
            else:
                start_index += 1
    matches = sorted(matches)
    # Prompt a USER to replace them.
    prompts = []
    for match in matches:
        if match[2] in {'adjective', 'adverb'}:
            prompts.append(input('Enter' + ' an ' + match[2]))
        else:
            prompts.append(input('Enter' + ' a ' + match[2]))

    # Excise words from original text and store remains.
    head = [text[:matches[0][0]]]
    middle = []
    for i in range(1, len(matches)):
        middle.append(text[matches[i-1][1]:matches[i][0]])
    tail = [text[matches[len(matches)-1][1]:]]
    non_altered_text = head + middle + tail

    # Merge non_altered text and USER's prompts.
    new_text = ''
    for i in range(len(prompts)):
        new_text += non_altered_text[i] + prompts[i]
    new_text += non_altered_text[-1]

    # Create file with modified text.
    new_path = os.path.dirname(path) + '\\modified_' + os.path.basename(path)
    textFile = open(new_path, 'w')
    textFile.write(new_text)
    textFile.close()
    textFile = open(new_path)
    print(textFile.read())
    textFile.close()  # Not sure if there is need to repeat open/close


# Raise exception if file not found.
except FileNotFoundError:
    print("Oops! Can't find the file. Try another one.")
    pass
