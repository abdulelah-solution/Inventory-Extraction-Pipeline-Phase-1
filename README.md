🏭 Inventory Extraction Pipeline (Phase 1)
This project is an automated system designed to extract inventory reports from a SQL Server database using Python and SQLAlchemy. The system is built to be flexible, secure, and organized according to Data Engineering best practices.

---

🌟 Key Features
    ◉ Decoupled Architecture: Clean separation of concerns between configuration (config.py), helper functions (utils.py), and the execution logic (extract.py).

    ◉ Secure Authentication: Robust management of sensitive credentials via .env files to prevent credential leaks.

    ◉ Smart WSL Connectivity: Automatic detection of the Host IP address when running within a Windows Subsystem for Linux (WSL) environment.

    ◉ Professional Logging: A comprehensive tracking system for operations and errors with UTF-8 support (ideal for multilingual data).

    ◉ Data Validation: Pre-execution checks to ensure all required environment variables and database connections are present.  

---

🏗️ Project Structure
├── config.py          # Configuration and Logging management
├── utils.py           # Utility functions (e.g., WSL Host IP detection)
├── extract.py         # Main script for data extraction and export
├── requirements.txt   # Required Python dependencies
├── .env.example       # Template for sensitive environment variables
└── .gitignore         # Rules to exclude unnecessary or sensitive files

---

🛠️ Getting Started
1. Prerequisites
    ◉ Python 3.10+ installed.
    ◉ ODBC Driver 18 for SQL Server installed.
    ◉ Access to a SQL Server instance containing Sales.Products and Sales.Inventory tables.

2. Installation
    1. Clone the repository:
    git clone https://github.com/yourusername/inventory-extraction.git
    cd inventory-extraction

    2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # For Linux/WSL
    # or: venv\Scripts\activate (For Windows)

    3. Install dependencies:
    pip install -r requirements.txt

3. Configuration
Create a .env file based on the .env.example template and add your specific database credentials.

---

🚀 Usage
To execute the extraction process and generate the Excel report, run:
python extract.py
The generated report will be saved in the output/ directory, and operation logs can be found in data/app.log.

---

🎯 Future Roadmap (Phase 2)
    ◉ [ ] Containerize the entire application using Docker.

    ◉ [ ] Implement Unit Tests to ensure data quality and pipeline integrity.

    ◉ [ ] Expand support for Cloud Databases (e.g., PostgreSQL on AWS/Azure).

    ◉ [ ] Implement Workflow Orchestration (Scheduling) using Apache Airflow or Cron Jobs.

---

🤝 Contributing
Contributions are welcome! Feel free to open an Issue or submit a Pull Request.
