## How to start this application

### Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Rename `config.py.txt` to `config.py`.

3. Add the following secrets to `config.py`:

    ```python
    SECRET_KEY = "your_secret_key_here"
    GOOGLE_CLIENT_ID = "your_google_client_id_here"
    GOOGLE_CLIENT_SECRET = "your_google_client_secret_here"
    GITHUB_CLIENT_ID = "your_github_client_id_here"
    GITHUB_CLIENT_SECRET = "your_github_client_secret_here"
    ```

### Running the Application

1. Create an admin user:

    ```bash
    flask fab create-admin
    ```

2. Build and run the Docker container:

    ```bash
    docker build -t auth-app .
    docker run -d -p 8080:5000 auth-app
    ```

