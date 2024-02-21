**bale-chatgpt**

This project is used to make a bot in bale which it works as agent of chatgpt. This bot asks your questions from Chatgpt API and sends you the answer.

**prerequisite:**

You can use this application on any Linux distribution, Windows or Mac. I write the Linux guide.
Preferably use Python version 3.11.3

`mv bale-chatgpt-main /opt/`

**Network requirements:**

Make sure that you have the right access to openai, you can use a server which doesnt have any limitation from openai or you can use shekan like this:

`echo "nameserver 178.22.122.100" > /etc/resolv.conf`

**Installation:**

`cd /opt/bale-chatgpt-main`

`python -m venv venv`

`source activate venv/bin/activate`

`pip install -r requirements.txt`

`cat balegpt.service > /etc/systemd/system/balegpt.service`

`systemctl daemon-reload`

`systemctl start balegpt`

`systemctl status balegpt`

`systemctl enable balegpt`
