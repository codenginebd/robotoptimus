__author__ = 'Codengine'

class Parser:
    @staticmethod
    def split_values(s):
        if not s:
            return []
        s = s.replace('\t',' ')
        values = []
        while s:
            if s.startswith('"'):
                temp_val = ''
                i = 1
                while i < len(s) and s[i] != '"':
                    temp_val += s[i]
                    i += 1
                s = s[i+1:]
                values += [temp_val]
            else:
                temp_val = ''
                i = 0
                while i < len(s) and s[i] != ' ':
                    temp_val += s[i]
                    i += 1
                s = s[i:]
                values += [temp_val]
            s = s.strip()

        return values

class FileHandler(object):
    def __init__(self):
        pass
    @staticmethod
    def read_txt_files(dir_name='RawTxtFiles'):
        import os
        txt_files = []
        for file in os.listdir(dir_name+"/"):
            if file.endswith(".txt"):
                txt_files += [file]
        file_contents = []
        for fname in txt_files:
            with open(dir_name+'/'+fname,'r') as f:
                lines = f.readlines()
                file_contents += lines[1:] if lines else []

        return file_contents

    @staticmethod
    def read_csv_file(file_name):
        contents = []
        with open(file_name,'r') as f:
            lines = f.readlines()
            if lines:
                lines = lines[1:]
            for line in lines:
                if line:
                    contents += [line.split(',')]
        return contents

class GarbageCleaner:
    def __init__(self):
        pass
    def start(self,data):
        for line in data:
            e_name = line[4]
            e_degree = line[5]
            e_major = line[6]


class Main:
    def __init__(self):
        pass
    def execute(self):
        data = []
        lines = FileHandler.read_txt_files()
        data_split = []
        for line in lines:
            split_vals = Parser.split_values(line)
            if split_vals:
                data_split += [split_vals]

Main().execute()