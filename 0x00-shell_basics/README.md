shell basics

This directory covers the basics of shell scripting and familiarizes you with the command-line interface.

Tasks

   `0-current_working_directory`: Prints the absolute pathname of the current working directory.
    

   `1-listit`: Displays the contents list of the current directory.
    
   `2-bring_me_home`: Changes the working directory to the user's home directory.
    
   `3-listfiles`: Displays the current directory contents in long format.
    
   `4-listmorefiles`: Displays the current directory contents, including hidden files, in long format.
    
   `5-listfilesdigitonly`: Displays current directory contents, including hidden files, in long format with user and group IDs displayed numerically.
    
   `6-firstdirectory`: Creates a directory named my_first_directory in /tmp/.
    
   `7-movethatfile`: Moves the file betty from /tmp/ to /tmp/my_first_directory.
    
   `8-firstdelete`: Deletes the file betty in /tmp/my_first_directory.
    
   `9-firstdirdeletion`: Deletes the directory my_first_directory in /tmp.
    
   `10-back`: Changes the working directory to the previous one.
    
   `11-lists`: Lists all files, including hidden files, in the current directory, parent of the working directory, and /boot directory, using long format.
    
   `12-file_type`: Prints the type of the file named iamafile located in the /tmp directory.
    
   `13-symbolic_link`: Creates a symbolic link to /bin/ls, named ls.
    
   `14-copy_html`: Copies HTML files from the current working directory to the parent of the working directory, but only those that did not exist in the parent directory or were newer than the versions in the parent working directory.
    
   `15-lets_move`: Moves all files beginning with an uppercase letter to the directory /tmp/u.
    
   `16-clean_emacs`: Deletes all files in the current working directory that end with the character ~.
    
   `17-tree`: Creates the directories welcome/, welcome/to/, and welcome/to/school in the current directory.
    
   `18-commas`: Lists all files and directories of the current directory, 

separated by commas (,). Directory names end with a slash (/). Files and directories starting with a dot (.) are listed. The listing is alpha-ordered, except for the directories . and .. which are listed at the very beginning. Digits come first.
   
`19 school.mgc`: A magic file that can be used with the file command to detect School data files. School data files always contain the string SCHOOL at offset 0.
