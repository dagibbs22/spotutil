import argparse


from utilities.spot_instance import Instance


def main():

    # Parse commandline arguments
    parser = argparse.ArgumentParser(description='Start spot instance and run multiprocessing jobs')
    
    # Args related to the machine we'll be starting
    parser.add_argument('--ami-id', '-a', default='ami-40275656', help="ID of the AMI you want to launch")
    parser.add_argument('--instance-type', '-i', required=True, help='spot instance type')
    parser.add_argument('--price', default='3.00', help='price for each instance')
    parser.add_argument('--disk-size', '-d', default=50, help='disk size in GB')

    # Args related to scripts that fab will run
    parser.add_argument('--prep-script', '-p', help='script that should run first on the instance')
    parser.add_argument('--main-script', '-m', help='main multiprocessing script')

    args = parser.parse_args()

    instance = Instance(args)

    instance.start()

    instance.run(args.prep_script, 'prep')

    instance.run(args.main_script, 'main')


if __name__ == '__main__':
    main()

