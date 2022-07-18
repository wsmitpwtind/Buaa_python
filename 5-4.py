def search(place):
    if place == len(sentence):
        return True
    if sentence[place] == 'H' or sentence[place] == 'h':
        if place < len(sentence) - 1 and (sentence[place + 1] == 'E' or sentence[place + 1] == 'e'):
            return search(place + 1) or search(place + 2)
        else:
            return search(place + 1)
    if sentence[place] == 'L' or sentence[place] == 'l':
        if place < len(sentence) - 1 and (sentence[place + 1] == 'I' or sentence[place + 1] == 'i'):
            return search(place + 2)
    if sentence[place] == 'B' or sentence[place] == 'b':
        if place < len(sentence) - 1 and (sentence[place + 1] == 'E' or sentence[place + 1] == 'e'):
            return search(place + 1) or search(place + 2)
        else:
            return search(place + 1)
    if sentence[place] == 'C' or sentence[place] == 'c':
        if place < len(sentence) - 1 and (sentence[place + 1] == 'L' or sentence[place + 1] == 'l'):
            return search(place + 1) or search(place + 2)
        else:
            return search(place + 1)
    if sentence[place] == 'N' or sentence[place] == 'n':
        if place < len(sentence) - 1 and (
                sentence[place + 1] == 'E' or sentence[place + 1] == 'e' or sentence[place + 1] == 'A' or sentence[
            place + 1] == 'a'):
            return search(place + 1) or search(place + 2)
        else:
            return search(place + 1)
    if sentence[place] == 'O' or sentence[place] == 'o':
        return search(place + 1)
    if sentence[place] == 'F' or sentence[place] == 'f':
        return search(place + 1)
    if sentence[place] == 'M' or sentence[place] == 'm':
        if place < len(sentence) - 1 and (sentence[place + 1] == 'G' or sentence[place + 1] == 'g'):
            return search(place + 2)
    if sentence[place] == 'A' or sentence[place] == 'a':
        if place < len(sentence) - 1 and (
                sentence[place + 1] == 'L' or sentence[place + 1] == 'l' or sentence[place + 1] == 'R' or sentence[
            place + 1] == 'r'):
            return search(place + 2)
    if sentence[place] == 'S' or sentence[place] == 's':
        if place < len(sentence) - 1 and (sentence[place + 1] == 'I' or sentence[place + 1] == 'i'):
            return search(place + 1) or search(place + 2)
        else:
            return search(place + 1)
    if sentence[place] == 'P' or sentence[place] == 'p':
        return search(place + 1)

    return False


n = int(input())

for i in range(n):
    sentence = input()
    if search(0):
        print('Yes')
    else:
        print('No')
