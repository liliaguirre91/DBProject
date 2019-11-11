INSERT INTO teams VALUES (101, 'Cardinals', 'Arizona');
INSERT INTO teams VALUES (105, 'Bears', 'Chicago');
INSERT INTO teams VALUES (109, 'Broncos', 'Denver');
INSERT INTO teams VALUES (121, 'Saints', 'New Orleans');
INSERT INTO teams VALUES (124, 'Raiders', 'Oakland');


INSERT INTO players VALUES (10107, 'Brett', 'Hundley', 101, 'QB', 9, 1836, 5700000);
INSERT INTO players VALUES (10101, 'Kyler', 'Murray', 101, 'QB', 4, 1324, 2400000);
INSERT INTO players VALUES (10129, 'Chase', 'Edmonds', 101, 'RB', 2, 208, 670000);
INSERT INTO players VALUES (10137, 'D.J.', 'Foster', 101, 'RB', 0, 19, 890000);
INSERT INTO players VALUES (10111, 'Larry', 'Fitzgerald', 101, 'WR', 6, 734, 770000);


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


