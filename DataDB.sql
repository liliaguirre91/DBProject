INSERT INTO teams VALUES (01, 'Cardinals', 'Arizona');
INSERT INTO teams VALUES (02, 'Bears', 'Chicago');
INSERT INTO teams VALUES (03, 'Broncos', 'Denver');
INSERT INTO teams VALUES (04, 'Saints', 'New Orleans');
INSERT INTO teams VALUES (05, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (06, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (07, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (08, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (09, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (10, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (11, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (12, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (13, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (14, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (15, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (16, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (17, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (18, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (19, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (20, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (21, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (22, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (23, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (24, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (25, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (26, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (27, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (28, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (29, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (30, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (31, 'Raiders', 'Oakland');
INSERT INTO teams VALUES (32, 'Raiders', 'Oakland');

SET SQL_SAFE_UPDATES = 0;
DELETE FROM teams;
SET SQL_SAFE_UPDATES = 1;
select * from teams;



INSERT INTO players VALUES (10107, 'Brett', 'Hundley', 101, 'QB', 9, 1836, 5700000);
INSERT INTO players VALUES (10101, 'Kyler', 'Murray', 101, 'QB', 4, 1324, 2400000);
INSERT INTO players VALUES (10129, 'Chase', 'Edmonds', 101, 'RB', 2, 208, 670000);
INSERT INTO players VALUES (10137, 'D.J.', 'Foster', 101, 'RB', 0, 19, 890000);
INSERT INTO players VALUES (10111, 'Larry', 'Fitzgerald', 101, 'WR', 6, 734, 770000);
INSERT INTO players VALUES ('10112', 'Eli', 'Manning', '105', 'QB', '6', '764', '790000');
INSERT INTO players VALUES ('10151', 'Jose Luis', 'Barrera', '121', 'WR', '9', '734', '770000');

SET SQL_SAFE_UPDATES = 0;
DELETE FROM players;
SET SQL_SAFE_UPDATES = 1;
select * from players;

SET SQL_SAFE_UPDATES = 0;
LOAD DATA local INFILE '10_Players.txt' INTO TABLE players fields terminated BY ',' lines terminated BY '\n';
SET SQL_SAFE_UPDATES = 1;
select * from players;
SHOW GLOBAL VARIABLES LIKE 'local_infile';
SHOW VARIABLES LIKE 'secure_file_priv';
SET GLOBAL local_infile = 1;

INSERT INTO games VALUES (101105, '2019-10-04', 'Soldier Field', 'W', 50000, 5050000);
INSERT INTO games VALUES (101124, '2019-11-01', 'Oakland-Alameda County Coliseum', 'L', 56000, 4536000);
INSERT INTO games VALUES (109121, '2019-10-11', 'Empower Field at Mile High', 'L', 72000, 7272000);
INSERT INTO games VALUES (124128, '2019-10-18', 'CenturyLink Field', 'W', '32000', 4256000);
INSERT INTO games VALUES (101121, '2019-10-25', 'University of Phoenix Stadium', 'L', 64000, 1920000);



INSERT INTO play VALUES (10107, 101105);
INSERT INTO play VALUES (10101, 101124);
INSERT INTO play VALUES (10129, 101105);
INSERT INTO play VALUES (10137, 101124);
INSERT INTO play VALUES (10111, 101105);


