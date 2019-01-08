-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Янв 08 2019 г., 15:39
-- Версия сервера: 5.6.41
-- Версия PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `python`
--

-- --------------------------------------------------------

--
-- Структура таблицы `transfers`
--

CREATE TABLE `transfers` (
  `id` int(255) NOT NULL,
  `method` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `account` varchar(255) DEFAULT NULL,
  `amt` int(11) DEFAULT NULL,
  `ccy` varchar(10) DEFAULT NULL,
  `create_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `allowed` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `transfers`
--

INSERT INTO `transfers` (`id`, `method`, `date`, `account`, `amt`, `ccy`, `create_at`, `update_at`, `allowed`) VALUES
(28, 'deposit', '2019-01-06', 'bob', 10, 'EUR', '2019-01-06 19:44:43', '2019-01-04 19:44:43', 0),
(30, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 08:49:21', '2019-01-07 08:49:21', 0),
(31, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 08:56:32', '2019-01-07 08:56:32', 0),
(32, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 09:00:36', '2019-01-07 09:00:36', 0),
(33, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 09:50:52', '2019-01-07 09:50:52', 0),
(34, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 09:52:25', '2019-01-07 09:52:25', 0),
(35, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 09:53:11', '2019-01-07 09:53:11', 0),
(36, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 09:53:18', '2019-01-07 09:53:18', 0),
(37, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 09:53:41', '2019-01-07 09:53:41', 0),
(38, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 10:10:22', '2019-01-07 10:10:22', 0),
(39, 'deposit', '2019-01-07', 'bob', 10, 'EUR', '2019-01-07 10:10:23', '2019-01-07 10:10:23', 0),
(40, 'deposit', '2018-10-09', 'bob', 10, 'EUR', '2019-01-08 11:24:32', '2019-01-08 11:24:32', 0),
(41, 'deposit', '2018-10-09', 'bob', 10, 'EUR', '2019-01-08 11:24:40', '2019-01-08 11:24:40', 0),
(42, 'deposit', '2018-10-09', 'bob', 10, 'EUR', '2019-01-08 11:24:42', '2019-01-08 11:24:42', 0),
(43, 'deposit', '2018-10-09', 'bob', 10, 'EUR', '2019-01-08 11:30:52', '2019-01-08 11:30:52', 0),
(44, 'transfer', '2018-10-09', 'bob', 100, 'GBP', '2019-01-08 12:14:54', '2019-01-08 12:14:54', 0),
(45, 'transfer', '2018-10-09', 'alice', 100, 'GBP', '2019-01-08 12:14:54', '2019-01-08 12:14:54', 0),
(46, 'withdrawal', '2018-10-09', 'alice', 10, 'EUR', '2019-01-08 12:20:09', '2019-01-08 12:20:09', 0),
(47, 'withdrawal', '2018-10-09', 'alice', 10, 'EUR', '2019-01-08 12:27:18', '2019-01-08 12:27:18', 0);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `transfers`
--
ALTER TABLE `transfers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `transfers`
--
ALTER TABLE `transfers`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
