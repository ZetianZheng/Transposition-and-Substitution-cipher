from utils import *

class CryptAnalysis(object):
    """ step 1, get frequency analysis of different chars and write to csv"""
    def __init__(self, encrypted_data):
        self.chars = None
        self.encrypted_data = encrypted_data

    def number_statistics(self, letters_number):
        """ return a number of all different n length words
        the dict of that and numbers of a pair chars"""
        dict_char = {}
        for i in range(len(self.encrypted_data) - letters_number + 1):
            temp_str = "".join(self.encrypted_data[i:i + letters_number])
            if temp_str in dict_char:
                dict_char[temp_str] += 1
            else:
                dict_char[temp_str] = 1

        return len(self.encrypted_data), dict_char

    def exec(self, letters_number, to_path_csv):
        """read data from txt, do analysis and rank the chars, write the answer to csv"""
        count, dict_chars = self.number_statistics(letters_number)
        self.chars, numbers, frequencies = statistics_analysis(dict_chars, count)
        write_to_csv(self.chars, numbers, frequencies, to_path_csv)
