def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    for ch in s1:
        if ch not in s2:
            return False
    return True


s1 = "listen"
s2 = "silent"
if check_anagram(s1, s2):
    print(f"{s1} and {s2} are ANAGRAM")
else:
    print(f"{s1} and {s2} are NOT ANAGRAM")
