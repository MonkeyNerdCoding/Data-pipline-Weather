
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

### 7. API 
1. Change the api key in venv

### 8. Step to open Unbutu and run the project (This project must be run on Unbutu (Linux))
- Information : Whold project goona in "\\wsl$\"
1. Step 1 : 
<img width="1335" height="801" alt="image" src="https://github.com/user-attachments/assets/2bc52ad9-1995-4f22-a0ae-e1dbfc91645a" />

2. Step 2 : 
<img width="1280" height="500" alt="image" src="https://github.com/user-attachments/assets/ecb684ab-f822-4426-8373-787275d35120" />

3. Step 3 :
<img width="711" height="178" alt="image" src="https://github.com/user-attachments/assets/dac986eb-5e9d-4837-b88a-89ed4a5dc8b8" />

4. Step 4 :
- Choose Open Folder -> Ok

5. Step 5 :
```bash
docker-compose up
```
6. Step 6 :
- If you want to go back normal enviroment : 
<img width="1281" height="796" alt="image" src="https://github.com/user-attachments/assets/bc1d80d9-57bf-4fd0-833b-371ac25b773b" />
