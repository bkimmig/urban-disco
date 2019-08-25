# urban-disco
Segment Recommender Application

(Sorry about the name - it was a github recommendation and it actually seemed
fitting/better than what I can come up with).

## Set Up

1. `make`
2. `touch docker-compose.override.yml`
  - Add following block of code with your strava api credentials.
```
version: '3.3'

services:
  app:
    environment: &appenv
    # you will need to override any confidential information in the
    # docker-compose.override.yml - otherwise put environment vars here
      DEBUG: True
      STRAVA_CLIENT_ID: # your id here
      STRAVA_CLIENT_SECRET: # your secret here
```
3. `docker-compose up` (add `-d` to detach)
4. Go to http://0.0.0.0:8888/ and check the site... 
