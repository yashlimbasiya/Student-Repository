.mode csv
.separator "\t"
.import ..\\HW09\\files_HW11\\grades.txt Grades 
.import ..\\HW09\\files_HW11\\instructors.txt Instructors
.import ..\\HW09\\files_HW11\\majors.txt Majors 
.import ..\\HW09\\files_HW11\\students.txt Students 


select Name from Students where CWID = '10115';

select Major, count(*) as  total_number_of_students from Students group by Major;

select Grade, count(*) as total_students from Grades where Course = 'SSW 810' group by Grade order by count(*) desc limit 1;

select  s.CWID, s.Name, count(*) as total_number_of_courses from Students s join Grades g on s.CWID = g.StudentCWID group by s.CWID

select s.Name, s.CWID , g.Grade, g.Course, i.Name as Instructor from Students s join Grades g on s.CWID =g.StudentCWID join Instructors I on g.InstructorCWID = I.CWID order by s.Name



