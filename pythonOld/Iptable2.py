import subprocess

class IptableConfigurator:
    def __init__(self, variables_file="variables.txt"):
        self.variables = self.load_variables(variables_file)

    def load_variables(self, filename):
        variables = {}
        with open(filename, 'r') as file:
            for line in file:
                name, value = line.strip().split(":")
                variables[name.strip()] = value.strip()
        return variables

    def snmp_config(self, interface):
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--dport", self.variables["sts_port"], "-j", "DROP"]
        try:
            subprocess.run(command, check=True)
            print("snmp_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing snmp_config command:", e)

    def sts_config(self, interface):
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--dport", self.variables["sts_port"], "-j", "DROP"]
        try:
            subprocess.run(command, check=True)
            print("sts_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing sts_config command:", e)

    # Define other methods similarly

def main():
    configurator = IptableConfigurator()
    configurator.snmp_config("ens3")
    configurator.sts_config("ens3")
    # Call other methods similarly

if __name__ == "__main__":
    main()
