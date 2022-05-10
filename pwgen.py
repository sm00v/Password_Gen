import sys
import argparse
import os

special_chars = ['!', '#', '$', '!!', '@']
common_year_list = ['22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010']
common_season_list = ['winter', 'summer', 'spring', 'fall', 'wintertime', 'summertime', 'springtime', 'falltime']

def gen_common_pws():
    for season in common_season_list:
        for year in common_year_list:
            for char in special_chars:
                password = season+year+char
                password_upper = season+year+char
                master_list_unfiltered.append(password)
                master_list_unfiltered.append(password_upper)

def gen_unique_pws():
    for year in common_year_list:
        word_year = args.word + year
        word_year_cap = args.word.capitalize() + year
        master_list_unfiltered.append(word_year)
        master_list_unfiltered.append(word_year_cap)
        for char in special_chars:
            word_with_char = args.word + char
            word_with_char_cap = args.word.capitalize() + char
            word_year_with_char = args.word + year + char
            word_year_with_char_cap = args.word.capitalize() + year + char
            master_list_unfiltered.append(word_with_char)
            master_list_unfiltered.append(word_with_char_cap)
            master_list_unfiltered.append(word_year_with_char)
            master_list_unfiltered.append(word_year_with_char_cap)

def argparseStuff():
    parser = argparse.ArgumentParser(description="Input the graph_me.csv file to graph!.")
    parser.add_argument("-l", "--length", help="Client requirement for minimum password length.")
    # parser.add_argument("-c", "--complexity", help="Policy requires 3 of 4 requirements (capital, character, number, lowercase)")
    parser.add_argument("-s", "--seasons", help="Enable the seasons passwords.", action='store_true')
    parser.add_argument("-w", "--word", help="Give a word to permutate like the company name.")
    parser.add_argument("-o", "--output", help="File to write to!", default='passwords.txt')
    return parser.parse_args()

if __name__ == '__main__':
    master_list_unfiltered = []
    master_list_filtered = []
    args = argparseStuff()
    gen_unique_pws()
    if args.seasons:
        gen_common_pws()
    for password in master_list_unfiltered:
        if len(password) < int(args.length):
            pass
        else: master_list_filtered.append(password)
    final_list = list(set(master_list_filtered))
    if args.output:
        file = open(args.output, 'w')
        [file.write(x+'\n') for x in final_list]
        print(f'[+] Wrote {len(final_list)} passwords to {args.output}')
    else: [print(x) for x in final_list]
