import sys
import os
from vimeo_uploader.index import upload
from path.index import process_path


# Get all arguments
args = sys.argv

try:
  # Call to get help
  if args[1] == "--help" and len(args) == 2:
    os.system('type help.txt')

  # Call to upload video 
  elif args[1] == "upload" and args[2] == "-m" and len(args) == 3:
    response = upload()
    print(response)

  # Call to show credentials
  elif args[1] == "show" and args[2] == "cred" and len(args) == 3:
    os.system('type .env')

  # Call to initialize app
  elif args[1] == "init" and len(args) == 2:
    os.system('type credentials.txt')
    identifier = input("client identifier: ")
    token = input("access token: ")
    secret = input("client secret: ")

    # lists of commands to execute
    commands = [
      f'echo CLIENT_ID={identifier} > .env',
      f'echo ACCESS_TOKEN={token}  >> .env',
      f'echo CLIENT_SECRET={secret} >> .env'
    ]

    # Execute commands
    for c in commands:
      os.system(c)

    os.system('echo Credentials taken.')

  # Call to set filepath
  elif args[1] == "set" and args[2] == "path" and len(args) == 3:
    # Process input path
    file_path = process_path(input("file path: "))

    # Store filepath in .env file
    os.system(f'echo FILE_PATH={file_path} >> .env')

    os.system('echo File path taken.')

  # If a call is not recognized send error msg
  else:
    os.system('echo Invalid format or command. Enter [ vimeo --help ] to get help.')


except KeyboardInterrupt:
  print()

except IndexError:
  os.system('echo Invalid format or command. Enter [ vimeo --help ] to get help.')
