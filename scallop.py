import os


# deafult file descriptor values of standard in and standard out
STDIN_FILE_DESCRIPTOR_DEFAULT = 0
STDOUT_FILE_DESCRIPTOR_DEFAULT = 1


def execute_pipe(pipe_1_tokens, pipe_2_tokens):
        pipe_read, pipe_write = os.pipe()

        # pipe one writes to the pipe write fd rather than standard out
        execute(pipe_1_tokens, fd_swap=(pipe_write, STDOUT_FILE_DESCRIPTOR_DEFAULT))

        # we close the pipe write fd so that we can write to standard out again
        os.close(pipe_write)

        # pipe two reads from pipe read (to read the output of the last step)
        execute(pipe_2_tokens, fd_swap=(pipe_read, STDIN_FILE_DESCRIPTOR_DEFAULT))


def execute(command_tokens, fd_swap=None):
    fork_return_value = os.fork()
    if fork_return_value == 0: # this is the child process
        try:
            if fd_swap: # we redirect file descriptors to connect pipes
                os.dup2(fd_swap[0], fd_swap[1])
            os.execvp(command_tokens[0], command_tokens)
        except OSError as exception:
            print(f"Exception: {exception}")

    else: # this is the parent process
        child_result = os.waitpid(fork_return_value, 0)


def main():
    while True:
        current_directory = os.getcwd()
        userinput = input(f"{current_directory}>> ")
        commands = userinput.split("&&")
        for command in commands:
            if "|" in command:
                pipe_segments = command.split("|")
                tokenized_pipe_segments = [pipe.split() for pipe in pipe_segments]
                execute_pipe(*tokenized_pipe_segments)

            else:
                command_tokens = command.split()
                if command_tokens[0] == "cd": # we don't want to fork to execute cd
                    os.chdir(os.path.abspath(command_tokens[1]))

                else:
                    execute(command_tokens)


if __name__ == "__main__":
    main()
