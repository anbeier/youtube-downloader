#!/usr/bin/env python3

import subprocess
import tempfile
import sys
import os


youtube_url = sys.argv[1]
mp3_name = sys.argv[2]

with tempfile.TemporaryDirectory() as tmpdir:
    tmpfile = os.path.abspath(tmpdir + '/tmp')
    subprocess.check_call(['youtube-dl','-fbest', '-o', tmpfile, youtube_url])
    subprocess.check_call(['ffmpeg', '-i', tmpfile, '-b:a', '192k', '-f', 'mp3', mp3_name])
