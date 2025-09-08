# Cloud DevOps Pipeline

This repository demonstrates a simple continuous integration and continuous deployment (CI/CD) pipeline
for containerized applications.  It includes a Dockerfile for building a container image and a
GitHub Actions workflow that builds, tests, and deploys the image to an AWS EC2 instance.

## Features

- **Dockerized application**: A basic Python web service that returns a greeting.
- **GitHub Actions workflow**: Automatically build and test the Docker image on every push.
- **Deployment step**: Example commands to deploy the container to an EC2 instance (customize as needed).

## Folder Structure

```
github_projects/cloud-devops-pipeline/
├── README.md             # Overview and instructions
├── app.py                # Sample Python application
├── Dockerfile            # Container build instructions
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Actions workflow
```

## Running Locally

To build and run the container locally:

```bash
docker build -t devops-sample .
docker run -p 8080:8080 devops-sample

# In another terminal
curl http://localhost:8080
```

You should see a greeting message returned from the server.

## GitHub Actions

The workflow defined in `.github/workflows/ci.yml` builds the Docker image, runs basic tests, and
optionally deploys the image.  Customize the `deploy` job according to your environment (e.g.,
upload the image to Amazon Elastic Container Registry and update an ECS or EC2 deployment).