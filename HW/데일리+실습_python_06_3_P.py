def count_vowels(x):
    count = 0
    vowels = ''.join(x)
    for i in list(vowels):
        if i in 'a':
            count += 1
        elif i in 'e':
            count += 1
        elif i in 'i':
            count += 1
        elif i in 'o':
            count += 1
        elif i in 'u':
            count +=1
        else:
            continue
    return count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3

