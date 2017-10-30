#!/bin/bash

scrapyd &

scrapyd-deploy

sleep 5

curl http://localhost:6800/schedule.json -d project=Damoa -d spider=clien
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=bobaedream
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=gameshot
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=ruli
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=humoruniv
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=thisisgame
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=ygosu

sleep 5

curl http://localhost:6800/schedule.json -d project=Damoa -d spider=fmkorea
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=82cook
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=dramameeting
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=underkg
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=giggle
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=hwbattle
curl http://localhost:6800/schedule.json -d project=Damoa -d spider=quasarzone

sleep 5

#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=82cook;
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=dramameeting;
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=underkg;
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=giggle;
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=hwbattle;
#curl http://localhost:6800/schedule.json -d project=Damoa -d spider=quasarzone;
