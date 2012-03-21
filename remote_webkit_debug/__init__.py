try:
    import json
except ImportError:
    import simplejson as json
import httplib2
import websocket

__version__ = (0, 0, 1)

class ChromeShell(object):
    def __init__(self, host='localhost', port=9222):
        self.host = host
        self.port = port

    def get_tabs(self):
        headers, content = httplib2.Http().request('http://{0}:{1}/json'.format(
                self.host, self.port))
        return json.loads(content)

    def pick_tab(self, tab_info):
        ws_url = tab_info['webSocketDebuggerUrl']
        return ChromeTab(websocket.create_connection(ws_url))


class ChromeTab(object):
    def __init__(self, ws):
        self.ws = ws
        self.cmd_id = 1

    def send_command(self, command, **params):
        payload = {
            'id': self.cmd_id,
            'method': command,
            'params': params
            }
        self.ws.send(json.dumps(payload))
        self.cmd_id += 1
        return json.loads(self.ws.recv())

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.ws.close()
