def Tokenizer(data):

    """해시태그를 토큰 단위로 토큰화"""

    import pandas as pd
    from ckonlpy.tag import Twitter

    twitter = Twitter()

    # 사용자 사전 추가
    txt = pd.read_csv('modeling/UserDic.txt', sep='\n')
    txt = txt['<사용자 사전>']
    for line in txt:
        twitter.add_dictionary(txt, 'Noun')

    # 데이터 가져오기
    data = data
    new_hashtags = data.hashtags.copy()

    # 토큰화
    for i in range(len(new_hashtags)):
        new_hashtags[i] = ' '.join(new_hashtags[i])

    tokenized = []
    for sentence in new_hashtags:
        tokens = twitter.morphs(sentence)
        tokenized.append(tokens)

    # 연속된 중복 제거
    new_tokenized = []
    for x in range(len(tokenized)):
        temp = []
        for y in range(len(tokenized[x]) - 1):
            if tokenized[x][y] != tokenized[x][y + 1]:
                temp.append(tokenized[x][y])
        new_tokenized.append(temp)

    return new_tokenized
