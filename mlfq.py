#!/usr/bin/env python3

from collections import deque

class Process:
  def __init__(self, name, duration, time_arrival):
    self.name = name
    self.duration = duration
  
  def exec(self, time_exec):
    if (time_exec >= self.duration):
      self.duration = 0
    else:
      self.duration -= time_exec
  
class FIFO:
  def __init__(self):
    self.q = deque()
    self.time = 0
  
  def add_process(self, process):
    self.q.append(process)
  
  def run_all_process(self):
    while self.q:
      cur = self.q.popleft()
      print(cur.name, cur.duration)
      cur.exec(cur.duration)

if __name__ == "__main__":
  sched = FIFO()
  sched.add_process(Process('A', 100, 0))
  sched.add_process(Process('B', 10, 0))
  sched.add_process(Process('C', 10, 0))
  sched.run_all_process()
