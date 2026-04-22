import subprocess

class IptableConfigurator:
    def snmp_config(self, interface, ip, port):
        # Construct the command
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--dport", str(port), "-j", "DROP"]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print("snmp_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing snmp_config command:", e)

    def sts_config(self, interface, ip, port):
        # Construct the command
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-p", "tcp", "--dport", str(port), "-j", "DROP"]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print("snmp_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing snmp_config command:", e)

    def icmp_config(self, interface, ip, protocol):
        # Code for ICMP configuration
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-s", ip, "-p", protocol, "-j", "ACCEPT"]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print("icmp_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing icmp_config command:", e)

    def telnet_disable_config(self, interface, protocol,port):
        # Code for ICMP configuration
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-p", protocol, "--sport", port, "-j", "DROP"]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print("telnet_disable_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing telnet_disable_config command:", e)

    def ftp_disable_config(self, interface, protocol,port):
        # Code for ICMP configuration
        command = ["sudo", "iptables", "-A", "INPUT", "-i", interface, "-p", protocol, "--sport", port, "-j", "DROP"]

        # Execute the command
        try:
            subprocess.run(command, check=True)
            print("ftp_disable_config rule added successfully.")
        except subprocess.CalledProcessError as e:
            print("Error executing ftp_disable_config command:", e)

    def ssh_disable_dataplane_interface(self, protocol, port):
        # Code for ICMP configuration
        commands = [
            ["sudo", "iptables", "-A", "INPUT", "-i", "dp0s8", "-p", protocol, "--dport", port, "-j", "DROP"],
            ["sudo", "iptables", "-A", "INPUT", "-i", "dp0s9", "-p", protocol, "--dport", port, "-j", "DROP"]
        ]

        # Execute the commands
        for command in commands:
            try:
                subprocess.run(command, check=True)
                print("Command executed successfully:", " ".join(command))
            except subprocess.CalledProcessError as e:
                print("Error executing command:", " ".join(command), e)


def main():
    configurator = IptableConfigurator()
    configurator.snmp_config("ens3","172.25.142",9453)
    configurator.sts_config("ens3", "172.25.142", 8020)
    configurator.icmp_config("ens3","192.168.173.61", "icmp")
    configurator.telnet_disable_config("ens3","tcp",23)
    configurator.ftp_disable_config("ens3", "tcp", 21)
    configurator.ssh_disable_dataplane_interface("tcp",22)

if __name__ == "__main__":
    main()
