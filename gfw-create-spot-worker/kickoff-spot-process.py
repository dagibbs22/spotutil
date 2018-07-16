import argparse


from utilities.spot_instance import Instance
from utilities import util


def main():

    # Parse commandline arguments
    parser = argparse.ArgumentParser(description='Start spot instance and run multiprocessing jobs')

    # Args related to the machine we'll be starting
    parser.add_argument('--ami-id', '-a', default='ami-57990128', help="ID of the AMI you want to launch")
    parser.add_argument('--instance-type', '-i', required=True, help='spot instance type')
    parser.add_argument('--price', default='3.00', help='price for each instance')
    parser.add_argument('--disk-size', '-d', default=500, help='disk size in GB')
    parser.add_argument('--tag', '-t', default='TEMP-TSV-SPOT', help='tag used to ID your instance')

    args = parser.parse_args()

    instance = Instance(args)

    instance.start()

    if args.putty:
        util.launch_putty(instance.instance.ip_address)


if __name__ == '__main__':
    main()