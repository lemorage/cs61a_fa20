-- Questions --

-- 2.1
/*
Write a query that outputs the names of employees that Oliver Warbucks directly
supervises.
*/
SELECT Name FROM records WHERE Supervisor = "Oliver Warbucks";


-- 2.2
/*
Write a query that outputs all information about employees that supervise
themselves.
*/
SELECT * FROM records WHERE Supervisor = Name;


-- 2.3
/*
Write a query that outputs the names of all employees with salary greater
than 50,000 in alphabetical order.
*/
SELECT Name FROM records WHERE Salary > 50000 ORDER BY Name;


-- 3.1
/*
Write a query that outputs the meeting days and times of all employees
directly supervised by Oliver Warbucks.
*/
SELECT Day, Time FROM records AS r, meetings AS m 
	WHERE Supervisor = 'Oliver Warbucks' AND
		r.Division = m.Division;


-- 3.2
/*
Write a query that outputs the names of all pairs of employees that have a
meeting at the same time. Make sure that if A|B appears in your output, B|A
does not appear as well.
*/
SELECT r1.name, r2.name
	FROM records AS r1, records AS r2, meetings AS m1, meetings AS m2
	WHERE r1.Division = m1.Division AND r2.Division = m2.Division AND
		m1.Day = m2.Day AND m1.Time = m2.Time AND r1.name < r2.name;


-- 3.3
/* No, this works iff the division here has single meetings. */


-- 3.4
/*
Write a query that outputs the names of employees whose supervisor is in a
different division.
*/
SELECT r1.Name
	FROM records AS r1, records AS r2
	WHERE r1.Supervisor = r2.Name AND r1.Division <> r2.Division AND
		r1.Name < r2.Name;


-- 4.1
/*
Write a query that outputs each supervisor and the sum of salaries of all the
employees they supervise.
*/
SELECT Supervisor, SUM(salary) FROM records GROUP BY Supervisor;


-- 4.2
/*
Write a query that outputs the days of the week for which fewer than 5 employees
have a meeting. You may assume no department has more than one meeting on a
given day.
*/
SELECT Day FROM records AS r, meetings AS m
	WHERE r.Division = m.Division
		GROUP BY Day HAVING count(*) < 5;


-- 4.3
/*
Write a query that outputs all divisions for which there is more than one
employee, and all pairs of employees within that division that have a combined
salary less than 100,000.
*/
SELECT Division FROM records
	GROUP BY Division HAVING COUNT(*) > 1 AND SUM(salary) < 100000; 


-- 5.1 short question
-- 15 rows will be contained


-- 5.1
/*
Create a table called num_taught that contains three columns: professor, the
course they taught, and the number of times they taught each course.
*/
CREATE TABLE num_taught AS
	SELECT professor AS professor, course AS course, COUNT(*) AS times
	FROM courses GROUP BY professor, course;


-- 5.2
/*
Write a query that outputs two professors and a course if they have taught that
course the same number of times. You may use the num taught table you created
in the previous question.
*/
SELECT n1.professor, n2.professor, n1.course
	FROM num_taught AS n1, num_taught AS n2
	WHERE n1.professor < n2.professor AND n1.course = n2.course AND
		n1.times = n2.times;


-- 5.3
/*
Write a query that outputs two professors if they co-taught (taught the same
course at the same time) the same course more than once.
*/
SELECT a.professor, b.professor
	FROM courses AS a, courses AS b
	WHERE a.professor < b.professor AND
		a.semester = b.semester AND a.course = b.course
	GROUP BY a.course, a.professor, b.professor HAVING COUNT(*) > 1;
