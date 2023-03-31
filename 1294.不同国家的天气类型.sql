--
-- @lc app=leetcode.cn id=1294 lang=mysql
--
-- [1294] 不同国家的天气类型
--

-- @lc code=start
# Write your MySQL query statement below
select country_name, 
    (
        case 
            when avg(weather_state)<=15 then 'Cold'
            when avg(weather_state)>=25 then 'Hot'
            else 'Warm'
        end
    ) as weather_type
from Weather w
left join Countries c on c.country_id = w.country_id
where day like '2019-11%'
group by country_name
-- @lc code=end

