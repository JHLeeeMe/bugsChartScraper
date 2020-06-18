USE bugsMusic_db;
DROP TABLE IF EXISTS bugsMusic_db.bugsChart_tb;

CREATE TABLE bugsMusic_db.bugsChart_tb (
     ranking INT             NOT NULL,
     title   VARCHAR(100)    NOT NULL,
     artist  VARCHAR(100)    NOT NULL,
     album   VARCHAR(100)    NOT NULL,
     date_   DATE            NOT NULL,
     score   FLOAT           NOT NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
COMMIT;

DESC bugsMusic_db.bugsChart_tb;
        
-- select all
SELECT * 
  FROM bugsChart_tb;
  
-- 1위를 가장 많이 한 artist
SELECT artist, count(*)
  FROM bugsChart_tb
 WHERE ranking = 1
 GROUP BY artist
 ORDER BY count(*) DESC;
 
-- 1위를 가장 많이 한 title
SELECT artist, title, count(*)
  FROM bugsChart_tb
 WHERE ranking = 1
 GROUP BY artist, title
 ORDER BY count(*) DESC;
 
-- 가장 많이 언급된 title
SELECT artist, title, count(title)
  FROM bugsChart_tb
 GROUP BY artist, title
 ORDER BY count(title) DESC;
 
-- album score
SELECT artist, album, sum(score)
  FROM bugsChart_tb
 GROUP BY artist, album
 ORDER BY sum(score) DESC;

-- 앨범이 100위권에서 언급된 수
SELECT artist, album, count(album)
  FROM bugsChart_tb
 GROUP BY artist, album
 ORDER BY count(album) DESC;
 
