DROP DATABASE IF EXISTS `test`;
CREATE DATABASE `test`;
USE `test`;

CREATE TABLE IF NOT EXISTS `User` (
  `user_id` INT ,
  `user_name` VARCHAR(255),
  `password` VARCHAR(255),
  PRIMARY KEY (`user_id`)
) ;

CREATE TABLE IF NOT EXISTS `User_Info` (
  `user_id` INT ,
  `nick_name` VARCHAR(255),
  `gender` VARCHAR(255),
  `about` VARCHAR(255),
  PRIMARY KEY (`user_id`)
) ;

CREATE TABLE IF NOT EXISTS `DAG` (
	`graph_id` INT ,
  `graph_name` VARCHAR(255),
	`owner_id` INT,
  `abstract` VARCHAR(999) DEFAULT "",
	PRIMARY KEY (`graph_id`)
);

CREATE TABLE IF NOT EXISTS `DAG_Group` (
	`graph_id` INT,
	`user_id` INT,
	PRIMARY KEY (`graph_id`,`user_id`)
);


CREATE TABLE IF NOT EXISTS `DAG_Node` (
  `task_id` INT ,
  `graph_id` INT ,
  PRIMARY KEY (`task_id`)
);

CREATE TABLE IF NOT EXISTS `DAG_Edge` (
  `begin_TID` INT ,
  `end_TID` INT,
  PRIMARY KEY (`begin_TID`,`end_TID`)
);

CREATE TABLE IF NOT EXISTS `Node` (
  `task_id` INT,
  `owner_id` INT,
  `task_name` VARCHAR(255),
  `version` INT,
  `status` VARCHAR(255),
  PRIMARY KEY (`task_id`)
);

CREATE TABLE IF NOT EXISTS `Node_Group` (
  `task_id` INT ,
  `user_id` INT ,
  PRIMARY KEY (`task_id`,`user_id`)
);

CREATE TABLE IF NOT EXISTS `Node_Details` (
  `task_id` INT ,
  `abstract` VARCHAR(999),
  `due_date` date DEFAULT NULL,
  PRIMARY KEY (`task_id`)
);

CREATE TABLE IF NOT EXISTS `Constraint` (
  `begin_TID` INT ,
  `end_TID` INT,
  PRIMARY KEY (`begin_TID`,`end_TID`)
) ;


INSERT INTO `User`(`user_id`,`user_name`,`password`) VALUES
(111,'rick1223','40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(222,'taylor1233','40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(333,'sponge1234','40bd001563085fc35165329ea1ff5c5ecbdbbeef')
;

INSERT INTO `User_Info` VALUES
(111,'rick','Male','A great engineer.'),
(222,'taylor','Female','An experienced drawer.'),
(333,'sponge','Male','Just a piece of sponge.')
;


INSERT INTO `DAG`(`graph_id`, `graph_name`, `owner_id`) VALUES
(000,'Database' ,111),
(001,'UML' , 222),
(003,'Android' ,333)
;

INSERT INTO `DAG_Group`VALUES
(000,111),
(000,333),
(001,111)
;

INSERT INTO `Node` VALUES
(1001,111,'wash',0,'False'),
(2002,111,'read',0,'False'),
(3003,111,'play',0,'False'),
(4004,111,'sign',0,'False'),
(6006,111,'drink',0,'False'),
(5005,111,'swim',0,'False')
;

INSERT INTO `DAG_Node` VALUES
(1001,000),
(2002,000),
(3003,000),
(4004,000),
(5005,000),
(6006,000)
;

INSERT INTO `DAG_Edge` VALUES
(1001,2002),
(2002,3003),
(2002,4004),
(4004,5005),
(5005,6006)
;



INSERT INTO `Node_Group` VALUES
(1001,111),
(1001,222),
(1001,333)
;

INSERT INTO `Node_Details` VALUES
(1001,"Finish it as soon as possible",NULL),
(2002,"Nothing :)",NULL),
(3003,"Eh - -",NULL),
(4004,"Oh!",NULL),
(5005,"Ouch!",NULL),
(6006,"Wow!",NULL)
;






