# Deploying a Flask Application with Gunicorn and Nginx

This document explains the steps and commands used to deploy a Flask application on a Linux server using Gunicorn as the WSGI server and Nginx as the reverse proxy.

## User Setup and SSH Configuration

### Create a New User
```sh
adduser user_name
```

### Grant Sudo Privileges
```sh
usermod -aG sudo user_name
```
Adds the user to the sudo group, allowing them to run commands with administrative privileges.

### Edit SSH Configuration
```sh
nano /etc/ssh/sshd_config
```
Opens the SSH server configuration file. You might need to make changes to secure SSH access, such as disabling root login or changing the default port.

### Restart SSH Service
```sh
systemctl restart sshd
```
Restarts the SSH service to apply any changes made to the configuration file.

## Application Setup

### SSH into the Server
```sh
ssh username@domain_name.com
```
Connects to the server using SSH. Replace username and domainname.com with your actual username and server domain or IP address.

### Clone the Git Repository

```sh
git clone url
```
Clones the repository containing your Flask application. Replace url with the URL of your Git repository.

# Create and Activate a Python Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```
Creates a virtual environment named venv and activates it. This isolates your project's dependencies.

### Install Python Dependencies

```sh
pip install -r requirements.txt
pip install gunicorn
```
Installs the Python packages listed in requirements.txt and Gunicorn, the WSGI server.

### Edit the WSGI Entry Point

```sh
nano wsgi.py
```
Opens the wsgi.py file for editing. This file should contain the WSGI application callable (usually named app).

### Run Gunicorn

```sh
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
Starts the Gunicorn server, binding it to all network interfaces on port 5000. wsgi:app refers to the WSGI application callable in wsgi.py.

## Systemd Service for Gunicorn

### Create a Systemd Service File

```sh
sudo nano /etc/systemd/system/app_name.service
```
Opens the systemd service file for your application. Replace app_name with a descriptive name for your service.

Example service file content:
```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=user_name  
Group=www-data
WorkingDirectory=/home/user_name/flask_app
Environment="PATH=/home/user_name/flask_app/venv/bin"
ExecStart=/home/user_name/flask_app/venv/bin/gunicorn --workers 3 --bind unix:/home/user_name/flask_app/peak.sock wsgi:app

[Install]
WantedBy=multi-user.target
```

This file configures Gunicorn to run as a systemd service.

Start and Enable the Gunicorn Service

```sh

sudo systemctl start app
sudo systemctl enable app
sudo systemctl status app
```
Starts the Gunicorn service, enables it to start on boot, and checks its status.

## Nginx Setup

### Install Nginx

```sh
sudo apt install nginx
```
Installs the Nginx web server.

### Configure Nginx

```sh
sudo nano /etc/nginx/sites-available/app_name.conf
```
Opens the Nginx configuration file for your application.

Example Nginx configuration:
```nginx

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user_name/flask_app/peak.sock;
    }
}
```
This configuration sets up Nginx to proxy requests to Gunicorn via the Unix socket.

### Enable the Nginx Site

```sh
sudo ln -s /etc/nginx/sites-available/app_name.conf /etc/nginx/sites-enabled/
```
Creates a symbolic link to enable the site configuration.

### Test and Restart Nginx

```sh
sudo nginx -t
sudo systemctl restart nginx
```
Tests the Nginx configuration for syntax errors and restarts Nginx to apply changes.

### Configure the Firewall

```sh
sudo ufw enable
sudo ufw status
sudo ufw delete allow 5000
sudo ufw allow "Nginx Full"
```
Enables the firewall, deletes any rule allowing port 5000 (used by Gunicorn), and allows traffic for Nginx.

## Final Checks

### Check Directory Permissions

```sh
sudo chmod 775 /home/user_name/
sudo chown user_name:www-data /home/user_name/flask_app/peak.sock
```
Sets the permissions of the specified directory. Ensure this is appropriate for your use case and security policies.

### View Nginx Logs

```sh
sudo tail /var/log/nginx/error.log
```
Views the Nginx error log for troubleshooting any issues.
