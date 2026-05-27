-- returns null when 2nd row in table does not exist

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1
    LIMIT 1
) AS second_highest_salary

-- DISTINCT
-- forces the database to eliminate duplicates, which might require extra sorting or hashing.

-- ORDER BY
-- the database can use indexes on the salary column to speed up

-- OFFSET
-- database still needs to scan and discard rows before the offset

-- OPTIMIZED QUERY
-- window functions like ROW_NUMBER() or DENSE_RANK()
-- window functions look at all rows at once, so the database can process the data in one pass

WITH RankedSalaries AS (
    SELECT
        salary
        ,DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
    FROM Employee
)
SELECT (
    SELECT salary
    FROM RankedSalaries
    WHERE rank = 2
    LIMIT 1
) AS SecondHighestSalary;
