def group_anagram(strs):
    dic = {}
    for i in strs:
        if str(sorted(i)) not in dic:
            dic[str(sorted(i))] = [i]
        else:
            dic[str(sorted(i))].append(i)
    return dic.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))


