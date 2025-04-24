from google.cloud import secretmanager_v1


def get_project_api_key(
        project_id = "rpgbot-457316",
        secret_id = "GOOGLE_API_KEY",
        version_id = "latest"):

    secret_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    client = secretmanager_v1.SecretManagerServiceClient()
    secret = client.access_secret_version(name = secret_name)

    return secret.payload.data.decode("UTF-8")