--

-- @lc app=leetcode.cn id=1440 lang=mysql

--

-- [1440] 计算布尔表达式的值

--

-- @lc code=start

# Write your MySQL query statement below
/* select (select v1.value
 from Variables as v1
 where v1.name = e.left_operand) as 'left', 
 e.operator as operator, 
 (select v2.value
 from Variables as v2
 where v2.name = e.right_operand) as 'right'
 from Expressions as e */
select
    e.left_operand,
    e.operator,
    e.right_operand, (
        case e.operator
            when '>' then if(
                v1.value > v2.value,
                'true',
                'false'
            )
            when '<' then if(
                v1.value < v2.value,
                'true',
                'false'
            )
            else if(
                v1.value = v2.value,
                'true',
                'false'
            )
        end
    ) as value
from Expressions e
    left join Variables v1 on e.left_operand = v1.name
    left join Variables v2 on e.right_operand = v2.name -- @lc code=end