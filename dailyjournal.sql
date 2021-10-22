CREATE TABLE `Journal_Entry` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`subject`	TEXT NOT NULL,
	`date`	TEXT NOT NULL,
    `feeling`	TEXT NOT NULL,
	`moods_id`	INTEGER NOT NULL,
    `tags_id`	INTEGER NOT NULL,
	`time_spent`	TEXT NOT NULL,
    FOREIGN KEY(`moods_id`) REFERENCES `Mood`(`id`),
	FOREIGN KEY(`tags_id`) REFERENCES `Tag`(`id`)
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `type`    TEXT NOT NULL
);

CREATE TABLE `Tag` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`type`  TEXT NOT NULL
);



INSERT INTO `Journal_Entry` VALUES (null, 'Coding', "11/25/21", 'happy', 1, 2, "2 Hours");
INSERT INTO `Journal_Entry` VALUES (null, 'JavaScript', "11/26/21",  'Sad', 1, 2, "3 Hours");

INSERT INTO `Mood` VALUES (null, "Happy");
INSERT INTO `Mood` VALUES (null, "Sad");




INSERT INTO `Tag` VALUES (null, "JS");
INSERT INTO `Tag` VALUES (null, "React");
