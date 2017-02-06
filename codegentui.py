'''
Created on Jan. 21 2017

@author: joshua meyer
'''
import sys
from string_builder import StringBuilder
#ftool.move_files_of_exten(root, root_path_to_keep, destination, file_extension)
#ftool.move_files_of_exten(root,dest, r"/media/joshua/Data3/00FFSorted_by_exten", ".txt")
action = sys.argv[1]
input_text = sys.argv[2]
symbol_src = sys.argv[3]
replacement_src = sys.argv[4]
if len(sys.argv) > 5:
    destination_path = sys.argv[5]
else:
    destination_path = ''
def main():
    #ftool.move_files_of_exten(a, a, b, c)
    print("COMMAND ACTION INPUTTEXT SYMBOLSRC REPLACEMENTSRC FILEEXTENSION")
    print("")
    if action == '-f':
        use_file_sources(input_text, symbol_src, replacement_src, destination_path)
    else:
        print('invalid action choice')


def write_list_to_file(destination, output_list):
    a_file = open(destination, mode='a', encoding='utf-8')
    a_file.write('#!/bin/bash\n')
    for line in output_list:
        a_file.write(line)

    return True

def use_file_sources(input_path, symbol_path, replacement_path, destination=''):
    text = read_file(input_path)
    symbol_list = read_file_to_list(symbol_path)
    replacement_list = read_file_to_list(replacement_path)
    output_list = generate_strings_for_list(text, symbol_list[0], replacement_list)
    if destination == '':
        for line in output_list:
            print(line)
    else:
        write_list_to_file(destination, output_list)

def generate_strings_for_list(original_text, symbol, replacement_list):
    oTool = StringBuilder()
    output_list = []
    for replacement in replacement_list:
        new_string = oTool.symbol_replace(original_text, symbol, replacement)
        print(new_string)
        output_list.append(new_string)
    return output_list
    print("done")


def read_file_to_list(file_path):
    input_list = []
    with open(file_path, encoding='utf-8') as a_file:
        for a_line in a_file:
            input_list.append(a_line.rstrip())
    return input_list
def read_file(file_path):
    input = ""
    a_file =  open(file_path, encoding='utf-8')
    input = a_file.read()
    return input





if __name__ == '__main__':
    main()