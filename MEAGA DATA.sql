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

      

      





