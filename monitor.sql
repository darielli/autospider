drop table if exists `pictures`;
drop table if exists `files`;
drop table if exists `posts`;
create table `posts` (
    `post_id` bigint(20) NOT NULL AUTO_INCREMENT,
    `publish_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `web` varchar(256) NOT NULL,
    `detail` varchar(256) NOT NULL,
    `title` varchar(1024) NOT NULL,
    `content` text NOT NULL,
    PRIMARY KEY(`post_id`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



create table `files` (
    `file_id` bigint(20) NOT NULL AUTO_INCREMENT,
    `file_name` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `url` varchar(256) NOT NULL,
    `post_id` bigint(20) NOT NULL,
    PRIMARY KEY(`file_id`),
    FOREIGN KEY (`post_id`) REFERENCES posts(`post_id`)
)ENGINE=InnoDB AUTO_INCREMENT=200001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


create table `pictures` (
    `picture_id` bigint(20) NOT NULL AUTO_INCREMENT,
    `picture_name` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `url` varchar(256) NOT NULL,
    `post_id` bigint(20) NOT NULL,
    PRIMARY KEY(`picture_id`),
    FOREIGN KEY (`post_id`) REFERENCES posts(`post_id`)
)ENGINE=InnoDB AUTO_INCREMENT=500001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;