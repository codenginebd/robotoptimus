__author__ = 'Codengine'

s = '100004	1	"10"	"Ingles"	"Universidade Anhembi Morumbi"	"Formado"	"Publicidade em Markentig"	"1998-2003"	""	""	""'

def split_values(s):
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

print split_values(s)

