import os

from fabric import Connection, Config, task


@task
def deploy(c):
    remote_user = os.environ['REMOTEUSER']
    remote_pass = os.environ['USERPASS']
    host = os.environ['REMOTEHOST']
    port = os.environ['PORT']

    config = Config(overrides={'sudo': {'password': remote_pass}})
    connect_kwargs = {"password": remote_pass, 'allow_agent': False}
    with Connection(host=host, user=remote_user, config=config, connect_kwargs=connect_kwargs) as conn:
        print("Connected with remote server")
        print("Copy sources")
        conn.put("app.py")
        conn.put("requirements.txt")
        print("Install requirements")
        conn.sudo("pip3 install -r requirements.txt")
        print("Run server")
        if fabric.contrib.files.exists("/root/server.pid"):
            print("ASDHJKFDSHG")

        conn.sudo("nohup python3 app.py & echo $! > pid")
        print("Success!")
