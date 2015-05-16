sqlline.bat -u "jdbc:drill:zklocal" -n admin -p admin -f "drill_query.sql" > result.csv
python wordcount.py result.csv