CREATE TABLE IF NOT EXISTS menu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS recipes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT NOT NULL,
title TEXT NOT NULL,
category TEXT NOT NULL,
cooking_time INTEGER NOT NULL,
ingredients TEXT NOT NULL,
instruction TEXT NOT NULL,
date INTEGER NOT NULL
);