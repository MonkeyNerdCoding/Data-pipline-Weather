## Data Pipeline Weather Instruction

### 1. Create virtual environment
```bash
python3 -m venv .venv
````

### 2. Activate virtual environment

```bash
source .venv/bin/activate
```

### 3. Access PostgreSQL database inside Docker

```bash
docker-compose exec db psql -U db_user -d db
```

### 4. Run Docker containers

```bash
sudo docker-compose up
```

### 5. Fix Permission Denied
```bash
ls -l [copy path of the folder]

sudo chgrp -R $USER [copy path of the folder]

sudo chmod 770 [copy path of the folder]

```

### 6. Run Dbt
```bash
docker-compose up dbt 

docker-compose down dbt
```
