Processes and signals 

In this project, I explored process management and signals in Linux, utilizing commands like ps, pgrep, pkill, exit, and trap. Here's a concise overview of the tasks:

Tasks 📃

    0-what-is-my-pid: Displays the PID of the current Bash script.
    
    1-list_your_processes: Lists currently running processes, including those without a TTY, in a user-oriented hierarchy.
    
    2-show_your_bash_pid: Displays lines containing the keyword "bash" from the processes listed in task 1.
    
    3-show_your_bash_pid_made_easy: Displays the PID and process name of processes containing "bash" in their names.
    
    4-to_infinity_and_beyond: Displays "To infinity and beyond" indefinitely with a 2-second interval.
    
    5-kill_me_now: Kills the process from task 4 using the kill command.
    
    6-kill_me_now_made_easy: Kills the process from task 4 using pkill.
    
    7-highlander: Repeats "To infinity and beyond" with a 2-second interval and displays "I am invincible!!!" upon receiving a SIGTERM signal.
    
    8-beheaded_process: Kills the process from task 7.
    
    100-process_and_pid_file: Creates a PID file and displays "To infinity and beyond" indefinitely, responding to various signals.
    
    101-manage_my_process: Manages the process from task 100, starting, stopping, or restarting it based on arguments.
    
    102-zombie.c: A C program that creates five zombie processes and displays their PIDs.
