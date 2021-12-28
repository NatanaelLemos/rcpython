mv ./bot ../rcpython_bot
mv ./venv ../rcpython_venv

scp -r ./* pi@10.0.0.110:/home/pi/rcpython/

mv ../rcpython_bot ./bot
mv ../rcpython_venv ./venv
# scp -r ./bot/* pi@10.0.0.110:/home/pi/rcpython/