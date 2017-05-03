# cozmo-object-recognition
This project used google cloud vision api

1. activate virtual env
2. get start with Cozmo SDK
```brew update```
- Once Homebrew is installed and updated, type the following into the Terminal window to install the latest version of Python 3:
```brew install python3```
- Install SDK
```pip3 install --user 'cozmo[camera]'```
-update SDK
```pip3 install --user --upgrade cozmo```

3. install google api
```pip install --upgrade google-cloud-vision```
- install google cloud SDK
```--upgrade google-cloud-vision```
－ install google cloud tool, download [sdk here](https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-153.0.0-darwin-x86_64.tar.gz). Add sdk tools to your path and run
```./google-cloud-sdk/install.sh```
-initialize sdk
```./google-cloud-sdk/bin/gcloud init```
-get authenticated with the Google Cloud SDK
```gcloud auth application-default login```

