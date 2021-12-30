import logging
import keyring
from getpass import getpass

log = logging.getLogger(__name__)


if (
    api_key := keyring.get_password(
        service_name="obsidian_tools_google_api_key", username=""
    )
) is None:
    print("Enter Google API key below:")
    api_key = getpass("API key: ")
    keyring.set_password(
        service_name="obsidian_tools_google_api_key",
        username="",
        password=api_key,
    )
    print("API key successfully saved to the system keyring.")
