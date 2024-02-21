**bale-chatgpt**

*This project is used to make a bot in bale which it works as agent of chatgpt. This bot asks your questions from Chatgpt API and sends you the answer.*

**prerequisite:**

*You can use this application on any Linux distribution, Windows or Mac. I write the Linux guide.
Preferably use Python version 3.11.3*

`mv bale-chatgpt-main /opt/`

**Network requirements:**

*Make sure that you have the right access to openai, you can use a server which doesnt have any limitation from openai or you can use shekan like this:*

`echo "nameserver 178.22.122.100" > /etc/resolv.conf`

**Installation:**

*change directory to the project directory*

`cd /opt/bale-chatgpt-main`

*create virtual environment and activate it*

`python -m venv venv`

`source activate venv/bin/activate`

*install python libraries which they need for running application*

`pip install -r requirements.txt`

*create a file service for application and start it*

`cat balegpt.service > /etc/systemd/system/balegpt.service`

`systemctl daemon-reload`

`systemctl start balegpt`

*check availability of this service*

`systemctl status balegpt`

*Enable this service for subsequent boots*

`systemctl enable balegpt`
