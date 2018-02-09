import os
import re

word_len_list = []

# loading file path
filepath = "paragraph.txt"

# open the text file containing the paragraph
with open(filepath,"r") as txt_file :
    file_object = txt_file.read()

    # create a list of words
    word_list = file_object.split(" ")

    # find number of words in the passage
    word_count = int(len(word_list))

    # create a list of sentences
    sent_list = file_object.split(".")

    # find number of sentences in the passage
    sent_count= file_object.count('.')

    # find length of each word and store in a list
    for each_word in word_list :
        word_len_list.append(int(len(each_word)))

    # sum of length of all words will yield total letter count in the passage
    letter_count = sum(word_len_list)

    # find average letter count
    avg_letter_count = round(letter_count/int(len(word_list)), 4)

    # find average words per sentence
    avg_word_per_sent = word_count/int(sent_count)

    # print all the results to the terminal
    print("                             ")
    print (f'Paragraph Analysis')
    print("-----------------------------")
    print(f'Approximate Word Count: {word_count}')
    print(f'Approximate Sentence Count: {sent_count}')
    print(f'Average Letter Count(per word): {avg_letter_count}')
    print(f'Average Sentence Length(in words): {avg_word_per_sent}' )
    print("------------------------------")

      # open a text file to write the results into..
    output_filepath = "OutPyParagraph.txt"
    with open(output_filepath,"w") as write_file :
        
        # write the results to a text file
        write_file.write('\nParagraph Analysis\n')
        write_file.write("-----------------------------------\n")
        write_file.write('Approximate Word Count: %s\n' %word_count)
        write_file.write('Approximate Sentence Count: %s\n' %sent_count)
        write_file.write('Average Letter Count: %s\n' %avg_letter_count)
        write_file.write('Average Sentence Length: %s\n' %avg_word_per_sent)
      


    


