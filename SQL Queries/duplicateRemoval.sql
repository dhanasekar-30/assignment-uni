-- 1. Creating Temp Table
CREATE OR REPLACE TABLE "SAMPLE_ATTENDANCE_TEMP" LIKE "SAMPLE_ATTENDANCE";

-- 2. Loading Unique records into temp table
insert into "SAMPLE_ATTENDANCE_TEMP"(Name, From, To)
select Name, From, To
from (
select *,row_number() over(partition by "Name", "From", "To" order by 1)rn
from "SAMPLE_ATTENDANCE"
)a  where a.rn = 2 

-- 3. Deleting all duplicated records from main table
delete from "SAMPLE_ATTENDANCE" where Name in
(
select Name from (
select *,row_number() over(partition by "Name", "From", "To" order by 1)rn
from "SAMPLE_ATTENDANCE"
)a  where a.rn = 2 )

-- 4. Inserting the temp table's data into main table
insert into "SAMPLE_ATTENDANCE"(Name, From, To)
select Name, From, To
from "SAMPLE_ATTENDANCE_TEMP"

-- 5. Dropping temp table
drop table SAMPLE_ATTENDANCE_TEMP