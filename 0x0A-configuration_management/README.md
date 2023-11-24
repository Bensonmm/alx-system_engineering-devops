0x0A-configuration_management

in this project .i started waorking with puppet as a configuration management  tool. 
objective 
1. writing puppet manifest files to create a file , install packages and execute a command 

** tasks:  page _with_curl:
** 0-create_a_file.pp

Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet

** 1-install_a_package.pp

Using Puppet, install flask from pip3.

Requirements:

Install flask
Version must be 2.1.0

** 2-execute_a_command.pp

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill

Terminal #0 - starting my process
Terminal #1 - executing my manifest
Terminal #0 - process has been terminated