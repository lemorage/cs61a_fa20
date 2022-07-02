CREATE TABLE scoring AS
  SELECT "Donald Stewart" AS player, 7 AS points, 1 AS quarter UNION
  SELECT "Christopher Brown Jr.", 7, 1 UNION
  SELECT "Ryan Sanborn", 3, 2 UNION
  SELECT "Greg Thomas", 3, 2 UNION
  SELECT "Cameron Scarlett", 7, 3 UNION
  SELECT "Nikko Remigio", 7, 4 UNION
  SELECT "Ryan Sanborn", 3, 4 UNION
  SELECT "Chase Garbers", 7, 4;

CREATE TABLE players AS
  SELECT "Ryan Sanborn" AS name, "Stanford" AS team UNION
  SELECT "Donald Stewart", "Stanford" UNION
  SELECT "Cameron Scarlett", "Stanford" UNION
  SELECT "Christopher Brown Jr.", "Cal" UNION
  SELECT "Greg Thomas", "Cal" UNION
  SELECT "Nikko Remigio", "Cal" UNION
  SELECT "Chase Garbers", "Cal";


-- 8.1
SELECT quarter
  FROM scoring
  GROUP BY quarter
  HAVING SUM(points) > 10;


-- 8.2
SELECT SUM(points), team
  FROM scoring, players
  WHERE name = player
  GROUP BY team