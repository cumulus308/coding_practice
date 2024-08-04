def solution(s):
    def transform_word(word):
        return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))
    
    words = s.split(' ')
    transformed_words = [transform_word(word) for word in words]
    return ' '.join(transformed_words)