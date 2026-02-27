create database megadb;
use megadb;
#CREATE USESR
create user 'mega'@'localhost'  IDENTIFIED BY 'MEGA_CLEAN';
#GRANT ALL PRERMIXXION 
grant aLL privileges on  megadb.*to 'mega'@'localhost';
flush privileges;
select user,host from mysql.user;
select*from MEGA_COLLAGE_DATA;
drop table MEGA_COLLAGE_DATA;	
select *from MEGA_COLLAGE_DATA where upper(College_Type) LIKE '%MBA%';
#TELLL ME THE ALL INFORMATION WHERE College_Management IS PRIVITE 
#TELL ME ALL CITY WHERE collageis private and city is agra 
select*from MEGA_COLLAGE_DATA where upper(College_Management) like "%Private Unaided%" and City="Agra";
#TELL ME ALL data where College_Principal_Contact_Number and College_TPO_Contact_Number is NA;
SELECT * 
FROM MEGA_COLLAGE_DATA 
WHERE (
        College_Principal_Contact_Number IS NULL
        OR TRIM(College_Principal_Contact_Number) = ''    #TRIM() removes spaces from left and right.
        OR UPPER(College_Principal_Contact_Number) = 'NA' #UPPER() changes text to CAPITAL letters.
      )
  AND (
        College_TPO_Contact_Number IS NULL
        OR TRIM(College_TPO_Contact_Number) = ''    #TRIM() removes spaces from left and right.
        OR UPPER(College_TPO_Contact_Number) = 'NA' #UPPER() changes text to CAPITAL letters.
      );
select * from  MEGA_COLLAGE_DATA  where State='Ladakh' and Student_Strength>400 and Region_North_South_East_West_Central='NORTH';
# TELL ME THE COLLAGE COUT BY STATE WISE##########
select COUNT(College_Name) AS COLLAGE_COUNT,state FROM MEGA_COLLAGE_DATA group by state order by COLLAGE_COUNT desc ;
#######Tell me total studentstrught by region ########
select Region_North_South_East_West_Central,COUNT(Student_Strength)  FROM MEGA_COLLAGE_DATA group by Region_North_South_East_West_Central  ;
#########################################################
#Find top 5 cities having the highest number of colleges.
select count(College_Name) as collage_count,City  FROM MEGA_COLLAGE_DATA group by city order by collage_count desc limit 5;
#Find all colleges where landline number is missing.
select *from  MEGA_COLLAGE_DATA where landline_no=0 ;
#Count private colleges in each state.
select state,count(college_name) as privite_collage from MEGA_COLLAGE_DATA where college_type='private' group by  state order by privite_collage desc ;
################################
##################################### advance ######################### 
	#Find the state having the highest total student strength.
select state ,sum(Student_Strength) as total from  MEGA_COLLAGE_DATA group by state order by total  desc limit 1;
  
#Find colleges whose student strength is above average.
select avg(Student_Strength) as average_ans from mega_collage_data;
SELECT college_name, Student_Strength FROM MEGA_COLLAGE_DATA
 WHERE Student_Strength > (
    SELECT AVG(Student_Strength) 
    FROM MEGA_COLLAGE_DATA
);
#Rank colleges based on student strength.
select city,college_name,student_strength,rank() over (partition by city order by student_strength desc) as RANKS from mega_collage_data ;
#################################################################
# RANK() → skips ranking numbers when duplicates exist.
# DENSE_RANK() → does not skip ranking numbers.
#where partion help it help us in where 
#PARTITION BY means ranking separately inside each group.
#Without partition → ranking on whole table
#With partition → ranking group wise#
#########################################################


#Find duplicate college names in the dataset.
select count(*) as collage_count, College_Name from mega_collage_data group by  College_Name,landline_no,College_Principal_Contact_Number  having count(*)>1;


#Find which region has the maximum MBA colleges.
SELECT Region_North_South_East_West_Central, COUNT(*) AS mba_college_count
FROM mega_collage_data
WHERE College_Type = 'MBA'
GROUP BY Region_North_South_East_West_Central
ORDER BY mba_college_count DESC
LIMIT 2;
#############################################################
select *from MEGA_COLLAGE_DATA ;
      





