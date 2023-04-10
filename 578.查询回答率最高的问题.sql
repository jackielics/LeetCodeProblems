--
-- @lc app=leetcode.cn id=578 lang=mysql
--
-- [578] 查询回答率最高的问题
--

-- @lc code=start
# Write your MySQL query statement below
SELECT  question_id AS `survey_log`
FROM    
    (SELECT question_id, 
            COUNT(1) OVER( PARTITION BY question_id
                            ) AS `num_show`
    FROM    SurveyLog
    where   action = 'show') AS `ST`
    LEFT JOIN(  SELECT  question_id, 
                        COUNT(1) OVER( PARTITION BY question_id
                                        ) AS `num_answer`
                FROM    SurveyLog
                where   action = 'answer') AS `AT`
    USING   (question_id)
ORDER BY    `num_answer` / `num_show` DESC, question_id ASC
LIMIT  1

/* 大神的方法1：用SUM+IF实现计数的效果 */
select question_id as survey_log
from (
  select
      question_id,
      sum(if(action = 'answer', 1, 0)) as AnswerCnt,
      sum(if(action = 'show', 1, 0)) as ShowCnt
  from
      survey_log
  group by question_id
) as tbl
order by (AnswerCnt / ShowCnt) desc
limit 1

/* 大神的方法2：不使用子查询，直接排序 */
select question_id as survey_log
from survey_log
group by question_id
order by sum(if(action = 'answer', 1, 0)) / sum(if(action = 'show', 1, 0)) desc
limit 1

-- @lc code=end

