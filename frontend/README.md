# Run frontend component

## Steps run the frontend without Docker

Find the file `public-html/index.html`

Open the file in your browser:

- Option 1:
  Double-click the HTML file (e.g., index.html) in your file explorer. This will open it in your default browser.

- Option 2:
  Drag and drop the HTML file into an open browser window.

- Option 3:
  Open your browser, use the shortcut Ctrl + O (or Cmd + O on macOS), select the HTML file in the dialog, and click Open.


## Steps to run the frontend with Docker

1. Inside frontend folder, build the image:

```bash
# Replace japeto with your preferred nickname
docker build -t valu/simfrontend .
```

2. Run container with:

```bash
docker run --name simfrontend -d -p 0.0.0.0:3000:80 valu/simfrontend
```

3. Access the frontend in your browser:

Open your browser and navigate to:

```plaintext
http://localhost:3000
```

This will load the frontend served by the Docker container.

## Unisg Docker Compose

1. From the project root (where docker-compose.yml is located), execute

```bash
docker-compose up --build frontend
```

2. Access the Services:

- Frontend: http://localhost:3000

Stop the Services:

3. To stop and remove the containers, run:

```bash
docker-compose down
```