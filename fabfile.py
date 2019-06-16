import os

from patchwork import files
from fabric import Connection, Config, task


@task
def deploy(c):
    remote_user = os.environ['REMOTEUSER']
    remote_pass = os.environ['USERPASS']
    host = os.environ['REMOTEHOST']

    config = Config(overrides={'sudo': {'password': remote_pass}})
    connect_kwargs = {"password": remote_pass, 'allow_agent': False}
    with Connection(host=host, user=remote_user, config=config, connect_kwargs=connect_kwargs) as conn:
        print("Connected with remote server")

        print("Copy sources")
        conn.put("app.py")
        conn.put("requirements.txt")

        print("Install requirements")
        conn.sudo("pip3 install -r requirements.txt")

        if files.exists(conn, "/root/server.pid"):
            print("Shutdown previous server")
            conn.sudo("pkill -F server.pid")

        print("Run server")
        conn.sudo("nohup python3 app.py &> /dev/null & echo $! > server.pid")
        print("Success!")
