# Changelog for microblog

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
