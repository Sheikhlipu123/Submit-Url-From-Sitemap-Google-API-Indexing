# Submit Pages from Sitemap

This Python script submits pages from a sitemap to the Google Indexing API. It uses OAuth2 authentication and the `oauth2client` library.

## Prerequisites

- Python 3.x
- `oauth2client` library
- Google Indexing API key

## Obtaining Google Indexing API Key

To use this script, you need to obtain an API key for the Google Indexing API. Here are the steps to obtain the API key:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the Google Indexing API for your project.
4. Create a service account key and download the JSON key file.
5. Save the downloaded JSON key file as `your.json` in the same directory as the script.

Make sure the service account associated with the API key has the necessary permissions to access and use the Google Indexing API.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
