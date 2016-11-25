apt-get update -y && apt-get upgrade -y
apt-get install git wget python python-pip python-dev vim supervisor -y

cd /opt
git clone https://github.com/Gloomywind/redispot.git

cd redispot/
pip install -r requirements.txt

var=$(curl http://queryip.net/ip/)
cat > redis.conf <<EOF
[IP]
ip = $var
EOF

cat > /etc/supervisor/conf.d/shockpot.conf <<EOF
[program:redispot]
command=nohup python /opt/redispot/redispot.py >/dev/null 2>&1 & 
directory=/opt/redispot
stdout_logfile=/opt/redispot/redispot.out
stderr_logfile=/opt/redispot/redispot.err
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=QUIT
EOF

service supervisor start
supervisorctl update