# bale-chatgpt
this project is used to make a bot in bale which it works as a chatgpt

# code
pip install -r requirements.txt
cat balegpt.service > /etc/systemd/system/balegpt.service
systemctl daemon-reload
systemctl start balegpt
systemctl enable balegpt
