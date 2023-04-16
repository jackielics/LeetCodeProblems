SELECT 	DISTINCT 	title
FROM 	Content 
		LEFT JOIN	TVProgram 
		USING(content_id)
WHERE	Kids_content = 'Y'
		AND content_type = 'Movies'
		AND program_date LIKE '2020-06%'