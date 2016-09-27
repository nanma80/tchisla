#!/usr/bin/env python

import os
import tchisla as t

if not os.path.exists(t.records.tmp_dir):
  os.makedirs(t.records.tmp_dir)


if os.path.exists(t.records.cache_path):
  os.remove(t.records.cache_path)

t.records.load()
