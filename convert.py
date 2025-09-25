#!/usr/bin/python

import os
import subprocess
import datetime
import time
import multiprocessing

SOURCE_DIR = "source"
DIST_DIR = "dist"

threads = []
MAX_PARALLEL_THREADS = multiprocessing.cpu_count()
thread_window = 0

def convert_figma_to_sketch(source, dest):
    print(f"🎨 Converting {source} to sketch >>> {dest}")
    subprocess.call(["fig2sketch", source, dest])
    print (f"✅ New file converted {dest}")


if __name__ ==  '__main__':
    print (f"⏰ Starting time {datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')}")
    print ("😶‍🌫️ Setting up...")
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)
    print ("✅ Done")

    for root, dirs, files in os.walk(SOURCE_DIR):
        path = root.split(os.sep)
        for file in files:
            name, ext = os.path.splitext(file)
            source = os.path.join(root, name + ext)
            dest = os.path.join(DIST_DIR, name + ".sketch")
            if ext == ".fig":
                t = multiprocessing.Process(target=convert_figma_to_sketch, args=(source, dest))
                threads.append(t)
                thread_window += 1
            if thread_window == MAX_PARALLEL_THREADS:
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()
                threads = []
                thread_window = 0

    # Process remaining threads
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"⏰ End time {datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')}")