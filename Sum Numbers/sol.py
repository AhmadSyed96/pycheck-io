def sum_numbers(text: str) -> int:
    sum = 0
    text = text.split()
    for word in text:
        try:
            sum += int(word)
        except:
            continue
    return sum