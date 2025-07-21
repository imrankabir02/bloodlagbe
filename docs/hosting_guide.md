# Hosting on PythonAnywhere Guide

This guide will walk you through the process of deploying your Django project to PythonAnywhere.

## Prerequisites

*   A GitHub account with your project pushed to a repository.
*   A PythonAnywhere account.

## Step 1: Clone the Repository on PythonAnywhere

1.  Log in to your PythonAnywhere account.
2.  Open a new **Bash Console**.
3.  Clone your repository from GitHub by running the following command. Replace `<your-github-username>` and `<your-repository-name>` with your actual GitHub username and repository name.

    ```bash
    git clone https://github.com/imrankabir02/bloodlagbe.git
    ```

## Step 2: Create a Virtual Environment

1.  Navigate into your project's directory:

    ```bash
    cd bloodlagbe
    ```

2.  Create a virtual environment for your project. It's good practice to use the same Python version as your project.

    ```bash
    mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv
    ```
    *(Replace `my-virtualenv` with your preferred name)*

## Step 3: Install Dependencies

1.  Activate your virtual environment (it should be activated automatically after creation). If you need to activate it manually:
    ```bash
    workon my-virtualenv
    ```
2.  Install the project dependencies using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Step 4: Set up the Web App on PythonAnywhere

1.  Go to the **Web** tab on your PythonAnywhere dashboard.
2.  Click on **Add a new web app**.
3.  Follow the prompts:
    *   Your domain name will be `<your-username>.pythonanywhere.com`.
    *   Select **Manual configuration** (it's important to choose this).
    *   Select the same Python version you used for your virtual environment (e.g., Python 3.10).

## Step 5: Configure the WSGI File

1.  On the **Web** tab, find the **Code** section and click on the WSGI configuration file link (e.g., `/var/www/<your-username>_pythonanywhere_com_wsgi.py`).
2.  Edit the file to match your Django project's structure. It should look something like this:

    ```python
    import os
    import sys

    # Add the project to the Python path
    path = '/home/<your-username>/bloodlagbe'
    if path not in sys.path:
        sys.path.insert(0, path)

    # Set the Django settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'blood_project.settings'

    # Import the Django WSGI application
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
    *Make sure to replace `<your-username>` with your actual PythonAnywhere username.*

## Step 6: Configure Static Files

1.  Go back to the **Web** tab.
2.  In the **Static files** section, add a new entry:
    *   **URL:** `/static/`
    *   **Directory:** `/home/<your-username>/bloodlagbe/static`
    *(Replace `<your-username>` with your PythonAnywhere username)*
3.  You will need to collect your static files. Open a Bash console in your project directory and run:
    ```bash
    python manage.py collectstatic
    ```

## Step 7: Set Environment Variables (if any)

If your project uses environment variables (e.g., for `SECRET_KEY`), you can set them in the **Web** tab under the **Code** section in a `.env` file.

## Step 8: Reload the Web App

1.  Go to the **Web** tab.
2.  Click the big green **Reload** button to apply your changes.
3.  Visit your site at `<your-username>.pythonanywhere.com` to see your live application.

## Troubleshooting

*   **Check the error log:** The error log link is on the **Web** tab. It's the first place to look if you have any issues.
*   **Check the server log:** This log shows information about your server's activity.
*   **Make sure your virtual environment is correct:** In the **Web** tab, ensure the path to your virtual environment is correctly set.
