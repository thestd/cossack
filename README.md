TODO:
- ~~MANAGE NGINX~~
  - ~~Start / Stop / Restart~~
  - ~~Status / Enabled Hosts~~ 
- MANAGE SUPERVISOR
- FIREWALL (UFW)
  - allow / disable
  - show status (open ports)
- PROJECT DEPLOY
- MIGRATION RUN
- EXEC COMMAND
- ADDED DATABASE FOR SAVE USER DATA
- ADDED WEBHOOKS


create database penguins;
create user penguins_ninja with password 'ninja135';
alter role penguins_ninja set client_encoding to 'utf8';
alter role penguins_ninja set default_transaction_isolation to 'read committed';
alter role penguins_ninja set timezone to 'UTC';
grant all privileges on database penguins to penguins_ninja;