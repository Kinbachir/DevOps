PPM and PGCD Calculator
This project is a Python script for calculating the PGCD (Greatest Common Divisor) and PPM (Least Common Multiple) of two integers. It is containerized using Docker and includes a CI/CD pipeline with GitHub Actions.

Features
Calculate PGCD (GCD) and PPM (LCM) for two integers.
Run locally or in a Docker container.
Automated CI/CD pipeline.
How to Use
Run Locally
Clone the repository:

bash

git clone https://github.com/your-username/ppm-pgcd-calculator.git
cd ppm-pgcd-calculator
Run the script:

bash

python app.py
Enter two integers when prompted.

Run with Docker
Build the Docker image:

bash

docker build -t ppm-pgcd-calculator .
Run the Docker container:

bash

docker run -it ppm-pgcd-calculator
CI/CD Pipeline
This project uses GitHub Actions to:

Build and push the Docker image to Docker Hub.
Analyze code quality with SonarQube.
Deploy the Docker image to Azure.
Required GitHub Secrets
DOCKER_USERNAME and DOCKER_PASSWORD
SONAR_PROJECT_KEY, SONAR_ORGANIZATION, SONAR_HOST_URL, SONAR_TOKEN
AZURE_APP_NAME and AZURE_PUBLISH_PROFILE
Example Output
bash

Enter the first number: 18
Enter the second number: 24
PGCD (GCD) of 18 and 24 is: 6
PPM (LCM) of 18 and 24 is: 72
License
This project is licensed under the MIT License.

This version keeps the essential information while being more concise. Let me know if you want further simplifications!