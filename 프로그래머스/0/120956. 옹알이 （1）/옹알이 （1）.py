def solution(babbling):
    possible_sounds = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        temp_word = word
        for sound in possible_sounds:
            if sound in temp_word:
                temp_word = temp_word.replace(sound, ' ', 1)
        
        if temp_word.strip() == '':
            count += 1
    
    return count