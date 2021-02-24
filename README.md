# Fancy Pihole

Modified pihole image which runs a little webservice to block/unblock sites.

This can be used, for instance, with [IFTTT](https://ifttt.com/)

## Origins

This was inspired by [NetworkChuck's "BLOCK EVERYTHING w/ PiHole on Docker, OpenDNS and IFTTT" video](https://www.youtube.com/watch?v=dH3DdLy574M)

While the image was published to DockerHub the source code was not.
This made it impossible to update the version of pihole that was running.

Hence, this repo was made.

## Differences original

* The Python server would not start automatically.  This image's server integrates with the already present [S6 Overlay](https://github.com/just-containers/s6-overlay) that is used to run pihole itself.  This means if the python server process crashes for any reason it'll get restarted.

* The original had hard coded sites in .sh files; this takes a list of sites as a parameter.  This means you can edit the sites on ifttt or wherever you're making the API calls from.

* The original script had no security token.  Since the API needs to be called from over the internet (i.e. from ifttt) it should some some security.  Run with `-e FANCY_SERVICE_SECRET=xxxx`

* Uses `PUT` instead of `GET`

## Example

Make sure you're using `PUT` instead of `GET`.  The body should look something like this:

```json
{"secret":"the_fancy_service_secret", "sites":["youtube.com", "netflix.com", "hulu.com"]}
```
