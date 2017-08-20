import os
def end_with(*endstring):
    ends = endstring
    def run(s):
        f = map(s.endswith,ends)
        if True in f: return s
    return run

def find_file(filepath, *endstring):
    list_file = os.listdir(filepath)
    a = end_with(endstring)
    f_file = filter(a, list_file)
    return f_file

