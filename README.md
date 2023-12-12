## Overview (Patched)

The POC demonstrates how an attacker could use the JWT instance ID to hijack session tokens of Electron applications, specifically when the application communicates with certain APIs, Ps - Please make sure to change the session cookie or it will return "Failed to get recent online user"

## How It Works

- ElectronUI.exe initiates with two command-line arguments which appear to include the user's HWID (Hardware ID).
- These hashes are sent to a verify API endpoint.
- Electron is tied to Bloxflip, a gambling platform.
- The vulnerability lies in an open endpoint that exposes the instance IDs of all verified users.
- By replicating the process, an attacker can generate a matching instance ID and log in as the user without needing the corresponding HWID.

## Key Points

- **Instance ID Vulnerability**: The exposed endpoint allows an attacker to obtain the instance IDs of active users.
- **JWT Decoding**: With the Instance ID, an attacker can use it as a private key to decrypt the JWT token sent to the verified endpoint.

## Steps to Reproduce

1. Observe the creation of `ElectronUI.exe` and extract the command line arguments.
2. Identify the verify API endpoint.
3. Access the open endpoint that lists current user instance IDs.
4. Replicate the process and create a hash (Instance ID) to authenticate as the user.

## Screenshots

- Here is a screenshot of the hashes being sent. The second hash is of particular importance:
  
  ![Hashes being sent](https://github.com/l4tt/electron_hijacker_poc/assets/97377137/a443deeb-32f4-45d8-b58b-72d7f8f3f701)

- This image shows the API verifying the InstanceID and authenticating successfully:
  
  ![API verifying InstanceID](https://github.com/l4tt/electron_hijacker_poc/assets/97377137/619d00fc-991f-42f2-ace7-4d364e62b2d9)

- This image shows the API listing all InstanceID's and running users that have verified on electron:

  ![image](https://github.com/l4tt/electron_hijacker_poc/assets/97377137/2c7d57a2-899d-4ff1-acd0-4ca63251e248)


## Demonstration Video

- Watch the live demonstration of the POC in 4K resolution:
  
  [POC Demonstration Video](https://discord.com/channels/1183726286275883008/1183728400733569064/1183926494498668564)

