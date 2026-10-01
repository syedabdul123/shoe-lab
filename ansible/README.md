# Deploy to three servers with Docker

Run Ansible from Linux, macOS, or WSL. The target servers must be Ubuntu or Debian machines with SSH access; the configured SSH user must have sudo privileges. Allow inbound TCP port 8000 to reach the app.

1. Copy `inventory.ini.example` to `inventory.ini` and replace the sample IP addresses and SSH user.
2. Make sure your SSH key can connect to all three servers.
3. From the repository root, run:

   ```sh
   ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --ask-become-pass
   ```

The playbook installs Docker and the Compose plugin, then builds and starts the app from the checked-out repository. The app will be available at `http://SERVER_IP:8000` on each host. The Compose service restarts automatically if the container stops.

The playbook deploys the `main` branch from GitHub, so push the deployment changes before running it. If the repository is private, configure Git access for the `shoeapp` user on each server. To run it locally, use `docker compose up --build` from the repository root and open `http://localhost:8000`.