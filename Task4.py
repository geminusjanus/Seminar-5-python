with open("Task4-1.txt", "r") as file1:
    txt = file1.readline()

def encode(txt):
    encoding = ""
    i = 0
    while i < len(txt):
        count = 1
        while i +1 < len(txt) and txt[i] == txt[i+1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + txt[i]
        i = i + 1
    return encoding
if __name__ == '__main__':
    print (encode(txt))