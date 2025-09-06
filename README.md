## Data Pipeline Weather Instruction

````markdown
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

