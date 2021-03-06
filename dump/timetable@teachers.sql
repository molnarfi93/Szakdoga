-- MySQLShell dump 1.0.1  Distrib Ver 8.0.22 for Win64 on x86_64 - for MySQL 8.0.22 (MySQL Community Server (GPL)), for Win64 (x86_64)
--
-- Host: localhost    Database: timetable    Table: teachers
-- ------------------------------------------------------
-- Server version	8.0.23

--
-- Table structure for table `teachers`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;
