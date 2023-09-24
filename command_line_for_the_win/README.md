```text
	command_line_for_the_win
```
# Guide:
## How to Connect with SFTP
By default, SFTP uses the SSH protocol to authenticate and establish a secure connection. Because of this, the same authentication methods are available that are present in SSH.

Although you can authenticate with passwords by default, we recommend you create SSH keys and transfer your public key to any system that you need to access. This is much more secure and can save you time in the long run.

Please see this guide to set up SSH keys in order to access your server if you have not done so already.

If you can connect to the machine using SSH, then you have completed all of the necessary requirements necessary to use SFTP to manage files. Test SSH access with the following command:

```bash
 $ ssh sammy@your_server_ip_or_remote_hostname
```
If that works, exit back out by typing:
```bash
 $ exit
```
Now we can establish an SFTP session by issuing the following command:
```bash
 $ sftp sammy@your_server_ip_or_remote_hostname
```
You will connect the the remote system and your prompt will change to an SFTP prompt.

If you are working on a custom SSH port (not the default port 22), then you can open an SFTP session as follows:
```bash
 $ sftp -oPort=custom_port sammy@your_server_ip_or_remote_hostname
```
This will connect you to the remote system by way of your specified port.

## Transferring Files with SFTP
If we want to download files from our remote host, we can do so using the get command:
```bash
sftp> get remoteFile
```
```bash
Output
Fetching /home/demouser/remoteFile to remoteFile
/home/demouser/remoteFile                       100%   37KB  36.8KB/s   00:01
```
As you can see, by default, the get command downloads a remote file to a file with the same name on the local file system.

We can copy the remote file to a different name by specifying the name afterwards:
```bash
sftp> get remoteFile localFile
```
The get command also accepts some option flags. For instance, we can copy a directory and all of its contents by specifying the recursive option:
```bash
sftp> get -r someDirectory
```
We can tell SFTP to maintain the appropriate permissions and access times by using the -P or -p flag:
```bash
sftp> get -Pr someDirectory
```
## Transferring Local Files to the Remote System
Transferring files to the remote system works the same way, but with a put command:
```bash
sftp> put localFile
```
```bash
Output
Uploading localFile to /home/demouser/localFile
localFile                                     100% 7607     7.4KB/s   00:00
```
