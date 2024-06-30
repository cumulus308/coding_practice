def solution(id_pw, db):
    dic =dict(db)
    if id_pw[0] in list(dic.keys()):
        if id_pw[1] == dic[id_pw[0]]:
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail' 