CREATE DATABASE /*!32312 IF NOT EXISTS*/ `timetable_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE timetable_database;

CREATE TABLE IF NOT EXISTS `timetables` (
  `name` varchar(30) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `add_manually` tinyint(1) DEFAULT NULL,
  `begin_time` int DEFAULT NULL,
  `end_time` int DEFAULT NULL,
  `user` int DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `user` (`user`),
  CONSTRAINT `timetables_ibfk_1` FOREIGN KEY (`user`) REFERENCES `users` (`id`),
  CONSTRAINT `timetables_chk_1` CHECK ((`add_manually` in (0,1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `classes` (
  `name` varchar(30) NOT NULL,
  `grade` int DEFAULT NULL,
  `headcount` int DEFAULT NULL,
  `timetable` varchar(30) NOT NULL,
  PRIMARY KEY (`name`),
  KEY `timetable` (`timetable`),
  CONSTRAINT `classes_ibfk_1` FOREIGN KEY (`timetable`) REFERENCES `timetables` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `classes_subjects` (
  `class_name` varchar(30) NOT NULL,
  `subject_name` varchar(30) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `weekly_periods` int DEFAULT NULL,
  `teacher` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`class_name`,`subject_name`),
  KEY `subject_name` (`subject_name`),
  CONSTRAINT `classes_subjects_ibfk_1` FOREIGN KEY (`class_name`) REFERENCES `classes` (`name`),
  CONSTRAINT `classes_subjects_ibfk_2` FOREIGN KEY (`subject_name`) REFERENCES `subjects` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `groups` (
  `name` varchar(20) NOT NULL,
  `grade` int DEFAULT NULL,
  `headcount` int DEFAULT NULL,
  `timetable` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `timetable` (`timetable`),
  CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`timetable`) REFERENCES `timetables` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `subjects` (
  `name` varchar(30) NOT NULL,
  `timetable` varchar(30) NOT NULL,
  PRIMARY KEY (`name`),
  KEY `timetable` (`timetable`),
  CONSTRAINT `subjects_ibfk_1` FOREIGN KEY (`timetable`) REFERENCES `timetables` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `rooms` (
  `name` varchar(20) NOT NULL,
  `capacity` int DEFAULT NULL,
  `timetable` varchar(30) NOT NULL,
  PRIMARY KEY (`name`),
  KEY `timetable` (`timetable`),
  CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`timetable`) REFERENCES `timetables` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `rooms_subjects` (
  `room` varchar(20) NOT NULL,
  `subject` varchar(30) NOT NULL,
  PRIMARY KEY (`room`,`subject`),
  KEY `subject` (`subject`),
  CONSTRAINT `rooms_subjects_ibfk_1` FOREIGN KEY (`room`) REFERENCES `rooms` (`name`),
  CONSTRAINT `rooms_subjects_ibfk_2` FOREIGN KEY (`subject`) REFERENCES `subjects` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `teachers` (
  `name` varchar(30) NOT NULL,
  `balance` int DEFAULT NULL,
  `extremisms` int DEFAULT NULL,
  `begin_time` int DEFAULT NULL,
  `end_time` int DEFAULT NULL,
  `timetable` varchar(30) NOT NULL,
  PRIMARY KEY (`name`),
  KEY `timetable` (`timetable`),
  CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`timetable`) REFERENCES `timetables` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `teachers_subjects` (
  `teacher` varchar(30) NOT NULL,
  `subject` varchar(30) NOT NULL,
  PRIMARY KEY (`teacher`,`subject`),
  KEY `subject` (`subject`),
  CONSTRAINT `teachers_subjects_ibfk_1` FOREIGN KEY (`teacher`) REFERENCES `teachers` (`name`),
  CONSTRAINT `teachers_subjects_ibfk_2` FOREIGN KEY (`subject`) REFERENCES `subjects` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

