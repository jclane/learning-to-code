# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
#
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    ndex = str.rfind('xyz')
  
    if str[ndex:ndex+3] == 'xyz' and str[ndex-1:ndex] != '.':
        return True
    else:
        return False
