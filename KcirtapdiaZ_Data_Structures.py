import csv
import sys
from collections import deque

class Request:
  def __init__(self, timestamp, path, process_time):
    self.timestamp = timestamp
    self.path = path
    self.process_time = process_time

class Server:
  def __init__(self):
    self.queue = deque()
    self.current_time = 0

  def process_request(self, request):
    wait_time = max(0, self.current_time - request.timestamp)
    self.current_time = max(self.current_time, request.timestamp) + request.process_time
    return wait_time

def simulateOneServer(datafile):
  server = server()
  total_wait_time = 0
  total_requests = 0

  with open(datafile, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      timestamp, path, process_time = int(row[0]), row[1], int(row[2])
      request = Request(timestamp, path, process_time)
      wait_time = server.process_request(request)
      total_wait_time += wait_time
      total_request += 1

average_wait_time = total_wait_time / total_requests if total_requests else 0
return average_wait_time

def simulatedManyServers(datafile, num_servers):
  servers = [Server() for _ in range(num_servers)]
  total_wait_time = 0
  total_requests = 0
  server_index = 0

  with open(datafile,'r') as file:
    reader = csv.reader(file)
    for row in reader:
      timestamp, path, process_time = int(row[0]), row[1], int(row[2])
      request = Request(timestamp, path, process_time)
      wait_time = servers[server_index].process_request(request)
      total_wait_time += wait_time
      total_request += 1
      server_index = (server_index + 1) % num_servers

  average_wait_time = total_wait_time / total_requests if total_requests else 0
  return average_wait_time

def main():
  if len(sys.argv) < 2:
    print("Usage: python simulation.py <datafile> [num_servers]")
    sys.exit(1)

  datafile = sys.argv[1]

  if len(sys.argv) == 3:
    num_servers = int(sys.argv[2])
    average_wait_time = simulatedManyServers(datafile, num_servers)
  else:
    average_wait_time = simulationOneServer(datafile)

  print(f"Average wait time: {average_wait_time:.2f} seconds")

if __name__ == "__name__":
  main()
