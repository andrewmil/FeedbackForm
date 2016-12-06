CREATE DATABASE feedback2;

  CREATE TABLE feedback (
      id int,
      satisfaction varChar(100),
      timeEntered timestamp,
      comment text,
      surveyID int,
      PRIMARY KEY (id)
  );
