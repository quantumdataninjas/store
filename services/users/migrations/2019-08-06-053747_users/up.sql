CREATE TABLE users (
  email VARCHAR(100) NOT NULL PRIMARY KEY,
  subscribed BOOLEAN NOT NULL,
  termsandconditions BOOLEAN NOT NULL,
  username VARCHAR(50),
  firstname VARCHAR(50),
  lastname VARCHAR(50),
  address1 VARCHAR(100),
  address2 VARCHAR(100),
  city VARCHAR(50),
  state VARCHAR(50),
  zipcode VARCHAR(15),
  country VARCHAR(50),
  phone VARCHAR(15),
  birthmonth VARCHAR(10),
  birthday SMALLINT,
  birthyear SMALLINT,
  online BOOLEAN NOT NULL,
  lastlogin TIMESTAMP NOT NULL,
  lastlogout TIMESTAMP NOT NULL,
  -- hash VARCHAR(122) NOT NULL, --argon hash
  created_at TIMESTAMP NOT NULL
);
