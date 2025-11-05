def parse_input(user_input):
    """Splits user command into a command and arguments."""
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:]
    return command, args