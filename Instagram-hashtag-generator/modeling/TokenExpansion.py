# 조건부 확률을 돌려주는 함수
def getCondtnlProb(tokenized_tags, tkn, pivot):
    ret = []
    # 기준 토큰 등장 확률
    tkn_cnt = 0
    total = len(tokenized_tags)
    idxs = []
    next_tkn = []
    for i in range(total):
        for j in range(len(tokenized_tags[i])):
            if tokenized_tags[i][j] == tkn:
                tkn_cnt += 1
                idxs.append([i,j])
                if j+1 < len(tokenized_tags[i]):
                    next_tkn.append(tokenized_tags[i][j+1])

    p_cur = tkn_cnt / total
    
    ### 코드 , 기준 토큰과 각 토큰의 동시 등장 확률
    p_nexts = []
    next_cnt = 0
    # t: 토큰셋
    t = list(set(next_tkn))
    for i in range(len(t)):
        cnt = 0
        for idx in idxs:
            if idx[1]+1 < len(tokenized_tags[idx[0]]) and tokenized_tags[idx[0]][idx[1]+1] == t[i]:
                cnt += 1
        p_nexts.append([t[i],(cnt/total) / p_cur])
    
    for i in range(len(p_nexts)):
        if p_nexts[i][1] > pivot:
            if p_nexts[i][0] == tkn:
                continue
            ret.append(p_nexts[i])
    
    return ret

# 필요 - 토큰들이 있는 리스트, 

def TagExpansion(tokenized, tkn, alpha, pivot):    
    import pandas as pd
    import numpy as np
    # 토큰들이 들어있는 리스트?
#     tokenized = []
#     for sentence in hashtag_joined:
#         tokens = mecab.morphs(sentence)
#         tokenized.append(tokens)
    
    probs = getCondtnlProb(tokenized, tkn, pivot)
    if len(probs) == 0:
        return [tkn]

    probs2 = []
    for t in probs:
        probs2.append(getCondtnlProb(tokenized, t[0], pivot/alpha))

    temp = []    
    probs3 = []
    for t in probs2:
        if len(t) == 0:
            probs3.append([])
        else:
            temp = []
            for i in range(len(t)):
                temp.append(getCondtnlProb(tokenized, t[i][0], pivot/(alpha**2)))
        probs3.append(temp)
    
    hashtag = [tkn+probs[k][0] for k in range(len(probs)) ]
    tag=[]
    for i in range(len(hashtag)):
        for j in range(len(probs2[i])):
            hashtag.append(hashtag[i]+probs2[i][j][0])
    
    return hashtag
