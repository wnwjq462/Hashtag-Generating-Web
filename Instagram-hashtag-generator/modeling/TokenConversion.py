def FirstTokenConversion(model, t_list):
    
    res = []
    for t in t_list:
        similar_tokens = model.wv.most_similar(t)
        for i in range(len(similar_tokens)):
            if similar_tokens[i][1]>=0.7:
                res.append(similar_tokens[i])
                
    return res

def NTokenConversion(model, t_list, alpha, cnt):

    res = []
    for t in t_list:
        similar_tokens = model.wv.most_similar(t[0])
        for i in range(len(similar_tokens)):
            if (alpha**cnt)*(similar_tokens[i][1])>=0.7:
                res.append(similar_tokens[i])

    return res

def TokenConversion(model, common_tokens, alpha, n=None):
    
    # 토큰 전환
    ls1 = FirstTokenConversion(model, common_tokens)
    ls2 = NTokenConversion(model, ls1, alpha, cnt=1)
    ls3 = NTokenConversion(model, ls2, alpha, cnt=2)
    ls4 = NTokenConversion(model, ls3, alpha, cnt=3)
    ls5 = NTokenConversion(model, ls4, alpha, cnt=4)
    ls = ls1 + ls2 + ls3 + ls4 + ls5

    # 중복 토큰 제거
    temp = []
    result = []
    for i in range(len(ls)):
        if ls[i][0] not in temp:
            temp.append(ls[i][0])
            result.append(ls[i])
    
    # 유사도 기준 높은 순서대로 정렬
    temp = []
    for i in range(len(result)):
        k = len(result) - i
        for j in range(1, k):
            if result[j-1][1]<=result[j][1]:
                temp = result[j-1]
                result[j-1] = result[j]
                result[j] = temp
    
    # 유사도 기준 상위 n개만 반환
    if n is not None:
        result = result[:n]
    
    return result