# Data Dump and Quality Checks using Docker

This repository provides a Dockerized solution to perform data dumping from a SQL Server database and conducting data quality checks. The dumped data is saved as an Excel file, and the data quality check report is generated as a text file.

## Prerequisites

Before you begin, ensure you have the following installed:

1. [Docker](https://docs.docker.com/get-docker/): Install Docker for your operating system.

## Usage

Follow the steps below to run the data dump and quality checks using Docker:

1. **Clone the Repository:**
```bash
git clone https://github.com/Karalius/barbora-task.git
cd barbora-task
```

2. **Configuration:**
Update the necessary configuration in the `.env` file. Provide the appropriate values for connecting to your SQL Server database.

3. **Running the Services:**
Run the following command to start the services defined in the `docker-compose.yml` file:

```bash
docker-compose up
```

This will start the data dump and data quality check processes inside separate Docker containers.

4. **Results:**
- The dumped data will be saved as an Excel file named `data_dump.xlsx` in the `output` directory.
- The data quality check report will be saved as a text file named `data_quality_report.txt` in the `output` directory.

## Customization

You can customize this repository according to your needs:

- Modify the SQL query in the `dump_data.py` script to extract specific data from your SQL Server database.
- Adjust the data quality checks in the `data_quality_checks.py` script to match the requirements of your data.
- Customize the Docker images and services in the `docker-compose.yml` file as necessary.

## Directory Structure

- `docker-compose.yml`: Defines the Docker services to run the data dump and data quality check processes.
- `.env`: Environment variables configuration file.
- `app_code`: Directory containing Python scripts for data dumping and quality checks.
- `output`: Directory to store the dumped data and data quality check report.
- `README.md`: This file, providing instructions and information about the repository.

## Notes

- This repository provides a basic example to get you started with data dumping and quality checks using Docker.
- Ensure that you have the necessary permissions and configurations to connect to your SQL Server database.
- Docker containers can consume disk space. Use `docker container prune` to clean up old containers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
