text = 'beatuful moon'
vowels = 'aeiou'
count = 0
for i in text:
    if i in vowels:
        print(i)
        count += 1
print("Total vowels:", count)