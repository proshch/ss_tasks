SELECT p.first_name, p.last_name, g.group_title FROM ((Personal_info p
INNER JOIN Students s on p.personal_info_id = s.personal_info_id)
INNER JOIN `Groups` g on s.groupID = g.groupID);

SELECT g.group_title, s.subject_title, r.lesson_date, r.audience FROM ((`Groups` g
LEFT JOIN Schedule r ON g.groupID = r.groupID)
RIGHT JOIN Subjects s ON r.subject_id = s.subject_id)
ORDER BY g.group_title DESC;

SELECT SUM(m.mark), p.last_name FROM ((Students s
INNER JOIN Personal_info p ON s.personal_info_id = p.personal_info_id)
INNER JOIN Marks m ON s.student_id = m.student_id)
GROUP BY p.last_name
HAVING MIN(m.mark > 3);

SELECT p.first_name, p.last_name, p.age, t.teacher_rank FROM Personal_info p
INNER JOIN Teachers t ON p.personal_info_id = t.personal_info_id
WHERE t.teacher_rank='professor' AND p.age < 40;

SELECT d.department_title, p.first_name, p.last_name, t.position FROM ((Departments d
INNER JOIN Teachers t ON d.department_id = t.department_id)
INNER JOIN Personal_info p ON t.personal_info_id = p.personal_info_id)
WHERE p.age BETWEEN 45 AND 55;

SELECT f.faculty_title, d.department_title, g.group_title FROM ((Faculties f
INNER JOIN Departments d ON f.faculty_id = d.faculty_id)
INNER JOIN `Groups` g ON d.department_id =  g.department_id);
