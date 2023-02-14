-- script that lists the number of records with the same score 
-- displays score and no. of rec for score as number
-- sorted by the number of records (descending)

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
