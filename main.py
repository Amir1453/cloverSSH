from pssh.clients import ParallelSSHClient
import configuration
import argparse

parser = argparse.ArgumentParser(prog="multiSSH",description="Connects to all the hosts in hosts.txt and runs Clover-generator",epilog="Stand on the shoulders of the giants")
parser.add_argument("-p", "--positions", type=int, default=configuration.default_positions, help="The number of positions to generate")
parser.add_argument("-t", "--threads", type=int, default=configuration.default_threads, help="The number of threads to use")
parser.add_argument("-u", "--username", type=str, default=configuration.username, help="Username for SSH connection")
parser.add_argument("-pw", "--password", type=str, default=configuration.password, help="Password for SSH connection")
parser.add_argument("-hs", "--hosts", type=str, default=configuration.hosts_path, help="Path to the hosts file")

args = parser.parse_args()

with open(args.hosts,"r") as file:
    hosts = []
    for line in file:
        hosts.append(line.rstrip("\n"))
    if hosts[-1] == "":
        hosts.pop()

client = ParallelSSHClient(hosts, args.username, args.password)

cmd = ["mkdir -p ~/CloverMassData/$(uname -n)", f"~/CloverEngine/src/Clover-generator generate {args.positions} {args.threads} ~/CloverMassData/$(uname -n)/ $SRANDOM"]

shells = client.open_shell()
client.run_shell_commands(shells,cmd)

client.join_shells(shells)
