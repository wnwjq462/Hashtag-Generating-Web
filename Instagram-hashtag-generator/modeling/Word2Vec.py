#!/usr/bin/env python
# coding: utf-8

# ### > 모듈



### 해시태그 전처리 모듈

def PreprocessingHashtags(path):
    
    import pandas as pd
    import re
    
    # 데이터 불러오기
    data = pd.read_csv(path).iloc[:, 1:]
    data = data[data['hashtags'].notnull()] # 해시태그 nan 제거
    data = data.drop_duplicates('image_url') # 중복 행 제거
    
    # 한글 외 제거 후 우물 정(#) 기준으로 분리
    p = re.compile(r'[가-힣#]+')
    data['hashtags_splitted'] = data['hashtags'].apply(lambda x: ''.join(p.findall(str(x))).split('#'))
    
    # 빈 해시태그 제거
    data['hashtags_completed'] = ''
    for i in range(len(data)):
        ls = [word for word in data.iloc[i]['hashtags_splitted'] if word!='']
        data['hashtags_completed'].iloc[i] = ls
        
    # 컬럼 삭제
    data.drop(['hashtags', 'hashtags_splitted'], axis=1, inplace=True)
        
    # 컬럼명 변경
    data.rename({'hashtags_completed':'hashtags'}, axis=1, inplace=True) 
    
    # 인덱스 reset
    data.reset_index(inplace=True)
    data.drop('index', axis=1, inplace=True)

    return data



### 출현빈도가 1회뿐인 해시태그 제거 모듈
### 시간이 오래걸려서 전처리 모듈과 따로 분리했습니다.

def PreprocessingHashtags_deletefreq(data):
    
    import pandas as pd
    
    # 데이터 가져오기
    data = data
    
    # 출현빈도가 1회뿐인 해시태그 제거
    hashtags_list = []
    for x in range(len(data.hashtags)):
        for y in range(len(data.hashtags[x])):
            hashtags_list.append(data.hashtags[x][y])
            
    hashtags_set = set(hashtags_list)
    hashtags_count = [hashtags_list.count(i) for i in hashtags_set]
    hashtags_dict = dict(zip(hashtags_set, hashtags_count))

    hashtags_df = pd.DataFrame()
    hashtags_df['name'] = hashtags_dict.keys()
    hashtags_df['count'] = hashtags_dict.values()
    
    hashtags_df = hashtags_df[hashtags_df['count'] >= 2]
    hashtags_df = hashtags_df.reset_index().drop('index', axis=1)
    
    # 컬럼 변경 완료
    new_hashtags = []
    for x in range(len(data.hashtags)):
        temp = []
    
        for y in range(len(data.hashtags[x])):    
            if data.hashtags[x][y] in hashtags_list:
                temp.append(data.hashtags[x][y])
        new_hashtags.append(temp)
        
    data['hashtags'] = new_hashtags
    
    return data



### 토큰화 모듈

def Tokenizer(data):
    
    import pandas as pd
    from ckonlpy.tag import Twitter
    
    twitter = Twitter()
    
    #사용자 사전 추가
    txt = pd.read_csv('UserDic.txt', sep='\n')
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

        for y in range(len(tokenized[x])-1):
            if tokenized[x][y] != tokenized[x][y+1]:
                temp.append(tokenized[x][y])
            
        new_tokenized.append(temp)
        
    return new_tokenized



### Word2Vec 학습 모듈

def Word2Vec(tokenized, min_count=1, workers=8, size=30, window=40, sg=1, iter=5):
    
    from gensim.models.word2vec import Word2Vec
    
    # Word2Vec 학습

    """
    sentences: 학습할 문장
    min_count : 임베딩할 단어의 최소 빈도수
    workers: 병렬 처리 스레드 수
    size: word vector의 차원(임베딩 사이즈)
    window: 윈도우 크기
    sg: skip-gram 사용여부(1: 사용, other: CBOW)
    iter: 학습횟수
    """
    
    model = Word2Vec(sentences = tokenized,
                 min_count = min_count,
                 workers = workers,
                 size = size,
                 window = window,
                 sg = sg,
                 iter=iter)
    
    # 학습이 완료 되면 필요없는 메모리를 unload
    model.init_sims(replace=True)
    
    return model

