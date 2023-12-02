# cloverSSH

Mass data generation using SSH clustering for CloverEngine. 

## Usage

Install the `argparse` and `parallel-ssh` python libraries. Edit the `configuration.py` file with your ssh credentials, or pass the credentials with flags. You can also change the default threads and number of generated positions. You can see all the flags using `python main.py --help`. Append the host names you want to connect to to the `hosts.txt` file. To run the script `python main.py`.
