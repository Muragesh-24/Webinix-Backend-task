# Webinix-Backend-task
#  FastAPI Task Manager

A simple **Task Manager** built with FastAPI and PostgreSQL, allowing you to:
- Create tasks
- Read all tasks
- Filter completed/incomplete tasks
- Update tasks
- Delete tasks

Also includes a clean HTML UI for testing all routes!

---

##  Tech Stack

| Tool           | Purpose                                |
|----------------|----------------------------------------|
| FastAPI        | Backend web framework                  |
| SQLAlchemy     | ORM for database access                |
| PostgreSQL     | Database                               |
| Docker         | Containerize app and DB                |
| Nginx          | Reverse proxy server                   |
| HTML + JS      | Frontend testing interface (`index.html`) |

---

##  Folder Structure

├── callbacks/ # logic functions<br>
│ └── callfunc.py<br>
│
├── container/ # Docker-related files<br>
│ ├── Dockerfile # FastAPI image build<br>
│ ├── Dockerfile.nginx # Nginx reverse proxy<br>
│ ├── nginx.config # Nginx config<br>
│ └── init.sql # DB initialization<br>
│
├── models/ # SQLAlchemy models<br>
│ └── task.py<br>
│
├── routes/ # API route definitions<br>
│ └── routes.py<br>
│
├── scripts/ # Utilities like DB connection<br>
│ └── db.py<br>
│
├── index.html # Test UI for the API<br>
├── docker-compose.yml # Run everything together<br>
├── requirements.txt # Python dependencies<br>
├── schemas.py # Pydantic schemas (input/output validation)<br>
├── server.py # Main FastAPI app entry<br>
├── wait-for-db.sh # Wait for DB before starting FastAPI<br>
└── README.md # This file<br>


---

##  How to Run (Locally)

### Option 1:  Using Docker (Recommended)

####  Prerequisites:
- Docker + Docker Compose installed

####  Run the app:

```bash
docker-compose up --build
```
 After running:
FastAPI will be available at: http://localhost:8041



HTML UI (if served): http://localhost/index.html (or open directly from file)

### Option 2:  Run Without Docker (Manual Setup)
1. Set up PostgreSQL database
You need a local PostgreSQL instance with:

database: mydb

user: user

password: password

You can adjust values in scripts/db.py.

pip install -r requirements.txt<br>
3. Run FastAPI

uvicorn server:app --reload --port 8041

API Endpoints<br>
Method	Endpoint	Description<br>
POST	/tasks	Create new task<br>
GET	/tasks	Get all tasks<br>
POST	/tasks/filter	Filter by status<br>
GET	/tasks/{id}	Get task by ID<br>
PUT	/tasks/{id}	Update task by ID<br>
DELETE	/tasks/{id}	Delete task by ID<br>

🧪 Testing with HTML UI
Open index.html in your browser. It includes:<br>

Task creation<br>

Task filtering<br>

Get, update, delete by ID<br>

JSON results<br>

For production use, the app's efficiency and security can be significantly improved. We can add caching in the frontend to reduce unnecessary API calls and make the user experience faster. Implementing authentication (like JWT) will help verify users and protect your APIs.<br>

To improve performance at scale, you can also distribute the load using multiple backend instances behind a load balancer (like Nginx).
