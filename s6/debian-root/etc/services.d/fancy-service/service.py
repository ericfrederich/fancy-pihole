#!/usr/bin/env python3

import re
import shlex
from subprocess import check_call

from bottle import request, route, run


@route("/block", method="PUT")
def block():
    if request.json.get("secret") != "HARD_CODED_SECRET":
        return

    args = []
    for site in request.json.get("sites", []):
        args.append(r"(^|\.)" + re.escape(site) + "$")

    cmd = ["pihole", "--regex"] + args

    print(" ".join(shlex.quote(c) for c in cmd))
    check_call(cmd)


@route("/unblock", method="PUT")
def unblock():
    if request.json.get("secret") != "HARD_CODED_SECRET":
        return

    args = []
    for site in request.json.get("sites", []):
        args.append(r"(^|\.)" + re.escape(site) + "$")

    cmd = ["pihole", "-b", "-d", "--regex"] + args

    print(" ".join(shlex.quote(c) for c in cmd))
    check_call(cmd)


if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, debug=True)
