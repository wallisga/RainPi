#!/bin/sh
cd ../server
sqlite3 rainfall.db <<EOF
create table data (timestamp INT PRIMARY KEY NOT NULL, amount REAL NOT NULL, pi_id INT NOT NULL);
insert into data values ($(date +%s), 0.0, 000);
create table auth (token VARCHAR(24) PRIMARY KEY NOT NULL, access)
EOF
echo $(python3 -c 'from auth import create_token; print(create_token("admin"))')
python3 -m venv rainpienv
chmod 700 rainpienv/bin/activate