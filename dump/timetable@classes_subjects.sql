-- MySQLShell dump 1.0.1  Distrib Ver 8.0.22 for Win64 on x86_64 - for MySQL 8.0.22 (MySQL Community Server (GPL)), for Win64 (x86_64)
--
-- Host: localhost    Database: timetable    Table: classes_subjects
-- ------------------------------------------------------
-- Server version	8.0.23

--
-- Table structure for table `classes_subjects`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;
