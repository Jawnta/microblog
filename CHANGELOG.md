# Changelog for microblog

## [0.3.0] [Release]
### Added
- feat(ansible): add 'docker_install' role to loadbalancer.yml for enhanced functionality.
- feat(ansible/loadbalancer): check for existing SSL certificate before obtaining a new one.
- style(ansible/loadbalancer): remove unnecessary space in proxy_pass directive for consistency.
- feat(ansible/security_groups): add 'EXPORTER' rule to security groups for monitoring support.
- feat(monitoring/main.yml): switch Prometheus config to templating for dynamic content.
- feat(monitoring/main.yml): add rules config file for enhanced monitoring.
- feat(monitoring/main.yml): introduce Grafana settings via grafana.ini template.
- feat(monitoring/main.yml): add multiple Grafana dashboards for better metrics visualization.
- refactor(monitoring/main.yml): change docker-compose command to use sudo for better permissions management.
- refactor(monitoring/main.yml): update Grafana data source and dashboard URLs for consistency.
- feat(monitoring/main.yml): implement a pause before starting Grafana to ensure service readiness.
- feat(monitoring): add alertmanager.yml template for webhook integration.
- feat(monitoring): update Prometheus and Grafana images in docker-compose.yml.
- feat(monitoring): mount grafana.ini in Grafana service for custom configuration.
- feat(monitoring): introduce prometheus.yml.j2 template with dynamic scrape configs.
- feat(dashboards): Added json files for dashboard, nginx, flask, and node exporter.

## [0.2.3]
### Fixed
- Update Flask-Login to version 0.6.3 in `prod.txt`.
- Update Flask-WTF to version 1.2.1 in `prod.txt`.
- Remove default `sshd_config` and copy new SSHD configuration file in Ansible.

### Added
- Add workflow to run security tests using Bandit, Trivy, and Dockle in `.github/workflows/cs.yml`.
- Set `DOCKER_CONTENT_TRUST=1` for content trust, and upgrade `libcrypto` in `docker/Dockerfile_prod`.
- Add new targets for scanning Docker image and repository in `Makefile`.
- Add 'bandit' target to `Makefile` for running Bandit for security code analysis.
- Add 'bandit' to test dependencies in `requirements/test.txt`.

### Updated
- Update test_avatar to use secure email hashing with hashlib in `models`.
- Add reference to new security tests workflow in `.github/workflows/cd.yml`.
- Bump Flask to version 2.3.2 and Werkzeug to version 2.3.8 in `requirements/prod.txt`.

### Refactored
- Replace md5 with sha256 for Gravatar URL generation in `models.py` to enhance security.


## [0.2.2] [Release]
### Refactored
- Removed commented verification tasks in `ansible/roles/appserver/tasks/main.yml` for clarity.

### Style
- Corrected typo in the Sign In header in `app/templates/auth/login.html` for better readability.

### Tests
- Added `test_version.py` to validate the version route response in `tests/unit/main/routes`.

## [0.2.1]
### Updated
- Added `DATABASE_HOST` configuration to `ansible/roles/appserver/tasks/main.yml` to use `database.microbloggu.me`.
- Added 'database' group with `database.microbloggu.me` as a host in `ansible/hosts`.
- Replaced direct database host reference with `DATABASE_HOST` variable in `ansible/roles/appserver/tasks`.
- Installed Docker SDK for Python (docker) using pip3 in `ansible/roles/docker_install/tasks`.
- Added task to ensure 'A' records for database in `create_instance.yml`.


## [0.2.0]

### Added
- Ansible playbook execution for app server setup in the deployment workflow (`cd.yml`).
- Dynamic docker image tagging for deployment (`cd.yml`).
- New Ansible playbooks for appserver, database, and load balancer setup.
- Docker installation and Nginx configuration roles in Ansible.
- DNS record setup for enhanced instance provisioning in Ansible.
- Version endpoint in `routes.py` to expose current application version.
- Additional dependencies for deployment configuration in `requirements.txt`.

### Changed
- Service port mapping in `docker-compose.yml` to align with Nginx setup.
- Integration of application version as a build argument in `Dockerfile_prod`.

### Fixed
- SSH command with correct key path in `Makefile`.

### Refactored
- Deployment workflow to include SSH setup and Ansible (`cd.yml`).
- Group variables with specific deployment details in Ansible.
- Database host configuration to allow dynamic setup in `boot.sh`.

## Version 0.1.5 [Release]

### Feature

- **routes.py:**
  - Update routes to use user's `followed_posts` instead of all posts to display only relevant content.
  
- **models.py:**
  - Add `followers` table for many-to-many relationship between users, allowing users to follow and unfollow each other.
  - Implement `follow`, `unfollow`, and `followed_posts` methods in User model to manage user relationships.

### Style
- **user.html:**
  - Improve code readability and formatting in user.html template.

### Refactor
- **followers.py:**
  - Add Alembic migration for the `followers` table.

### Test
- **test_followers.py:**
  - Add unit tests for `follow`, `unfollow`, and `followed_posts` methods in the User model.


## Version 0.1.4

### Feature

- **.gitattributes:**
  - Added .gitattributes file with LF line endings for boot.sh, ensuring consistent line endings across different platforms.

- **docker-compose.yml:**
  - Introduced DATABASE_URL environment variable in service for dynamic database connection configuration.

### Refactor

- **config.py:**
  - Removed hardcoded SQLALCHEMY_DATABASE_URI in ProdConfig for enhanced security.

## Version 0.1.3

### Chore

- **boot.sh:**
  - Improved readability and added comments for better understanding of the script.

- **docker-compose.yml:**
  - Updated MySQL image to `mysql/mysql-server:5.7`.
  - Updated volume path for MySQL initialization script.

## Version 0.1.2

### Chore
- **config.py:** Added `SQLALCHEMY_DATABASE_URI` for production configuration.
- **boot.sh:** Added sleep and improved upgrade command for a more robust boot script.

### Feature
- **docker-compose.yml:** Updated MySQL ports and volumes configuration for better compatibility.
- **init.sql:** Added initialization SQL script for database and user

## Version 0.1.1

### Added
- **Docker Compose Setup**: Introduced `docker-compose.yml` to orchestrate the application, database, and testing containers. This enhancement improves local development and CI/CD processes by simplifying multi-container setups.
- **Dockerfile for Testing**: Added `Dockerfile_test` in the `docker` directory. This Dockerfile creates a dedicated environment for testing, ensuring tests run in an isolated and consistent setting.

### Chore
- **.dockerignore File**: Created a `.dockerignore` file in the `docker` directory. This file optimizes the Docker build context by excluding the `app` and `tests` directories, leading to faster image builds.

### Feature
- **Test Startup Script**: Added `test_startup.sh` script for executing tests in a Docker container. This script facilitates automated and reproducible test runs in a containerized environment.

## Version 0.1.0

### Added

- **Boot.sh Script**: Added a `boot.sh` script for managing Flask database upgrades and the startup of Gunicorn server. This script simplifies the process of setting up and running the Flask application, ensuring that the database schema is always up-to-date before starting the server.

- **Docker Support**:
  - Created `Dockerfile_prod` for an Alpine-based container setup, specifically tailored for Python 3.8.
  - This Dockerfile sets up an environment optimized for running the microblog application, ensuring portability and ease of deployment across different systems.
