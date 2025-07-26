# Problem
[180. Consecutive Numbers]

# Key Intuition
1. use windows function LAED() and LAG()

# Code
```sql
SELECT DISTINCT
    num AS ConsecutiveNums
FROM
(select
    num,
    LEAD(num) OVER (ORDER BY id ASC) as lead_num,
    LAG(num) OVER (ORDER BY id ASC) as lag_num
from Logs) subq
WHERE 
    num = lead_num
    AND lead_num = lag_num
```