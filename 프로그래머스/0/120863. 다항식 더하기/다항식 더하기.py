def solution(polynomial):
    terms = polynomial.replace(" ", "").split("+")
    
    xx = [term for term in terms if 'x' in term]
    nn = sum(int(term) for term in terms if term.isnumeric())
    
    xx_count = sum(int(term[:-1]) if term[:-1].isnumeric() else 1 for term in xx)
    
    if xx_count > 1 and nn > 0:
        return f'{xx_count}x + {nn}'
    elif xx_count == 1 and nn > 0:
        return f'x + {nn}'
    elif xx_count > 1 and nn == 0:
        return f'{xx_count}x'
    elif xx_count == 1 and nn == 0:
        return 'x'
    elif xx_count == 0 and nn > 0:
        return str(nn)
    else:
        return '0'