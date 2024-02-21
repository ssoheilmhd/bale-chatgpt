**bale-chatgpt**

*This project is used to make a bot in bale which it works as agent of chatgpt. This bot asks your questions from Chatgpt API and sends you the answer. You can have a conversation with chatgpt without any limitation*

**prerequisite:**

*You can use this application on any Linux distribution, Windows or Mac. I write the Linux guide.

Preferably use Python version 3.11.3*

*You need to sign up in openai to get access to openaiAPItoken, if you dont want to use your personal number to sign up on this site, I suggest you to use https://numberland.ir. You can buy a virtual number from anywhere to use it for openai.
After the registration you need to create API access key (use this tutorial https://platform.openai.com/docs/quickstart) set your API access key on .env file as openaiAPItoken*

*You need to make a bot in bale platform.It's similar to telegram but if you need to help you can use this documentation : https://blog.bale.ai/making-a-bot. After the registration on bale botfather you need to copy your API access key and paste it on .env file as baleAPItoken*

**Network requirements:**

*Make sure that you have the right access to openai, you can use a server which doesnt have any limitation from openai or you can use shekan like this:*

`echo "nameserver 178.22.122.100" > /etc/resolv.conf`

**Installation:**

*Clone the project and move it to the /opt*

`mv bale-chatgpt-main /opt/`

*Change directory to the project directory*

`cd /opt/bale-chatgpt-main`

*Create virtual environment and activate it*

`python -m venv venv`

`source activate venv/bin/activate`

*Install python libraries which they need for running application*

`pip install -r requirements.txt`

*Create a file service for application and start it*

`cat balegpt.service > /etc/systemd/system/balegpt.service`

`systemctl daemon-reload`

`systemctl start balegpt`

*check availability of this service*

`systemctl status balegpt`

*Enable this service for subsequent boots*

`systemctl enable balegpt`
