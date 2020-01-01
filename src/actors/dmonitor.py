
import ray


@ray.remote
class DMonitor(object):
    def __init__(self, repo_name):
        self._repo_name = repo_name
