# bugsChartScrapy

# 수집한 데이터를 가지고 뭐라도 좀 해보자. 


```python
import pandas as pd

df = pd.read_csv('./resources/csv/bugsChartScrapy_20200616.psv',
                 sep='|',
                 names=['ranking', 'title', 'artist', 'album', 'date'],
                 encoding='utf-8')
df.head()
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ranking</th>
      <th>title</th>
      <th>artist</th>
      <th>album</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>운다</td>
      <td>손호영</td>
      <td>Yes</td>
      <td>2006.09.22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>제발</td>
      <td>이승기</td>
      <td>남자가 여자를 사랑할 때 (Special Album)</td>
      <td>2006.09.22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>마음을 잃다</td>
      <td>넬(NELL)</td>
      <td>Healing Process</td>
      <td>2006.09.22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>I Love Rock &amp; Roll</td>
      <td>코요태</td>
      <td>London Koyote</td>
      <td>2006.09.22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>The Day</td>
      <td>브라운 아이드 걸스</td>
      <td>To My Lover - 브라운 아이드 걸스 &amp; 씨야 프로젝트 싱글</td>
      <td>2006.09.22</td>
    </tr>
  </tbody>
</table>
</div>



### 총 50만 row


```python
df.shape
```




    (501773, 5)



### ranking 이 null인 행의 수


```python
df['ranking'].isna().sum()
```




    1769



### ranking이 null인 행은 자료가 이상하다.
### bugsMusic에 들어가보니 공통적으로 스트리밍 제한된 title이 존재.
### 본인이 생각한 tag구조와 다른가보다.


```python
df.loc[df['ranking'].isna()].head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ranking</th>
      <th>title</th>
      <th>artist</th>
      <th>album</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>488</th>
      <td>NaN</td>
      <td>2009.11.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>497</th>
      <td>NaN</td>
      <td>2007.04.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>558</th>
      <td>NaN</td>
      <td>2007.04.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>585</th>
      <td>NaN</td>
      <td>2007.04.20</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>859</th>
      <td>NaN</td>
      <td>2009.01.09</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### ranking이 null이 아닌 행만 취한다. 


```python
df_notnull = df[~df['ranking'].isna()]
df_notnull['ranking'].isna().sum()
```




    0



### ranking 칼럼값이 없으면 곤란하니 삭제는 했는데
### 생각해보니 나머지 값들도 마찬가지다
### 그냥 null을 하나라도 포함하는 행들은 전부 삭제를해주자. 


```python
df_notnull.dropna(inplace=True)
```

    /home/jhleeeme/.pyenv/versions/3.5.2/envs/jupyter-3.5.2/lib/python3.5/site-packages/ipykernel_launcher.py:4: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      after removing the cwd from sys.path.


### date, ranking 칼럼으로 정렬도 해줌


```python
df_notnull.sort_values(['date', 'ranking'], ascending=[False, True], inplace=True)
df_notnull.head()
```

    /home/jhleeeme/.pyenv/versions/3.5.2/envs/jupyter-3.5.2/lib/python3.5/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ranking</th>
      <th>title</th>
      <th>artist</th>
      <th>album</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>478941</th>
      <td>1.0</td>
      <td>Downtown Baby</td>
      <td>블루(BLOO)</td>
      <td>Downtown Baby</td>
      <td>2020.06.14</td>
    </tr>
    <tr>
      <th>478942</th>
      <td>2.0</td>
      <td>MORE &amp; MORE</td>
      <td>TWICE (트와이스)</td>
      <td>MORE &amp; MORE</td>
      <td>2020.06.14</td>
    </tr>
    <tr>
      <th>478943</th>
      <td>3.0</td>
      <td>에잇(Prod.&amp;Feat. SUGA of BTS)</td>
      <td>아이유(IU)</td>
      <td>에잇</td>
      <td>2020.06.14</td>
    </tr>
    <tr>
      <th>478944</th>
      <td>4.0</td>
      <td>사랑하게 될 줄 알았어</td>
      <td>전미도</td>
      <td>슬기로운 의사생활 OST Part 11</td>
      <td>2020.06.14</td>
    </tr>
    <tr>
      <th>478945</th>
      <td>5.0</td>
      <td>작사가</td>
      <td>헤이즈(Heize)</td>
      <td>Lyricist</td>
      <td>2020.06.14</td>
    </tr>
  </tbody>
</table>
</div>



### type도 ranking 칼럼은 int, date 칼럼은 datetime으로 바꿔줌


```python
df_notnull = df_notnull.astype({'date': 'datetime64', 'ranking': 'int64'})
df_notnull.dtypes
```




    ranking             int64
    title              object
    artist             object
    album              object
    date       datetime64[ns]
    dtype: object



### null값을 그냥 제거했더니 총 49만8천 row가 됐다. 뭐 충분하다.


```python
df_notnull.shape
```




    (498235, 5)



### score 칼럼을 추가했다. 간단하게 1/ranking 으로 매김
### e.g. 1등: 1점, 2등: 0.5점, ..., 10등: 0.1점 


```python
df_notnull['score'] = 1/df_notnull['ranking']
df_notnull.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ranking</th>
      <th>title</th>
      <th>artist</th>
      <th>album</th>
      <th>date</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>478941</th>
      <td>1</td>
      <td>Downtown Baby</td>
      <td>블루(BLOO)</td>
      <td>Downtown Baby</td>
      <td>2020-06-14</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>478942</th>
      <td>2</td>
      <td>MORE &amp; MORE</td>
      <td>TWICE (트와이스)</td>
      <td>MORE &amp; MORE</td>
      <td>2020-06-14</td>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>478943</th>
      <td>3</td>
      <td>에잇(Prod.&amp;Feat. SUGA of BTS)</td>
      <td>아이유(IU)</td>
      <td>에잇</td>
      <td>2020-06-14</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>478944</th>
      <td>4</td>
      <td>사랑하게 될 줄 알았어</td>
      <td>전미도</td>
      <td>슬기로운 의사생활 OST Part 11</td>
      <td>2020-06-14</td>
      <td>0.250000</td>
    </tr>
    <tr>
      <th>478945</th>
      <td>5</td>
      <td>작사가</td>
      <td>헤이즈(Heize)</td>
      <td>Lyricist</td>
      <td>2020-06-14</td>
      <td>0.200000</td>
    </tr>
  </tbody>
</table>
</div>



### 일단 여기까지 전처리한 데이터를 psv파일로 저장


```python
df_notnull.to_csv('./resources/csv/bugsChart_score.psv',
                  sep='|',
                  index=False,
                  encoding='utf8')
```

---
## MySQL에 데이터를 넣고, 살펴보자.


```python
import pymysql


host = 'localhost'
username = 'JHLeeeMe'
password = '********'
db_name = 'bugsMusic_db'

db = pymysql.connect(
        host = host,
        port = 3306,
        user = username,
        passwd= password,
        db = db_name,
        charset = 'utf8'
)
```


```python
sql_drop_table = """
    DROP TABLE IF EXISTS bugsMusic_db.bugsChart_tb
"""

sql_create_table = """
    CREATE TABLE bugsMusic_db.bugsChart_tb (
        ranking int             not null,
        title   varchar(100)    not null,
        artist  varchar(100)    not null,
        album   varchar(100)    not null,
        date_   date            not null,
        score   float           not null
    ) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
"""

# sql_load_data = """
#     load data infile './resources/csv/bugsChart_score.psv'
#     into table bugsMusic_db.bugsChart_tb
#     fields terminated by '|'
#     lines terminated by '\n'
#     ignore 1 lines
# """
```


```python
cursor = db.cursor()

cursor.execute(sql_drop_table)
cursor.execute(sql_create_table)
# cursor.execute(sql_load_data)

db.commit()
```

---

### 일단 그래프에서 한글폰트 깨짐 문제 해결을 위한 코드


```python
import platform
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
%matplotlib inline

# 한글 사용시 마이너스 폰트가 깨지는 문제가 발생할 수 있으므로 설정변경
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Linux':
    rc('font', family='NanumBarunGothic')
else:
    print('Unknown system... sorry~~~~~~')
```

## 1. 점수가 가장 높은 가수는?


```python
sql_artist_score = """
    select artist, sum(score)
      from bugsChart_tb
     group by artist
     order by sum(score) desc
     limit 10;
"""
```


```python
artist_score_df = pd.read_sql(sql_artist_score, db)
artist_score_df.set_index('artist', inplace=True)
artist_score_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sum(score)</th>
    </tr>
    <tr>
      <th>artist</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>아이유(IU)</th>
      <td>584.004760</td>
    </tr>
    <tr>
      <th>BIGBANG</th>
      <td>437.742153</td>
    </tr>
    <tr>
      <th>다비치</th>
      <td>371.404638</td>
    </tr>
    <tr>
      <th>볼빨간사춘기</th>
      <td>330.655340</td>
    </tr>
    <tr>
      <th>TWICE (트와이스)</th>
      <td>277.568538</td>
    </tr>
    <tr>
      <th>태연 (TAEYEON)</th>
      <td>264.421062</td>
    </tr>
    <tr>
      <th>소녀시대 (GIRLS' GENERATION)</th>
      <td>237.066701</td>
    </tr>
    <tr>
      <th>케이윌</th>
      <td>235.490209</td>
    </tr>
    <tr>
      <th>백지영</th>
      <td>234.864432</td>
    </tr>
    <tr>
      <th>Red Velvet (레드벨벳)</th>
      <td>230.639596</td>
    </tr>
  </tbody>
</table>
</div>




```python
artist_score_df.plot(kind='bar', figsize=(12, 6), fontsize=15, rot=60)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f23803d0ac8>




![1](https://user-images.githubusercontent.com/31606119/85188664-6e88c980-b2e3-11ea-98c6-2ce4d6dc0885.png)


## 2. 타이틀 점수 TOP10


```python
# Title 점수 TOP10
sql_title_score = """
    select artist, title, sum(score)
      from bugsChart_tb
     group by artist, title
     order by sum(score) desc
     limit 10
"""
```


```python
title_score_df = pd.read_sql(sql_title_score, db)
title_score_df.set_index(['artist', 'title'], inplace=True)
title_score_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>sum(score)</th>
    </tr>
    <tr>
      <th>artist</th>
      <th>title</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>쥬얼리(Jewelry)</th>
      <th>One More Time</th>
      <td>65.087647</td>
    </tr>
    <tr>
      <th>MC몽</th>
      <th>서커스 (feat. 임유경 - 달래 음악단, $howgun)</th>
      <td>56.026355</td>
    </tr>
    <tr>
      <th>BIGBANG</th>
      <th>하루하루</th>
      <td>45.646840</td>
    </tr>
    <tr>
      <th>백지영</th>
      <th>총맞은 것처럼</th>
      <td>45.326374</td>
    </tr>
    <tr>
      <th>장범준</th>
      <th>흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야</th>
      <td>45.266149</td>
    </tr>
    <tr>
      <th>에일리(Ailee)</th>
      <th>첫눈처럼 너에게 가겠다</th>
      <td>43.388505</td>
    </tr>
    <tr>
      <th>iKON</th>
      <th>사랑을 했다 (LOVE SCENARIO)</th>
      <td>43.375965</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">아이유(IU)</th>
      <th>Blueming</th>
      <td>42.402319</td>
    </tr>
    <tr>
      <th>밤편지</th>
      <td>41.842738</td>
    </tr>
    <tr>
      <th>폴킴(Paul Kim)</th>
      <th>모든 날, 모든 순간 (Every day, Every Moment)</th>
      <td>41.221391</td>
    </tr>
  </tbody>
</table>
</div>




```python
title_score_df.plot(kind='bar', figsize=(12, 6), fontsize=15, rot=70)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f237b1de828>




![2](https://user-images.githubusercontent.com/31606119/85188666-6fb9f680-b2e3-11ea-99eb-b0ea4286e2a9.png)



## 3. 가장 많이 언급된 타이틀 TOP10


```python
sql_title_count = """
    select artist, title, count(title)
      from bugsChart_tb
     group by artist, title
     order by count(title) desc
     limit 10
"""
```


```python
title_count_df = pd.read_sql(sql_title_count, db)
title_count_df.set_index(['artist', 'title'], inplace=True)
title_count_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count(title)</th>
    </tr>
    <tr>
      <th>artist</th>
      <th>title</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>아이유(IU)</th>
      <th>밤편지</th>
      <td>1177</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">폴킴(Paul Kim)</th>
      <th>모든 날, 모든 순간 (Every day, Every Moment)</th>
      <td>818</td>
    </tr>
    <tr>
      <th>비</th>
      <td>744</td>
    </tr>
    <tr>
      <th>에일리(Ailee)</th>
      <th>첫눈처럼 너에게 가겠다</th>
      <td>705</td>
    </tr>
    <tr>
      <th>Ed Sheeran(에드 시런)</th>
      <th>Shape Of You</th>
      <td>683</td>
    </tr>
    <tr>
      <th>정승환</th>
      <th>너였다면</th>
      <td>674</td>
    </tr>
    <tr>
      <th>버스커 버스커(Busker Busker)</th>
      <th>벚꽃 엔딩</th>
      <td>638</td>
    </tr>
    <tr>
      <th>The Chainsmokers(체인스모커스)</th>
      <th>Closer (feat. Halsey)</th>
      <td>633</td>
    </tr>
    <tr>
      <th>폴킴(Paul Kim)</th>
      <th>너를 만나</th>
      <td>595</td>
    </tr>
    <tr>
      <th>DEAN(딘)</th>
      <th>D (half moon) (Feat. 개코)</th>
      <td>592</td>
    </tr>
  </tbody>
</table>
</div>




```python
title_count_df.plot(kind='barh', figsize=(12, 6), fontsize=15)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f237b160908>




![3](https://user-images.githubusercontent.com/31606119/85188668-70528d00-b2e3-11ea-8724-e7b69536860a.png)


## 4. 앨범 점수 TOP10


```python
sql_album_score = """
    select artist, album, sum(score)
      from bugsChart_tb
     group by artist, album
     order by sum(score) desc
     limit 10;
"""
```


```python
album_score_df = pd.read_sql(sql_album_score, db)
album_score_df.set_index(['artist', 'album'], inplace=True)
album_score_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>sum(score)</th>
    </tr>
    <tr>
      <th>artist</th>
      <th>album</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>아이유(IU)</th>
      <th>Love poem</th>
      <td>80.178207</td>
    </tr>
    <tr>
      <th>볼빨간사춘기</th>
      <th>Full Album RED PLANET</th>
      <td>69.239082</td>
    </tr>
    <tr>
      <th>버스커 버스커(Busker Busker)</th>
      <th>버스커 버스커 1집</th>
      <td>68.931575</td>
    </tr>
    <tr>
      <th>쥬얼리(Jewelry)</th>
      <th>Kitchi Island</th>
      <td>65.359024</td>
    </tr>
    <tr>
      <th>MC몽</th>
      <th>Show's Just Begun</th>
      <td>62.662819</td>
    </tr>
    <tr>
      <th>BLACKPINK</th>
      <th>SQUARE UP</th>
      <td>61.418836</td>
    </tr>
    <tr>
      <th>BIGBANG</th>
      <th>Stand Up (2008 빅뱅 3rd Mini Album)</th>
      <td>57.874649</td>
    </tr>
    <tr>
      <th>싸이 (PSY)</th>
      <th>싸이6甲 Part.1</th>
      <td>57.317014</td>
    </tr>
    <tr>
      <th>AKMU (악동뮤지션)</th>
      <th>항해</th>
      <td>55.485827</td>
    </tr>
    <tr>
      <th>볼빨간사춘기</th>
      <th>Red Diary Page.1</th>
      <td>55.443944</td>
    </tr>
  </tbody>
</table>
</div>




```python
album_score_df.plot(kind='bar', figsize=(12, 6), fontsize=15, rot=65)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f23798ffa58>




![4](https://user-images.githubusercontent.com/31606119/85188669-70528d00-b2e3-11ea-85b8-5738b9958fa1.png)



```python
db.close()
```
