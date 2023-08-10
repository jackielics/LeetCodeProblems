--
-- @lc app=leetcode.cn id=177 lang=mysql
--
-- [177] 第N高的薪水
--

-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select t.Salary
      from (select Salary, (rank() over(order by salary desc)) as 'rk'
            from Employee
            group by Salary) as t
      where t.rk = N
  );
END
-- @lc code=end

