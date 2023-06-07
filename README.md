## Build & Run
```sh
#ホスト側の.dockervenvにpoetry installされたのが保存される
docker-compose run --entrypoint "poetry install --no-root" app
docker-compose up
```
Run browser to http://localhost:8000/docs

```sh
└─$ docker ps
#CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS         PORTS                                  NAMES
#de67d0352262   fastapi_scaffold_app   "poetry run uvicorn …"   7 minutes ago   Up 7 minutes   127.0.0.1:8000->8000/tcp               fastapi_scaffold-app-1
#c7730ed6f5c8   mysql:8.0              "docker-entrypoint.s…"   7 minutes ago   Up 7 minutes   33060/tcp, 127.0.0.1:33306->3306/tcp   fastapi_scaffold-db-1
```

## Migrate DB
```sh
# api モジュールの migrate_db スクリプトを実行する
docker-compose exec app poetry run python -m api.migrate_db
docker-compose exec db mysql demo

#mysql> SHOW TABLES;
#+----------------+
#| Tables_in_demo |
#+----------------+
#| dones          |
#| tasks          |
#+----------------+
#2 rows in set (0.01 sec)
#
#mysql> DESCRIBE tasks;
#+-------+---------------+------+-----+---------+----------------+
#| Field | Type          | Null | Key | Default | Extra          |
#+-------+---------------+------+-----+---------+----------------+
#| id    | int           | NO   | PRI | NULL    | auto_increment |
#| title | varchar(1024) | YES  |     | NULL    |                |
#+-------+---------------+------+-----+---------+----------------+
#2 rows in set (0.05 sec)
#
#mysql> DESCRIBE dones;
#+-------+------+------+-----+---------+-------+
#| Field | Type | Null | Key | Default | Extra |
#+-------+------+------+-----+---------+-------+
#| id    | int  | NO   | PRI | NULL    |       |
#+-------+------+------+-----+---------+-------+
#1 row in set (0.00 sec)
```
```sh
docker volume ls
#DRIVER    VOLUME NAME
#local     fastapi_scaffold_mysql_data
```

## Test
```sh
docker-compose run --entrypoint "poetry run pytest" app
```
## Remove containers
```sh
docker-compose down
```

## Remove Build Cache
```sh
docker system df
docker rmi fastapi_scaffold_app && docker builder prune
```
