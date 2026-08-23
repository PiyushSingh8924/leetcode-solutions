# Write your MySQL query statement below
Select p.firstName,p.lastName,a.state,city
from person p
left join Address a
on p.personId = a.personId