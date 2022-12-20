CREATE EXTERNAL TABLE crimes (
    crime_id string,
    month date,
    reported_by string,
    falls_within string,
    longitude double,
    latitude double,
    location string,
    lsoa_code string,
    lsoa_name string,
    crime_type string,
    last_outcome_category string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

load data inpath "hdfs://sandbox-hdp.hortonworks.com:8020/data/crimes-london.csv" overwrite into table crimes;
