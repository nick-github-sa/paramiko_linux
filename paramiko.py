import csv
import paramiko


# paramiko main connect and command run
def connect_and_run_command(ip, private_key_path, passphrase, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("Connecting to server")
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path, password=passphrase)
    client.connect(ip, port=22, username='tenable', pkey=private_key)
	print("Connected to server")
	(stdin, stdout, stderr) = ssh.exec_command(command)
    output = stdout.read().decode('utf-8')

	return output
    client.close()

# main add IP's and keypaths
def main():
    ip_list = ['10.1.1.1']
    private_key_path = 'key_path'
    passphrase = 'xxxxxxxxxxxxxxxxx'
    command = "hostname && ip -o addr | awk '!/^[0-9]*: ?lo|link\\/ether/ && !/inet6 [[:xdigit:]:]+\\/[0-9]+/ {print $2\" \"$4}'"

    output_file = 'output.csv'
    header = ['IP Address', 'Output']
    rows = []

    for ip in ip_list:
        output = connect_and_run_command(ip, private_key_path, passphrase, command)
        rows.append([ip, output])

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Command output saved to '{output_file}'.")

if __name__ == '__main__':
    main()
