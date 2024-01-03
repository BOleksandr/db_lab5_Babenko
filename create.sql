CREATE TABLE Cellphone
(
  cellphone_id INT NOT NULL,
  model CHAR(50) NOT NULL,
  brand CHAR(50) NOT NULL,
  PRIMARY KEY (cellphone_id)
);

CREATE TABLE Users
(
  user_id INT NOT NULL,
  age INT NOT NULL,
  gender CHAR(10),
  profession CHAR(100),
  PRIMARY KEY (user_id)
);

CREATE TABLE Characteristic
(
  main_camera INT NOT NULL,
  internal_memory INT NOT NULL,
  battery_size INT NOT NULL,
  ram INT NOT NULL,
  selfie_camera INT NOT NULL,
  os CHAR(20) NOT NULL,
  cellphone_id INT NOT NULL,
  PRIMARY KEY (cellphone_id),
  FOREIGN KEY (cellphone_id) REFERENCES Cellphone(cellphone_id)
);

CREATE TABLE Rating
(
  grade INT NOT NULL,
  user_id INT NOT NULL,
  cellphone_id INT NOT NULL,
  PRIMARY KEY (user_id, cellphone_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (cellphone_id) REFERENCES Cellphone(cellphone_id)
);