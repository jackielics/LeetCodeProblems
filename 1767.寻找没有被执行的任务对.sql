--
-- @lc app=leetcode.cn id=1767 lang=mysql
--
-- [1767] 寻找没有被执行的任务对
--

-- @lc code=start
# Write your MySQL query statement below
/* 提前声明临时表的表名、列名 */
WITH RECURSIVE TaskList(task_id, subtask_id) AS
(
    SELECT  task_id, subtasks_count
    FROM    Tasks
    UNION ALL
    SELECT  task_id, subtask_id - 1
    FROM    TaskList
    WHERE   subtask_id > 1
)

SELECT  task_id, subtask_id
FROM    TaskList t
WHERE   NOT EXISTS (
    SELECT  task_id, subtask_id
    FROM    Executed e
    WHERE   (e.task_id, e.subtask_id) = (t.task_id, t.subtask_id)
)
-- @lc code=end

