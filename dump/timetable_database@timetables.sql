-- MySQLShell dump 1.0.1  Distrib Ver 8.0.22 for Win64 on x86_64 - for MySQL 8.0.22 (MySQL Community Server (GPL)), for Win64 (x86_64)
--
-- Host: localhost    Database: timetable_database    Table: timetables
-- ------------------------------------------------------
-- Server version	8.0.23

--
-- Table structure for table `timetables`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;
