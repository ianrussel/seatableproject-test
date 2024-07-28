sudo apt-get update
sudo apt-get install -y gstreamer1.0-libav gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev

crontab entry

Adjust interval, in this example it runs every 2 and 3 minutes

```
*/2 * * * * /home/ianrussel/projects/tests/seatable/bin/python /home/ianrussel/projects/tests/seatable/Update_analyser.py >> /home/ianrussel/projects/tests/seatable/logfile.log 2>&1
```

```
*/3 * * * * /home/ianrussel/projects/tests/seatable/bin/python /home/ianrussel/projects/tests/seatable/Volume_Dim.py >> /home/ianrussel/projects/tests/seatable/logfile.log 2>&1
```

to add entry

Run `crontab -e`

to check entry

Run `crintab -l`
