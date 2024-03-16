-- \project_{Students.FirstName, Students.LastName}(\s_{Students.Department='CS' and Enrollments.Score<90 and Courses.Department='ECE'} (Students \natural_join Enrollments \theta_join_{Enrollments.CRN=Courses.CRN} Courses) );

SELECT DISTINCT Students.FirstName, Students.LastName
FROM Students Natural Join Enrollments Join Courses Using(CRN)
WHERE Students.Department='CS' and Enrollments.Score<90 and Courses.Department='ECE'