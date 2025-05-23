# Upgrade_Lab


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [AWS Configuration](#aws-configuration)
- [Hugging-face](#hugging-face)
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
Upgrade_Lab is a web-based platform designed to enhance the learning experience by providing a comprehensive environment for coding practice, repository management, and user interaction. The platform supports multiple programming languages and offers features such as code execution, problem-solving, and repository management.

## Features
- **Code Execution**: Write and execute code in multiple programming languages directly in the browser.
- **Problem Solving**: Solve coding problems and get instant feedback on your solutions.
- **Repository Management**: Create and manage repositories, commit changes, and view repository details.
- **User Profiles**: Create and manage user profiles, view other users' profiles, and track progress.
- **Search Functionality**: Search for users and repositories based on various criteria.
- **Chatbot**: Integrate a chatbot using LangChain to provide instant assistance and answer user queries.
- **Dark Mode**: Switch between light and dark themes for a better user experience.

## Technologies Used
- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Django, Python
- **Database**: SQLite (development), PostgreSQL (production)
- **Code Editor**: CodeMirror
- **Version Control**: Git
- **Cloud Services**: AWS (Lambda, S3, etc.)

## AWS Configuration
To configure AWS for your project, follow these steps:

1. **Install the AWS CLI**:
   Follow the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to install the AWS CLI.

2. **Configure AWS CLI**:
   Run the following command and follow the prompts to enter your AWS credentials:
   ```sh
   aws configure
   ```
    You will need to provide:

    - AWS Access Key ID
    - AWS Secret Access Key
    - Default region name (e.g., us-east-1)
    - Default output format (e.g., json)

3. **Set up AWS Lambda**:
    - Create a new Lambda function in the AWS Management Console.
    - Choose a runtime (e.g., Python 3.8) and configure the function as needed.
    - Deploy your code to the Lambda function.

4. **Configure S3 Bucket**:
    - Create a new S3 bucket in the AWS Management Console.
    - Set up appropriate permissions and policies for the bucket.
    - Upload necessary files to the bucket.


5. **Navigate to the IAM Console**:
    - In the AWS Management Console, search for "IAM" and select "IAM" to open the IAM Dashboard.

6. **Create a New IAM User**:
    - In the IAM Dashboard, click on "Users" in the left sidebar.
    - Click on the "Add user" button.
    - Enter a username for the new user.
    - Select the "Programmatic access" checkbox to grant the user access to the AWS API, CLI, and SDK.

7. **Set Permissions**:
    - Click on "Next: Permissions".
    - Choose "Attach existing policies directly".
    - Select the policies that grant the necessary permissions for your use case (e.g., `AmazonS3FullAccess`, `AWSLambdaFullAccess`).
    - Click on "Next: Tags" to add tags if needed, then click on "Next: Review".

8. **Create User**:
    - Review the user details and click on "Create user".

9. **Download Access Key and Secret Key**:
    - After the user is created, you will see the "Success" page.
    - Click on the "Download .csv" button to download the user's access key ID and secret access key.
    - Store the downloaded file in a secure location.

You can now use the access key ID and secret access key in your project by setting them as environment variables or configuring them in the AWS CLI.

## Hugging Face

To use Hugging Face's models and APIs, you need to create an account and generate an API key. Follow these steps:

1. **Create an Account**:
    - Go to the [Hugging Face website](https://huggingface.co/join).
    - Fill in the required details to create a new account.

2. **Generate an API Key**:
    - After logging in, navigate to your [API tokens page](https://huggingface.co/settings/tokens).
    - Click on "New token" to generate a new API key.
    - Copy the generated API key and keep it secure.


## Installation


To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/Upgrade_Lab.git
    cd Upgrade_Lab
    ```

2. **Create virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r req.txt
    ```

4. **Set environment variable**:
    - Create a `.env` file in the root directory of your project.
    - Add the following environment variables and set their values:
    ```env
    IAM_USER_ACCESS_KEY=your-access-key-id
    IAM_USER_SECRET_ACCESS_KEY=your-secret-access-key
    S3_BUCKET_NAME=your-s3-bucket-name
    REGION=your-region

    LAMBDA_COMPILER_FUNCTION="your-python-lambda-function-name"
    LAMBDA_COMPILER_FUNCTION_JS="your-python-lambda-function-name"

    HUGGINGFACE_API_KEY=your-hugging-face-api-key
    ```


5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Install code editor**:
    ```sh
    npm install codemirror
    ``` 

8. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

9. **Open the application in your browser**:
    Navigate to http://127.0.0.1:8000/ to access the application.

10. **Install tailwind css**:
    Open another terminal and activate the virtual environment, then run 
    ```sh
    python manage.py tailwind install
    ```
11. **Start tailwind**
    ```sh
    python manage.py tailwind start
    ```
    Now tailwind css will be applied.

## Docker Setup

To run the project using Docker, follow these steps:

1. **Build the Docker image**:
    ```sh
    docker build -t upgrade_lab .
    ```


## Usage

1. **Login or Register**: Create a new account or log in with your existing credentials.
2. **Explore Problems**: Browse and solve coding problems.
3. **Manage Repositories**: Create and manage your repositories.
4. **View Profiles**: View and edit your profile, and explore other users' profiles.
5. **Search**: Use the search functionality to find users and repositories.
6. **Chatbot**: Interact with the integrated chatbot for instant assistance and answers to your queries.


## Contributing
We welcome contributions to Upgrade_Lab! To contribute, follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes**.
4. **Commit your changes**:
    ```sh
    git commit -m "Add your commit message"
    ```

5. **Push to the branch**:
    ```sh
    git push origin feature/your-feature-name
    ```

6. **Create a pull request**.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
This project is licensed under the MIT License. See the LICENSE file for details.
1. **Email**: [soumensamanta112233@gmail.com](mailto:soumensamanta112233@gmail.com)
2. **GitHub**: [Soumen3](https://github.com/Soumen3)
