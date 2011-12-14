-- MySQL dump 10.13  Distrib 5.1.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: doodle
-- ------------------------------------------------------
-- Server version	5.1.54-1ubuntu4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `guess`
--

DROP TABLE IF EXISTS `guess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guess` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `guesser_id` bigint(20) NOT NULL,
  `guessed_id` bigint(20) NOT NULL,
  `constellation_id` int(11) NOT NULL,
  `rate` int(11) DEFAULT '0',
  `datetime` datetime DEFAULT NULL,
  `count` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `guesser_id` (`guesser_id`,`guessed_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `constellation_id` int(11) DEFAULT '0',
  `guesser_count` int(11) DEFAULT '0',
  `guessed_count` int(11) DEFAULT '0',
  `score` bigint(20) DEFAULT '0',
  `rate` int(11) DEFAULT '0',
  `user_count` int(11) DEFAULT '0',
  `user_hit` int(11) DEFAULT '0',
  `user_miss` int(11) DEFAULT '0',
  `star_count` int(11) DEFAULT '0',
  `star_miss` int(11) DEFAULT '0',
  `notice` int(11) DEFAULT '0',
  `role` int(11) DEFAULT '0',
  `status` int(11) DEFAULT '0',
  `login_ip` varchar(20) DEFAULT '',
  `login_datetime` datetime DEFAULT NULL,
  `signin_datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `weibo`
--

DROP TABLE IF EXISTS `weibo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weibo` (
  `id` bigint(20) NOT NULL,
  `at_key` varchar(50) DEFAULT '',
  `at_secret` varchar(50) DEFAULT '',
  `name` varchar(20) DEFAULT '',
  `screen_name` varchar(20) DEFAULT '',
  `domain` varchar(20) DEFAULT '',
  `profile_image_url` varchar(255) DEFAULT '',
  `gender` char(1) DEFAULT '',
  `description` varchar(500) DEFAULT '',
  `city` int(11) DEFAULT '0',
  `province` int(11) DEFAULT '0',
  `location` varchar(500) DEFAULT '',
  `created_at` varchar(50) DEFAULT '',
  `credentials_num` bigint(20) DEFAULT '0',
  `credentials_type` int(11) DEFAULT '0',
  `lang` varchar(50) DEFAULT '',
  `birthday` varchar(50) DEFAULT '',
  `birthday_visible` int(11) DEFAULT '0',
  `email` varchar(50) DEFAULT '',
  `email_visible` int(11) DEFAULT '0',
  `msn` varchar(50) DEFAULT '',
  `msn_visible` int(11) DEFAULT '0',
  `qq` varchar(50) DEFAULT '',
  `qq_visible` int(11) DEFAULT '0',
  `real_name` varchar(10) DEFAULT '',
  `real_name_visible` int(11) DEFAULT '0',
  `url` varchar(50) DEFAULT '',
  `url_visible` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-13 22:21:36
