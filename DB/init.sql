CREATE DATABASE  IF NOT EXISTS `music_ai_2`;
music_ai_2;
USE `music_ai_2`; 

CREATE TABLE `song` (
  `song_id` bigint NOT NULL,
  `song_name` varchar(225) NOT NULL,
  `song_lyrics` text,
  PRIMARY KEY (`song_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `album` (
  `album_id` bigint NOT NULL,
  `album_years` varchar(20) NOT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `artist` (
  `artist_id` bigint NOT NULL,
  `artist_name` varchar(200) NOT NULL,
  PRIMARY KEY (`artist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `genre` (
  `genre_id` bigint NOT NULL,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `karaoke` (
  `karaoke_id` bigint NOT NULL AUTO_INCREMENT,
  `karaoke_name` varchar(30) DEFAULT NULL,
  `karaoke_store` varchar(30) NOT NULL,
  `karaoke_location` varchar(300) NOT NULL,
  `karaoke_lat` double NOT NULL,
  `karaoke_long` double NOT NULL,
  PRIMARY KEY (`karaoke_id`)
) ENGINE=InnoDB AUTO_INCREMENT=572 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `music` (
  `song_id` bigint NOT NULL,
  `artist_id` bigint NOT NULL,
  `album_id` bigint NOT NULL,
  `genre_id` bigint NOT NULL,
  PRIMARY KEY (`song_id`,`artist_id`,`album_id`,`genre_id`),
  KEY `artist_id` (`artist_id`),
  KEY `album_id` (`album_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `music_ibfk_1` FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`) ON DELETE CASCADE,
  CONSTRAINT `music_ibfk_2` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`artist_id`) ON DELETE CASCADE,
  CONSTRAINT `music_ibfk_3` FOREIGN KEY (`album_id`) REFERENCES `album` (`album_id`) ON DELETE CASCADE,
  CONSTRAINT `music_ibfk_4` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`genre_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
