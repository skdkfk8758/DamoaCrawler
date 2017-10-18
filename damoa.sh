#! bin/bash

scrapyd &

python3.6 scrapyd-client/scrapyd_client/deploy.py

curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=bobaedream
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=gameshot
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=ruli
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=humoruniv
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=thisisgame
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=ygosu
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=becle
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien

