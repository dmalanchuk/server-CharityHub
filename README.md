# CharityHub

## About the Project

CharityHub is an open-source platform that unites charitable foundations across Ukraine.
Here, users can discover organizations that:

* Support the Armed Forces of Ukraine
* Organize blood donation campaigns
* Participate in various humanitarian initiatives



## Technologies Used

### Backend (Server-side)
* **Python with FastAPI** — high-performance asynchronous web framework
* **PostgreSQL** — relational database
* **SQLAlchemy** + asyncpg — ORM and asynchronous DB communication
* **Alembic** — for database migrations

The backend is fully asynchronous, which improves performance, scalability, 
and responsiveness under high load.

## Running app

command: `uvicorn src.main:app --reload`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Docker

First, pull the latest version of the image from Docker Hub:
`docker pull dmalanchuk/server-charityhub-server-fastapi:latest`

Run the container: `docker run -p 8000:8000 dmalanchuk/server-charityhub-server-fastapi:latest`
