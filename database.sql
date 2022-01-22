/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - dressup
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dressup` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dressup`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) NOT NULL,
  `logistic_id` int(11) NOT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

/*Table structure for table `book` */

DROP TABLE IF EXISTS `book`;

CREATE TABLE `book` (
  `B_ID` int(11) NOT NULL AUTO_INCREMENT,
  `U_ID` int(11) NOT NULL,
  `DATE` date DEFAULT NULL,
  `TOTAL_AMOUNTT` int(11) DEFAULT NULL,
  `STATUS` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`B_ID`,`U_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `book` */

insert  into `book`(`B_ID`,`U_ID`,`DATE`,`TOTAL_AMOUNTT`,`STATUS`) values 
(1,14,'2021-09-11',0,'pending'),
(2,14,'2021-09-11',13998,'pending');

/*Table structure for table `bookitems` */

DROP TABLE IF EXISTS `bookitems`;

CREATE TABLE `bookitems` (
  `BOOKITEM_ID` int(11) NOT NULL AUTO_INCREMENT,
  `B_ID` int(11) DEFAULT NULL,
  `I_ID` int(11) DEFAULT NULL,
  `QUANTITY` int(11) DEFAULT NULL,
  `PRICE` int(11) DEFAULT NULL,
  `U_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`BOOKITEM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `bookitems` */

insert  into `bookitems`(`BOOKITEM_ID`,`B_ID`,`I_ID`,`QUANTITY`,`PRICE`,`U_ID`) values 
(1,2,1,3,3000,14),
(2,2,1,3,3000,14),
(3,2,2,2,7998,14);

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `C_ID` int(11) NOT NULL AUTO_INCREMENT,
  `U_ID` int(11) DEFAULT NULL,
  `COMPLAINTS` varchar(50) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  `REPLY` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`C_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`C_ID`,`U_ID`,`COMPLAINTS`,`DATE`,`REPLY`) values 
(1,4,'tagsgtahs thatgev ytahgshaa','2021-08-13','okkkkkkkkk'),
(2,14,'hello','2021-09-03','pending'),
(3,14,'hii','2021-09-03','pending'),
(4,14,'hello world','2021-09-10','pending'),
(5,14,'I\'m confused','2021-09-12','pending');

/*Table structure for table `design` */

DROP TABLE IF EXISTS `design`;

CREATE TABLE `design` (
  `DESIGN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `DESIGN` varchar(50) DEFAULT NULL,
  `STAFF_ID` int(11) DEFAULT NULL,
  `DETAILS` varchar(20) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  `STATUS` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`DESIGN_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `design` */

insert  into `design`(`DESIGN_ID`,`DESIGN`,`STAFF_ID`,`DETAILS`,`DATE`,`STATUS`) values 
(1,'red-nissan-gtr-r34-02.jpg',8,'shirt','2021-08-14','accepted'),
(3,'red-nissan-gtr-r34-02.jpg',8,'pants','2021-08-14','accepted'),
(4,'red-nissan-gtr-r34-02.jpg',8,'shirt','2021-08-14','pending'),
(9,'red-nissan-gtr-r34-02.jpg',8,'sfsdfs','2021-08-14','accepted');

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `E_ID` int(11) NOT NULL AUTO_INCREMENT,
  `FIRST_NAME` varchar(20) NOT NULL,
  `LAST_NAME` varchar(20) NOT NULL,
  `PLACE` varchar(20) NOT NULL,
  `POST` varchar(20) NOT NULL,
  `PIN` int(6) NOT NULL,
  `EMAIL` varchar(80) NOT NULL,
  `PHONE_NUMBER` bigint(20) NOT NULL,
  `L_ID` int(11) DEFAULT NULL,
  `TYPE` varchar(20) DEFAULT NULL,
  UNIQUE KEY `E_ID` (`E_ID`,`EMAIL`),
  UNIQUE KEY `PHONE_NUMBER_2` (`PHONE_NUMBER`),
  KEY `PHONE_NUMBER` (`PHONE_NUMBER`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `employee` */

insert  into `employee`(`E_ID`,`FIRST_NAME`,`LAST_NAME`,`PLACE`,`POST`,`PIN`,`EMAIL`,`PHONE_NUMBER`,`L_ID`,`TYPE`) values 
(1,'mm','hh','hhhhh','jjjjj',8888,'ggggggg',888888,2,'SELLERS'),
(2,'aa','bb','cc','ss',4444,'seddd',56676666,3,'SELLERS'),
(3,'aathif ','shahil ','clt','clt',673355,'aathifaathu@gmail.co',9605221888,5,'LOGISTICS'),
(4,'alok','mahesh','mahe','mahe',673311,'alokallu@gmail.com',9999999998,6,'SELLERS'),
(5,'misbah','sulthan','thalassery','ssroad',0,'misbamisbu@gmail.com',0,7,'LOGISTICS'),
(6,'fahad','yousaf','mahe','mahe',673312,'fahadyusaf000@gmail.',8129903932,8,'DESIGNERS');

/*Table structure for table `feedbacks` */

DROP TABLE IF EXISTS `feedbacks`;

CREATE TABLE `feedbacks` (
  `F_ID` int(11) NOT NULL AUTO_INCREMENT,
  `U_ID` int(11) DEFAULT NULL,
  `FEEDBACK` varchar(60) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  PRIMARY KEY (`F_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `feedbacks` */

insert  into `feedbacks`(`F_ID`,`U_ID`,`FEEDBACK`,`DATE`) values 
(1,4,'iysuuebc eubssd dh','2021-08-13'),
(2,14,'Send','2021-09-03'),
(3,14,'Send','2021-09-03'),
(4,14,'hii','2021-09-03'),
(5,14,'hello hii','2021-09-04'),
(6,14,'hi , I\'m fadhil yousaf k','2021-09-12'),
(7,14,'aathifshahilapppp','2021-09-15');

/*Table structure for table `interact` */

DROP TABLE IF EXISTS `interact`;

CREATE TABLE `interact` (
  `L_ID` int(11) NOT NULL AUTO_INCREMENT,
  `FROM_ID` int(11) DEFAULT NULL,
  `TO_ID` int(11) DEFAULT NULL,
  `MESSAGE` varchar(60) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  `TYPE` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`L_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `interact` */

insert  into `interact`(`L_ID`,`FROM_ID`,`TO_ID`,`MESSAGE`,`DATE`,`TYPE`) values 
(1,8,6,'hi aathif','2021-08-19','sellers'),
(2,6,8,'hi fahhad','2021-08-19','designers'),
(3,14,6,'hello00009','2021-09-10','user'),
(4,6,14,'hiiiiii','2021-09-10','sellers'),
(5,14,6,'hi fadhil here','2021-09-12','user');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `L_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(50) NOT NULL,
  `PASSWORD` varchar(50) DEFAULT NULL,
  `U_TYPE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`L_ID`),
  UNIQUE KEY `USERNAME` (`USERNAME`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`L_ID`,`USERNAME`,`PASSWORD`,`U_TYPE`) values 
(1,'admin','123456','admin'),
(2,'admin1','123456','SELLERS'),
(3,'admin2','123456','SELLERS'),
(4,'aaaa','6627d','user'),
(5,'admin3','123456','LOGISTICS'),
(6,'admin4','123456','SELLERS'),
(7,'admin5','123456','LOGISTICS'),
(8,'fahad','fahad123','DESIGNERS'),
(10,'aathif11','aathif11','user'),
(11,'adil','adil11','user'),
(13,'aktharali','aktharali','user'),
(14,'niyasniyu','niyas112233','user'),
(16,'fadhil','fadhil','user'),
(17,'vishnu','vishnuuu','user'),
(18,'uname','password','user'),
(19,'ababab','bababa','user'),
(20,'user','12345678','user'),
(21,'usernamen','password','user'),
(22,'userqwerty','password','user');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `P_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ITEM_NAME` varchar(20) DEFAULT NULL,
  `QUANTITY` int(11) DEFAULT NULL,
  `RATE` int(11) DEFAULT NULL,
  `PHOTO` varchar(50) DEFAULT NULL,
  `COLOUR` varchar(50) DEFAULT NULL,
  `DATE` date DEFAULT NULL,
  PRIMARY KEY (`P_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`P_ID`,`ITEM_NAME`,`QUANTITY`,`RATE`,`PHOTO`,`COLOUR`,`DATE`) values 
(1,'tshirt',17,1000,'wonder_woman.jpg','blue','2021-08-13'),
(2,'shirt',27,3999,'red-nissan-gtr-r34-02.jpg','white','2021-08-13'),
(3,'pants',20,4000,'red-nissan-gtr-r34-02.jpg','black','2021-08-13'),
(4,'pant',0,999,'red-nissan-gtr-r34-02.jpg','red','2021-08-19');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `U_ID` int(11) NOT NULL AUTO_INCREMENT,
  `F_NAME` varchar(20) DEFAULT NULL,
  `L_NAME` varchar(20) DEFAULT NULL,
  `PHONE_NUMBER` int(20) DEFAULT NULL,
  `PLACE` varchar(20) DEFAULT NULL,
  `POST` varchar(20) DEFAULT NULL,
  `EMAIL` varchar(20) NOT NULL,
  `loginid` int(11) DEFAULT NULL,
  UNIQUE KEY `U_ID` (`U_ID`,`EMAIL`),
  UNIQUE KEY `EMAIL` (`EMAIL`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`U_ID`,`F_NAME`,`L_NAME`,`PHONE_NUMBER`,`PLACE`,`POST`,`EMAIL`,`loginid`) values 
(1,'aa','ttu',763547,'mahe','mahe','gggg',4),
(2,'niyas','ashraf',2147483647,'monthaal','chokli','niyasashraf@gmail.co',14),
(3,'fadhil','',2147483647,'mahe','mahe','fadhil@gmail.com',16),
(4,'vishnu','',111111111,'ppppp','post','vishnu@gmail.com',17),
(5,'adil','adi',0,'place','post','email@gmail.com',18),
(6,'ababab','bababa',99999999,'place','post','mail@gmail.com',19),
(7,'firstname','lastname',123456789,'place','post','mailidid@gmail.com',20),
(8,'haha','haha',11223344,'place','post','mailmail@gmail.com',21),
(9,'ffff','hhhh',2147483647,'place','post','mailmailmail@gmqil.c',22);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
