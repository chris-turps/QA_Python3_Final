import json

def generic_show(command):
    return \
        [
          {
            "jsonrpc": "2.0",
            "method": "cli",
            "params": {"cmd": "show " + command,
              "version": 1
            },
            "id": 1,
            "rollback": "rollback-on-error"
          }
        ]