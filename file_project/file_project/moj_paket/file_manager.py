# -*- coding: utf-8 -*-

def save_to_file(content, fp):
    try:
        with open(fp, "a") as file:
            # file.write(f"{content}\n")
            file.write(content)
            file.write("\n")
        return True
    except TypeError:
        raise KrivoError(f"{type(content)} nije str")
    
        
def read_from_file(fp):
    with open(fp, "r") as file:
        return [x.strip() for x in file.readlines()]
    
def brisi(fp):
    with open(fp, "w") as file:
        pass


class KrivoError(Exception):
    pass