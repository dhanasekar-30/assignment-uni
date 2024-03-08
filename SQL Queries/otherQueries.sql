-- 2. Write a query to find out total number of days attended by all members

SELECT SUM(DATEDIFF(To, From) + 1) AS TotalDaysAttended
FROM STUDENTS_ATTENDANCE;


-- 3. Write a query to list the members with the most attendance (i.e. one or more members who have attended the course for maximum number of days)

SELECT Name
FROM STUDENTS_ATTENDANCE
GROUP BY Name
HAVING SUM(DATEDIFF(To, From) + 1) = (
    SELECT MAX(AttendanceDays)
    FROM (
        SELECT SUM(DATEDIFF(To, From) + 1) AS AttendanceDays
        FROM YourTableName
        GROUP BY Name
    ) AS SubQuery
);


-- 4. Write a query to list the members with the most attendance in any one month (i.e. one or more members who have attended the course for maximum number of days with a month, say within Sep, Oct, Nov)

SELECT 
    Name,
    COUNT(*) AS TotalDaysAttended
FROM 
    attendance_table
WHERE 
    MONTH(From) IN (9, 10, 11) AND 
    MONTH(To) IN (9, 10, 11)
GROUP BY 
    Name
ORDER BY 
    TotalDaysAttended DESC
LIMIT 1;

-- 5. Write a query to find out the member with the greatest number of consecutive attendances.

WITH consecutive_attendances AS (
    SELECT 
        Name,
        FromDate,
        ToDate,
        ROW_NUMBER() OVER (PARTITION BY Name ORDER BY FromDate) AS rn
    FROM 
        attendance
)
SELECT 
    Name,
    MAX(rn) AS max_consecutive_attendances
FROM (
    SELECT 
        Name,
        ROW_NUMBER() OVER (PARTITION BY Name, DATEADD(day, -ROW_NUMBER() OVER (PARTITION BY Name ORDER BY FromDate), FromDate) ORDER BY FromDate) AS rn
    FROM 
        attendance
) AS temp
GROUP BY 
    Name;
