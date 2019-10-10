/*Assumptions for the teams table:
  - Assume that all temas will have names that are no more than 32 characters
  - TeamID should be unique and not null, so it's the primary key.
  - TeamName should not be null since all teams should have a name.
  - A team may not necessarily be associated with a specific city. Some are associated
    with a state like the Tennesse Titans.
*/
create table teams
	(TeamID		int,
     TeamName	varchar(32) not null,
     City		varchar(32),
     primary key (TeamID)
	);


/* Assumptions for the players table:
   - FirstName and LastName will only contain at most 32 characters and neither can be null
   - PlayerID should be unique and may not be null, therefore it is the primary key.
   - TeamID will only contain values declared in the teams table, therefore it's a foreign
     key referencing the teams table.
   - Position may only containt the values 'QB', 'RB', and 'WR', therefore it may not be null
     and it must be contrained to these three values.
	- A player may not have a negative number of touchdowns, but they may have a negative number of yards.
	- Salary for a player may not be less than 0.
*/
create table players
	(PlayerID		int,
     FirstName		varchar(32) not null,
     LastName		varchar(32) not null,
     TeamID			int,
     Position		char(2) not null check (Position in ('QB', 'RB', 'WR')),
     Touchdowns		int check (Touchdowns >= 0),
     TotalYards		int,
     Salary			int check (Salary >= 0),
     primary key (PlayerID),
     foreign key (TeamID) references teams(TeamID)
		on delete null
	);
     
     
/* Assumptions for the games table:
   - GameID must be unique and not null, therefore it will be the primary key
   - Stadium will have a maximum of 32 characters and should always be know, so cannot be null
   - The result will always be always be one of the following values: 'W', 'L', or 'T'.
   - TicketRevenue must always be greater than 0.
*/
create table games
	(GameID			int,
     Date			date,
     Stadium		varchar(32) not null,
     Result			char(1) not null check (Result in ('W', 'L', 'T')),
     Attendance 	int,
     TicketRevenue	int check (TicketRevenue >= 0),
     primary key (GameID)
	);
 
/* Assumptions for the play table:
   - Player ID and GameID will only contain values already declared in the players and games
     tables. Therefore, they will be foreign keys referenceing these two table respectively.
     Also, the primary key for this table must be the combination of PlayerID and GameID.
*/
create table play
	(PlayerID	int,
     GameID		int,
     primary key (PlayerID, GameID),
     foreign key (PlayerID) references players(PlayerID)
		on delete null,
	 foreign key (GameID) references games(GameID)
		on delete null
	);
     
