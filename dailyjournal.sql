CREATE TABLE `Journal_Entry` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL
);

CREATE TABLE `Mood` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE `Tag` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`mood_id` INTEGER NOT NULL,
	`journal_entry_id` INTEGER,
	FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`),
	FOREIGN KEY(`journal_entry_id`) REFERENCES `journal_entry`(`id`)
);



INSERT INTO `Journal_Entry` VALUES (null, 'Nashville North', "64 Washington Heights");
INSERT INTO `Journal_Entry` VALUES (null, 'Nashville South', "101 Penn Ave");

INSERT INTO `Mood` VALUES (null, "Mo Silvera", "201 Created St", "mo@silvera.com", "password");
INSERT INTO `Mood` VALUES (null, "Bryan Nilsen", "500 Internal Error Blvd", "bryan@nilsen.com", "password");
INSERT INTO `Mood` VALUES (null, "Jenna Solis", "301 Redirect Ave", "jenna@solis.com", "password");
INSERT INTO `Mood` VALUES (null, "Emily Lemmon", "454 Mulberry Way", "emily@lemmon.com", "password");



INSERT INTO `Tag` VALUES (null, "Snickers", "Recreation", "Dalmation", 4, 1);
INSERT INTO `Tag` VALUES (null, "Jax", "Treatment", "Beagle", 1, 1);
INSERT INTO `Tag` VALUES (null, "Falafel", "Treatment", "Siamese", 4, 2);
INSERT INTO `Tag` VALUES (null, "Doodles", "Kennel", "Poodle", 3, 1);
INSERT INTO `Tag` VALUES (null, "Daps", "Kennel", "Boxer", 2, 2);