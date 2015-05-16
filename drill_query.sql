select text  from  dfs.`C:\Users\supreet\Downloads\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_tip.json` where  business_id in (select distinct business_table.business_id from (select flatten(categories) catg, business_id from dfs.`C:\Users\supreet\Downloads\yelp_dataset_challenge_academic_dataset\yelp_academic_dataset_business.json` )  business_table group by  business_table.catg, business_table.business_id  having  business_table.catg='Restaurants'  ) order by likes desc ;