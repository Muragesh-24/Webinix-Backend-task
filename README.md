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

├── callbacks/ # logic functions
│ └── callfunc.py
│
├── container/ # Docker-related files
│ ├── Dockerfile # FastAPI image build
│ ├── Dockerfile.nginx # Nginx reverse proxy
│ ├── nginx.config # Nginx config
│ └── init.sql # DB initialization
│
├── models/ # SQLAlchemy models
│ └── task.py
│
├── routes/ # API route definitions
│ └── routes.py
│
├── scripts/ # Utilities like DB connection
│ └── db.py
│
├── index.html # Test UI for the API
├── docker-compose.yml # Run everything together
├── requirements.txt # Python dependencies
├── schemas.py # Pydantic schemas (input/output validation)
├── server.py # Main FastAPI app entry
├── wait-for-db.sh # Wait for DB before starting FastAPI
└── README.md # This file


---

##  How to Run (Locally)

### Option 1:  Using Docker (Recommended)

####  Prerequisites:
- Docker + Docker Compose installed

####  Run the app:

```bash
docker-compose up --build

 After running:
FastAPI will be available at: http://localhost:8041



HTML UI (if served): http://localhost/index.html (or open directly from file)

Option 2:  Run Without Docker (Manual Setup)
1. Set up PostgreSQL database
You need a local PostgreSQL instance with:

database: mydb

user: user

password: password

You can adjust values in scripts/db.py.

pip install -r requirements.txt
3. Run FastAPI

uvicorn server:app --reload --port 8041

API Endpoints
Method	Endpoint	Description
POST	/tasks	Create new task
GET	/tasks	Get all tasks
POST	/tasks/filter	Filter by status
GET	/tasks/{id}	Get task by ID
PUT	/tasks/{id}	Update task by ID
DELETE	/tasks/{id}	Delete task by ID

🧪 Testing with HTML UI
Open index.html in your browser. It includes:

Task creation

Task filtering

Get, update, delete by ID

JSON results

For production use, the app's efficiency and security can be significantly improved. We can add caching in the frontend to reduce unnecessary API calls and make the user experience faster. Implementing authentication (like JWT) will help verify users and protect your APIs.

To improve performance at scale, you can also distribute the load using multiple backend instances behind a load balancer (like Nginx).