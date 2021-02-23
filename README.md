# Fancy Pihole

Modified pihole image which runs a little webservice to block/unblock sites.

Inspired by [NetworkChuck's video](https://www.youtube.com/watch?v=dH3DdLy574M)

While this image was published to DockerHub the source code was not.
This made it impossible to update the version of pihole that was running.

## Improvements over original

* The original Python script would not start automatically.  This script is ran via the same [`s6` stuff]() that the underlying pihole is using, so even if it crashes it'll restart.

* The original script had hard coded sites; this takes a list of sites as a parameter

* The original script had no security token
