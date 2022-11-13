# Write function Remove Exclamation Marks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    if s.find('!') != -1:
        s = s.replace('!','')
    return s
