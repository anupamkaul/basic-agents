from pathlib import Path

parent_dir = Path("..")
env_path = parent_dir / ".env"

if env_path.exists() and env_path.is_file():
    print(".env file found.")

    # Read the contents of the .env file
    with env_path.open("r") as env_file:
        contents = env_file.readlines()

    key_exists = any(line.startswith("OPENAI_API_KEY=") for line in contents)
    good_key = any(line.startswith("OPENAI_API_KEY=sk-proj-") for line in contents)
    classic_problem = any("OPEN_" in line for line in contents)
    
    if key_exists and good_key:
        print("SUCCESS! OPENAI_API_KEY found and it has the right prefix")
    elif key_exists:
        print("Found an OPENAI_API_KEY although it didn't have the expected prefix sk-proj- \nPlease double check your key in the file..")
    elif classic_problem:
        print("Didn't find an OPENAI_API_KEY, but I notice that 'OPEN_' appears - do you have a typo like OPEN_API_KEY instead of OPENAI_API_KEY?")
    else:
        print("Didn't find an OPENAI_API_KEY in the .env file")
else:
    print(".env file not found in the llm_engineering directory. It needs to have exactly the name: .env")
    
    possible_misnamed_files = list(parent_dir.glob("*.env*"))
    
    if possible_misnamed_files:
        print("\nWarning: No '.env' file found, but the following files were found in the llm_engineering directory that contain '.env' in the name. Perhaps this needs to be renamed?")
        for file in possible_misnamed_files:
            print(file.name)
