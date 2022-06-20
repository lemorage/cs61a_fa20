.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;
  -- the smallest unique integer is 15, BTW

CREATE TABLE matchmaker AS
  SELECT t1.pet, t1.song, t1.color, t2.color FROM students AS t1, students AS t2
  WHERE t1.pet = t2.pet AND t1.song = t2.song AND t1.time < t2.time;


CREATE TABLE sevens AS
  SELECT seven FROM students AS a, numbers AS b WHERE a.time = b.time AND a.number = 7 AND b.'7' = 'True';

