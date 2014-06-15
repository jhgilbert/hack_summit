BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL
);
INSERT INTO "alembic_version" VALUES('10e323d520eb');
CREATE TABLE friends (
	lender_id INTEGER NOT NULL, 
	friend_id INTEGER NOT NULL, 
	FOREIGN KEY(lender_id) REFERENCES lenders (id), 
	FOREIGN KEY(friend_id) REFERENCES lenders (id)
);
CREATE TABLE lenders (
	id INTEGER NOT NULL, 
	username VARCHAR(200) NOT NULL, 
	json BLOB, facebook_id VARCHAR(200), work VARCHAR(200), location VARCHAR(200), hometown VARCHAR(200), 
	PRIMARY KEY (id)
);
CREATE TABLE loan_lenders (
	id INTEGER NOT NULL, 
	json BLOB, 
	PRIMARY KEY (id)
);
CREATE TABLE loans (
	id INTEGER NOT NULL, 
	json BLOB, status VARCHAR(50), is_staff_pick BOOLEAN, 
	PRIMARY KEY (id)
);
CREATE TABLE recommendations (
	id INTEGER NOT NULL, 
	lender_id INTEGER NOT NULL, 
	loan_id INTEGER NOT NULL, 
	score INTEGER, 
	PRIMARY KEY (id)
);
COMMIT;
