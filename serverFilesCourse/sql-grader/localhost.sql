-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 12, 2019 at 06:43 PM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coffeeshopes`
--
CREATE DATABASE IF NOT EXISTS `coffeeshopes` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `coffeeshopes`;

-- --------------------------------------------------------

--
-- Table structure for table `Cafe`
--

CREATE TABLE `Cafe` (
  `name` varchar(20) NOT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `license` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Cafe`
--

INSERT INTO `Cafe` (`name`, `addr`, `license`) VALUES
('Aroma', 'Ribeira Quente', '12-3547386'),
('Brewlab', 'Santo Niño', '56-2671118'),
('Caffe Bene', 'Paço', '72-2304565'),
('Espresso Royal', 'Huyuan', '04-1458851'),
('etc.', 'Lauro de Freitas', '18-4566120'),
('Hammerhead', 'Balangiga', '41-6976685'),
('Starbucks', 'Lahishyn', '83-9980457');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `name` varchar(50) NOT NULL,
  `addr` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`name`, `addr`, `phone`) VALUES
('Abbe', 'Los Arcos', '379-377-7338'),
('Adey', 'Yinla', '859-594-2141'),
('Alfonse', 'Ponta Grossa', '834-949-1574'),
('Alina', 'Alexandria', '202-826-2084'),
('Alisa', 'Shaghat', '981-654-2871'),
('Alvina', 'Oshnavīyeh', '874-885-5592'),
('Ariana', 'Klaeng', '369-137-8276'),
('Armin', 'Daojiang', '434-553-7391'),
('Averil', 'Vorob’yovo', '583-450-7880'),
('Barney', 'Devin', '183-691-5121'),
('Benedetto', 'Berlin', '466-200-6188'),
('Benjy', 'Zborovice', '858-608-3877'),
('Blake', 'Yuanmen', '905-867-8415'),
('Bob', 'Oepuah', '160-908-3730'),
('Borg', 'Kiruru', '925-971-1029'),
('Brigitta', 'Ivanishchi', '526-869-4414'),
('Carlie', 'Lat Yao', '541-459-1648'),
('Cathlene', 'Beihe', '280-137-6921'),
('Cesar', 'Non Sung', '358-733-3460'),
('Clarey', 'Dingqing', '616-499-6448'),
('Claudelle', 'São Cristóvão', '866-845-9573'),
('Dane', 'Patrída', '881-334-5778'),
('Danit', 'Barraute', '513-570-9175'),
('Darleen', 'Georgiyevsk', '995-146-3229'),
('Davon', 'Dunaivtsi', '966-769-6261'),
('Dorian', 'Xi’an', '832-852-6960'),
('Eduino', 'Ijuw', '265-281-1405'),
('Elbertina', 'Blagnac', '721-170-4837'),
('Elsey', 'Xingdian', '441-593-5025'),
('Ernaline', 'Taoyuan', '939-614-8663'),
('Ernesta', 'Oslo', '511-730-6976'),
('Felix', 'Strasbourg', '813-901-3622'),
('Fionna', 'Pasararba', '958-679-6365'),
('Garvy', 'Mikulášovice', '202-984-6191'),
('Geno', 'Iguape', '687-713-0792'),
('Georgeta', 'Doloplazy', '311-990-8913'),
('Hanna', 'Przemków', '621-883-5804'),
('Hansiain', 'Wilczyce', '632-203-9328'),
('Henriette', 'Daga', '615-553-3235'),
('Herculie', 'Canauay', '835-181-0884'),
('Isabelle', 'Bendoroto', '269-961-1221'),
('Issy', 'Layo', '767-796-2445'),
('Jake', 'Krajan Dua Patempuran', '642-213-4851'),
('Jeremias', 'Walagar', '741-724-9057'),
('Joana', 'Touho', '856-688-6090'),
('Jocelyn', 'Saskylakh', '492-566-8173'),
('Johann', 'Guanchao', '953-588-6809'),
('Jorgan', 'Farsta', '460-456-1973'),
('Kary', 'Vihti', '824-878-1799'),
('Khalil', 'Bërxull', '422-877-7048'),
('Lee', 'Póvoa de Santo António', '582-368-4048'),
('Lilyan', 'Mayrtup', '282-976-4350'),
('Lissa', 'Saint Lucia', '596-605-3840'),
('Lorna', 'Pingxi', '878-754-4513'),
('Maggy', 'Vukojevci', '568-463-1791'),
('Marchall', 'La Virtud', '186-478-6108'),
('Margalit', 'Kwali', '674-160-5144'),
('Marje', 'Gaïtánion', '876-646-9280'),
('Maryjo', 'Balqash', '234-860-2958'),
('Megen', 'Ilihan', '909-201-8159'),
('Mellicent', 'Kunčice pod Ondřejníkem', '565-304-2357'),
('Moll', 'Nagqu', '333-428-5257'),
('Mozes', 'Concepcion', '261-271-3074'),
('Nichole', 'Opatówek', '797-570-0237'),
('Oliy', 'Shiyun', '725-931-3036'),
('Orton', 'Harstad', '674-203-6203'),
('Patin', 'Salem', '522-263-0320'),
('Pearl', 'Xinzhou', '661-949-0317'),
('Phil', 'Vnukovo', '801-615-4586'),
('Pietra', 'Zhouji', '271-549-3102'),
('Rafa', 'Eslāmābād', '578-411-7391'),
('Rahel', 'Fundación', '873-463-0116'),
('Reece', 'Kauhava', '500-517-9682'),
('Ritchie', 'Vidče', '659-876-8333'),
('Rodolphe', 'Badulla', '943-293-8893'),
('Rosemarie', 'Guintubhan', '468-586-0338'),
('Sayre', 'Merke', '311-589-4267'),
('Seth', 'Da’an', '913-222-5435'),
('Shannah', 'Mankono', '784-485-8749'),
('Sharleen', 'Gýtheio', '976-467-0700'),
('Shina', 'Aracaju', '770-437-2321'),
('Spense', 'Colorado', '478-126-2602'),
('Stefan', 'Anju', '209-358-2245'),
('Suzanne', 'Semiluki', '687-336-3119'),
('Tate', 'Sé', '980-642-7828'),
('Terri-jo', 'Energeticheskiy', '319-242-2381'),
('Thaddus', 'Encruzilhada do Sul', '115-521-4936'),
('Thomas', 'Caetité', '775-340-0609'),
('Tim', 'Minle', '606-253-8241'),
('Torey', 'Daijiaba', '588-126-4330'),
('Tyson', 'Novopavlovsk', '514-649-6826'),
('Ulysses', 'Modimolle', '554-934-0092'),
('Urbano', 'Shalang', '839-527-2579'),
('Vally', 'Xianju', '606-953-1118'),
('Vanya', 'Glagahan', '420-925-2941'),
('Virgil', 'Cibitung', '731-696-6393'),
('Wain', 'Choa Saidān Shāh', '386-210-9196'),
('Welsh', 'Sizao', '623-712-0482'),
('Wright', 'Dublje', '639-433-6406');

-- --------------------------------------------------------

--
-- Table structure for table `Drinks`
--

CREATE TABLE `Drinks` (
  `name` varchar(20) NOT NULL,
  `manf` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Drinks`
--

INSERT INTO `Drinks` (`name`, `manf`) VALUES
('Cappuccino', 'Dare-Vandervort'),
('Cappuccino', 'Larson-O\'Connell'),
('Cappuccino', 'Monahan-Marvin'),
('Cappuccino', 'Runte Group'),
('Cappuccino', 'Schroeder-Gislason'),
('Cappuccino', 'Schuster-Lueilwitz'),
('Cappuccino', 'Spencer-Wehner'),
('Cappuccino', 'Thompson Group'),
('Espresso', 'Blanda Inc'),
('Espresso', 'Crona and Sons'),
('Espresso', 'Hammes-Williamson'),
('Espresso', 'Harris-Schneider'),
('Espresso', 'Huel Inc'),
('Espresso', 'Johnston and Sons'),
('Espresso', 'Rodriguez-Labadie'),
('Espresso', 'Stark-Hand'),
('Espresso', 'Stroman-Waelchi'),
('Latte', 'Auer Group'),
('Latte', 'Batz and Sons'),
('Latte', 'Beier-Windler'),
('Latte', 'Bogan Inc'),
('Latte', 'Crooks-Connelly'),
('Latte', 'Crooks-Stracke'),
('Latte', 'Frami LLC'),
('Latte', 'Quitzon-Mraz'),
('Latte', 'Satterfield-DuBuque'),
('Latte', 'Turner-Kuhn'),
('Latte', 'Wilderman Group'),
('Macchiato', 'Bednar LLC'),
('Macchiato', 'Bernhard-Renner'),
('Macchiato', 'Daniel-Kuhn'),
('Macchiato', 'Dare and Sons'),
('Macchiato', 'Friesen-Pfannerstill'),
('Macchiato', 'Goldner Inc'),
('Macchiato', 'Nolan Group'),
('Macchiato', 'Rogahn and Sons'),
('Macchiato', 'Schamberger and Sons'),
('Macchiato', 'Schmidt-McClure'),
('Macchiato', 'Schneider Inc'),
('Mocha', 'Becker LLC'),
('Mocha', 'Donnelly-Gaylord'),
('Mocha', 'Harber Group'),
('Mocha', 'Hegmann Inc'),
('Mocha', 'Kerluke-Botsford'),
('Mocha', 'Nikolaus-Roob'),
('Mocha', 'O\'Conner Group'),
('Mocha', 'Purdy, Johns and Fay'),
('Mocha', 'Wisoky and Sons'),
('White Mocha', 'Abshire-McLaughlin'),
('White Mocha', 'Bernier LLC'),
('White Mocha', 'Bogan Inc'),
('White Mocha', 'Braun-Wunsch'),
('White Mocha', 'Dare LLC'),
('White Mocha', 'Gislason-Effertz'),
('White Mocha', 'Howe-Ondricka'),
('White Mocha', 'Kozey Inc'),
('White Mocha', 'Quitzon and Sons'),
('White Mocha', 'Steuber Group'),
('White Mocha', 'Stroman LLC'),
('White Mocha', 'Toy, Kulas and Fay'),
('White Mocha', 'Wisozk Inc');

-- --------------------------------------------------------

--
-- Table structure for table `Frequents`
--

CREATE TABLE `Frequents` (
  `customer` varchar(20) NOT NULL,
  `cafe` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Frequents`
--

INSERT INTO `Frequents` (`customer`, `cafe`) VALUES
('Alina', 'Aroma'),
('Alina', 'Espresso Royal'),
('Alvina', 'Espresso Royal'),
('Armin', 'Aroma'),
('Averil', 'Brewlab'),
('Averil', 'Caffe Bene'),
('Averil', 'etc.'),
('Barney', 'etc.'),
('Bob', 'Brewlab'),
('Borg', 'etc.'),
('Borg', 'Hammerhead'),
('Borg', 'Starbucks'),
('Carlie', 'Aroma'),
('Dane', 'Aroma'),
('Dane', 'Espresso Royal'),
('Danit', 'Hammerhead'),
('Darleen', 'Aroma'),
('Dorian', 'Brewlab'),
('Eduino', 'Brewlab'),
('Eduino', 'etc.'),
('Elbertina', 'Aroma'),
('Elsey', 'Caffe Bene'),
('Ernaline', 'Caffe Bene'),
('Felix', 'Caffe Bene'),
('Fionna', 'Caffe Bene'),
('Garvy', 'etc.'),
('Hanna', 'Starbucks'),
('Herculie', 'Caffe Bene'),
('Herculie', 'Starbucks'),
('Isabelle', 'Brewlab'),
('Jeremias', 'Caffe Bene'),
('Joana', 'Espresso Royal'),
('Jocelyn', 'Brewlab'),
('Jocelyn', 'Hammerhead'),
('Johann', 'Brewlab'),
('Johann', 'Caffe Bene'),
('Johann', 'etc.'),
('Johann', 'Starbucks'),
('Jorgan', 'Caffe Bene'),
('Kary', 'Brewlab'),
('Kary', 'Caffe Bene'),
('Lee', 'Caffe Bene'),
('Lee', 'Espresso Royal'),
('Lilyan', 'Aroma'),
('Lissa', 'Brewlab'),
('Lissa', 'Caffe Bene'),
('Maggy', 'Espresso Royal'),
('Maggy', 'Starbucks'),
('Marchall', 'Aroma'),
('Marje', 'Aroma'),
('Marje', 'Caffe Bene'),
('Megen', 'Brewlab'),
('Megen', 'etc.'),
('Mellicent', 'Aroma'),
('Mellicent', 'etc.'),
('Nichole', 'Starbucks'),
('Oliy', 'Espresso Royal'),
('Oliy', 'Starbucks'),
('Orton', 'Aroma'),
('Orton', 'Hammerhead'),
('Patin', 'Aroma'),
('Pearl', 'Brewlab'),
('Pearl', 'etc.'),
('Pietra', 'Caffe Bene'),
('Rafa', 'Aroma'),
('Ritchie', 'Caffe Bene'),
('Rosemarie', 'Aroma'),
('Sayre', 'Aroma'),
('Sayre', 'Brewlab'),
('Sayre', 'etc.'),
('Seth', 'Brewlab'),
('Sharleen', 'Hammerhead'),
('Spense', 'Caffe Bene'),
('Stefan', 'Aroma'),
('Stefan', 'Espresso Royal'),
('Stefan', 'Starbucks'),
('Thomas', 'Aroma'),
('Thomas', 'Brewlab'),
('Tim', 'Starbucks'),
('Torey', 'Aroma'),
('Torey', 'Espresso Royal'),
('Tyson Ulysses', 'Brewlab'),
('Tyson Ulysses', 'Espresso Royal'),
('Urbano', 'etc.'),
('Vally', 'Hammerhead'),
('Vally', 'Starbucks'),
('Vanya', 'Hammerhead'),
('Virgil', 'Starbucks'),
('Wain', 'Aroma'),
('Wain', 'Hammerhead'),
('Welsh', 'Aroma'),
('Welsh', 'Hammerhead'),
('Wright', 'Brewlab'),
('Wright', 'Espresso Royal');

-- --------------------------------------------------------

--
-- Table structure for table `Likes`
--

CREATE TABLE `Likes` (
  `customer` varchar(20) NOT NULL,
  `drink` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Likes`
--

INSERT INTO `Likes` (`customer`, `drink`) VALUES
('', 'Espresso'),
('', 'Latte'),
('', 'White Mocha'),
('Abbe', 'Latte'),
('Alfonse', 'White Mocha'),
('Alina', 'Mocha'),
('Alisa', 'Mocha'),
('Alvina', 'Latte'),
('Ariana', 'Cappuccino'),
('Ariana', 'Latte'),
('Armin', 'Espresso'),
('Averil', 'Mocha'),
('Averil', 'White Mocha'),
('Barney', 'Latte'),
('Benedetto', 'Espresso'),
('Benjy', 'Cappuccino'),
('Bob', 'Cappuccino'),
('Cathlene', 'Cappuccino'),
('Cathlene', 'Latte'),
('Clarey', 'Espresso'),
('Clarey', 'Latte'),
('Danit', 'Espresso'),
('Darleen', 'Mocha'),
('Davon', 'Mocha'),
('Dorian', 'Cappuccino'),
('Dorian', 'White Mocha'),
('Ernaline', 'Espresso'),
('Ernesta', 'White Mocha'),
('Felix', 'Latte'),
('Fionna', 'Mocha'),
('Garvy', 'Cappuccino'),
('Garvy', 'Mocha'),
('Garvy', 'White Mocha'),
('Geno', 'Espresso'),
('Geno', 'Latte'),
('Georgeta', 'Espresso'),
('Hanna', 'Mocha'),
('Hansiain', 'Cappuccino'),
('Henriette', 'Mocha'),
('Herculie', 'White Mocha'),
('Isabelle', 'White Mocha'),
('Issy', 'White Mocha'),
('Jake', 'Latte'),
('Jeremias', 'Cappuccino'),
('Jocelyn', 'White Mocha'),
('Johann', 'Mocha'),
('Khalil', 'White Mocha'),
('Lee', 'Cappuccino'),
('Lee', 'Mocha'),
('Lilyan', 'White Mocha'),
('Maggy', 'Espresso'),
('Maggy', 'White Mocha'),
('Marje', 'Cappuccino'),
('Marje', 'White Mocha'),
('Maryjo', 'Latte'),
('Megen', 'Mocha'),
('Mellicent', 'Cappuccino'),
('Mellicent', 'Mocha'),
('Mellicent', 'White Mocha'),
('Mozes', 'Latte'),
('Oliy', 'Cappuccino'),
('Oliy', 'Mocha'),
('Orton', 'White Mocha'),
('Patin', 'White Mocha'),
('Pearl', 'Espresso'),
('Rafa', 'Cappuccino'),
('Rafa', 'White Mocha'),
('Rahel', 'Mocha'),
('Reece', 'Latte'),
('Reece', 'White Mocha'),
('Ritchie', 'Cappuccino'),
('Rodolphe', 'Latte'),
('Rosemarie', 'Cappuccino'),
('Rosemarie', 'Espresso'),
('Sayre', 'Latte'),
('Shannah', 'Cappuccino'),
('Shannah', 'Mocha'),
('Sharleen', 'Cappuccino'),
('Spense', 'Cappuccino'),
('Thaddus', 'Espresso'),
('Thomas', 'Cappuccino'),
('Tim', 'White Mocha'),
('Torey', 'White Mocha'),
('Tyson Ulysses', 'Cappuccino'),
('Urbano', 'Cappuccino'),
('Vally', 'Espresso'),
('Vanya', 'Cappuccino'),
('Vanya', 'Latte'),
('Virgil', 'Latte'),
('Wain', 'Espresso'),
('Wain', 'Mocha');

-- --------------------------------------------------------

--
-- Table structure for table `Sells`
--

CREATE TABLE `Sells` (
  `cafe` varchar(20) DEFAULT NULL,
  `drink` varchar(20) DEFAULT NULL,
  `price` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Sells`
--

INSERT INTO `Sells` (`cafe`, `drink`, `price`) VALUES
('Aroma', 'Cappuccino', 8.06),
('Aroma', 'Espresso', 5.97),
('Aroma', 'Latte', 4.12),
('Aroma', 'Mocha', 8.28),
('Aroma', 'White Mocha', 4.59),
('Brewlab', 'Cappuccino', 7.46),
('Brewlab', 'Espresso', 7.24),
('Brewlab', 'Latte', 7.75),
('Brewlab', 'Mocha', 2.38),
('Brewlab', 'White Mocha', 2.96),
('Caffe Bene', 'Cappuccino', 2.33),
('Caffe Bene', 'Espresso', 3.76),
('Caffe Bene', 'Latte', 8.46),
('Caffe Bene', 'Mocha', 7.11),
('Caffe Bene', 'White Mocha', 7.05),
('Espresso Royal', 'Cappuccino', 4.05),
('Espresso Royal', 'Espresso', 5.74),
('Espresso Royal', 'Latte', 6.46),
('Espresso Royal', 'Mocha', 7.54),
('Espresso Royal', 'White Mocha', 4.25),
('etc.', 'Cappuccino', 4.57),
('etc.', 'Espresso', 3.64),
('etc.', 'Latte', 6.49),
('etc.', 'Mocha', 3.66),
('etc.', 'White Mocha', 1.99),
('Hammerhead', 'Cappuccino', 6.46),
('Hammerhead', 'Espresso', 3.39),
('Hammerhead', 'Latte', 2.21),
('Hammerhead', 'Mocha', 6.03),
('Hammerhead', 'White Mocha', 9.38),
('Starbucks', 'Cappuccino', 6.53),
('Starbucks', 'Espresso', 2.66),
('Starbucks', 'Latte', 9.93),
('Starbucks', 'Mocha', 8.69),
('Starbucks', 'White Mocha', 4.94),
(NULL, 'Milk', 2),
(NULL, 'Water', 1),
(NULL, NULL, NULL),
(NULL, NULL, NULL),
(NULL, 'Hot Iced Tea Coffee', 100),
(NULL, 'Hot Iced Tea Coffee', 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Cafe`
--
ALTER TABLE `Cafe`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `Drinks`
--
ALTER TABLE `Drinks`
  ADD PRIMARY KEY (`name`,`manf`);

--
-- Indexes for table `Frequents`
--
ALTER TABLE `Frequents`
  ADD PRIMARY KEY (`customer`,`cafe`);

--
-- Indexes for table `Likes`
--
ALTER TABLE `Likes`
  ADD PRIMARY KEY (`customer`,`drink`);