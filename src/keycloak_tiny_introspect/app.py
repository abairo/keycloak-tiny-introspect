import os
import requests


class KeycloakClient:
    def __init__(self, client_id: str, client_secret: str, realm: str):
        self._client_id = client_id
        self._client_secret = client_secret
        self._ream = realm

    def _well_known(self) -> dict:
        url = os.environ.get("KEYCLOAK_HOST")
        response = requests.get(url)
        return response.json()

    def introspect(self, token: str, username: str):
        url = os.environ.get("KEYCLOAK_INTROSPECTION_URL")
        data = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "username": username,
            "token": token,
        }
        response = requests.post(url, data)
        return None


def get_keycloak_client() -> KeycloakClient:
    client_id = os.environ.get("KEYCLOAK_CLIENT_ID")
    client_secret = os.environ.get("KEYCLOAK_CLIENT_SECRET")
    realm = os.environ.get("KEYCLOAK_REALM")
    return KeycloakClient(client_id=client_id, client_secret=client_secret, realm=realm)


def load_env_vars(file_path):
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key] = value.strip().replace('"', "")


if __name__ == "__main__":
    load_env_vars(".env")
    token = os.environ.get("TOKEN_TEST")
    username = "62518288031"
    keycloak_client = get_keycloak_client()
    keycloak_client._well_known()
    keycloak_client.introspect(token, username)
