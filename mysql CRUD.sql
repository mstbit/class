SELECT * FROM Artists;

INSERT INTO Artists (NAME, ID)
	VALUES ('Rylee Miller', '1');
	
INSERT INTO Artists (NAME, ID)
	VALUES ('Bud Powell', '2');

INSERT INTO Artists (NAME, ID)
	VALUES ('Bud Powell', '3');

SET SQL_SAFE_UPDATES = 0;
     
UPDATE Artists SET NAME = 'Taylor Swift'
 	WHERE (ID = 3);
     
DELETE FROM Artists
	WHERE (ID = '2');