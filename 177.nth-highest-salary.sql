#
# @lc app=leetcode id=177 lang=python3
#
# [177] Nth Highest Salary 
#

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE M INT;
    SET M = N - 1 ;
  RETURN (
    SELECT DISTINCT Salary FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET M
  );
END
