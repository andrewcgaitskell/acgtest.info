#!/bin/bash
cp /etc/postgresql/10/main/pg_hba.conf /etc/postgresql/10/main/pg_hba_backup_20201124.conf
cp /etc/postgresql/10/main/postgresql.conf /etc/postgresql/10/main/postgresql_backup_20201124.conf

sed -i 's+host    all             all             127.0.0.1/32            md5+host    all             all             0.0.0.0/0            md5+' /etc/postgresql/10/main/pg_hba.conf
sed -i 's+#listen_addresses = '\''localhost'\''         # what IP address(es) to listen on;+listen_addresses = '\''*'\''         # what IP address(es) to listen on;+' /etc/postgresql/10/main/postgresql.conf

service postgresql restart
