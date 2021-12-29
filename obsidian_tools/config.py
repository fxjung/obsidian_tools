import keyring
from getpass import getpass

if (
        api_key := keyring.get_password(
            service_name="obsidian_tools_google_api_key", username=""
        )
) is None:
    print("Enter Google API Key below:")
    api_key = getpass("API Key: ")
    keyring.set_password(
        service_name="obsidian_tools_google_api_key",
        username='',
        password=api_key,
    )
    print("Password successfully saved to the system keyring.")
