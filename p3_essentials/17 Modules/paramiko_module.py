__author__ = 'rafael'


'''
Method
    def ssh_commander(self, device, username, password, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        data = None
        try:
            conn = ssh.connect(device, username=username, password=password, timeout=4)
            if conn is None:
                stdin, stdout, stderr = ssh.exec_command(command)
                data = stdout.read().decode("utf-8")
                ssh.close()
        except paramiko.AuthenticationException as e:
            print('Authentication Failed')
        except paramiko.SSHException as e:
            self.ssh_commander_data = 'Error, {}'.format(e)
        except socket.error as e:
            self.ssh_commander_data = 'Error, {}'.format(e)
        except ConnectionRefusedError as e:
            self.ssh_commander_data = 'Error, {}'.format(e)
        except KeyboardInterrupt:
            print('Goodbye')
            exit()
        else:
            self.ssh_commander_data = data

        return self.ssh_data

'''

__author__ = 'rafael'


import paramiko
import socket

def ssh_commander(devices, commands, username, password):
    data = []
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # The break avoids an unecesary iteration on commands after is unable to connect the first time
    for device in devices:
        for command in commands:
            try:
                conn = ssh.connect(device, username=username, password=password, timeout=4)
                if conn is None:
                    stdin, stdout, stderr = ssh.exec_command(command)
                    data.append(stdout.read().decode("utf-8"))
                    ssh.close()
            except paramiko.AuthenticationException:
                output = "Authentication Failed"
                data.append(output)
                break
            except paramiko.SSHException:
                output = "Issues with SSH service"
                data.append(output)
                break
            except socket.error:
                output = "Connection Error"
                data.append(output)
                break
            except ConnectionRefusedError:
                output = 'Connection Error'
                data.append(output)
                break
            except KeyboardInterrupt:
                print('Goodbye')
                exit()
    return data

print(ssh_commander(['10.0.1.100', '10.0.1.24'], ['whoami', 'pwd'], 'rafael', 'Levittown'))

'''
if __name__ == "__main__":
    import timeit
    print(timeit.timeit('ssh_commander()', setup="from __main__ import ssh_commander", number=10))
'''