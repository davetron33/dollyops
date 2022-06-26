# dollyops-CTF
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
This is a simple web app that (1) writes a key called 'dolly_ctf' and provides it with a polite greeting as a value and stores them both to a Redis database. It was built for the Dolly SRE Interview mini project. 

## How to use this webapp:
1. Install Docker
2. Clone the repo using: 
3. Update the redis passwords in `config/redis.conf:2`, `docker-compose.yml:8,19`. These passwords MUST match! 
4. run `docker compose up -build` from the repository root to build all necessary images, and `docker compose up` subsequently to bring the web app back up. (alternatively, to destroy the web app and remove all images, use `docker compose down`)
5. Navigate to `https://localhost:9001` in your browser to see the web app in action!




