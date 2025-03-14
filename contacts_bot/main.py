import colorama

colorama.init()

success = colorama.Fore.GREEN
fail = colorama.Fore.RED
reset = colorama.Fore.RESET  

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_valid_name(name):
    return name.isalpha()  

def is_valid_phone(phone):
    return phone.isdigit()  

def add_contact(args, contacts):
    try:
        name, phone = args
        if not is_valid_name(name):
            return f"{fail}Invalid name. Use only letters.{reset}"
        if not is_valid_phone(phone):
            return f"{fail}Invalid phone number. Use only digits.{reset}"

        contacts[name] = phone
        return f"{success}Contact {name} added.{reset}"
    
    except ValueError:
        return f"{fail}Give me name and phone please. Example: add John 1234567890{reset}"
    except Exception as e:
        return f"{fail}Unexpected error: {str(e)}{reset}"

def change_contact(args, contacts):
    try:
        name, phone = args
        if not is_valid_name(name):
            return f"{fail}Invalid name. Use only letters.{reset}"
        if not is_valid_phone(phone):
            return f"{fail}Invalid phone number. Use only digits.{reset}"

        if name not in contacts:
            return f"{fail}Contact {name} not found.{reset}"

        contacts[name] = phone
        return f"{success}Contact {name} updated.{reset}"
    
    except ValueError:
        return f"{fail}Give me name and phone please. Example: change John 1234567890{reset}"
    except Exception as e:
        return f"{fail}Unexpected error: {str(e)}{reset}"

def show_all(contacts):
    if not contacts:
        return f"{fail}No contacts added yet.{reset}"
    
    res = f"{success}All contacts:{reset}"
    for name, phone in contacts.items():
        res += f"\n - {name}: {phone}"
    return res

def main():
    contacts = {}
    print(f"\n{success}Hello! Welcome to the assistant bot!{reset}\n")
    
    while True:
        try:
            user_input = input("Enter a command: ").strip()
            if not user_input:
                print(f"{fail}Please enter a command.{reset}")
                continue

            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(f"{success}Good bye!{reset}")
                break
            
            elif command == "hello":
                print(f"{success}How can I help you?{reset}")
                
            elif command == "add":
                if len(args) < 2:
                    print(f"{fail}Give me name and phone please. Example: add John 1234567890{reset}")
                    continue
                print(add_contact(args, contacts))
                
            elif command == "change":
                if len(args) != 2:
                    print(f"{fail}Give me name and phone please. Example: change John 1234567890{reset}")
                    continue
                print(change_contact(args, contacts))
                
            elif command == "all":
                print(show_all(contacts))
                
            else:
                print(f"{fail}Invalid command.{reset}")

        except KeyboardInterrupt:
            print(f"\n{fail}Program interrupted. Exiting...{reset}")
            break
        except Exception as e:
            print(f"{fail}Unexpected error: {str(e)}{reset}")

if __name__ == "__main__":
    main()
