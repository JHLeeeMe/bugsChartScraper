LOAD DATA LOCAL INFILE '/home/jhleeeme/Project/03_Src/python/jupyter/bugsChartScrapy/resources/csv/bugsChart_score.psv'
            INTO TABLE bugsMusic_db.bugsChart_tb
     FIELDS TERMINATED BY '|'
      LINES TERMINATED BY '\n'
        IGNORE 1 LINES;