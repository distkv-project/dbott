
import ray

import dexecutor.DExecutor as DExecutor
import dmonitor.DMonitor as DMonitor


@ray.remote
class DMaster(object):

    def __init__(self, init_num_executors, init_num_monitors):
        self._init_num_executors = init_num_executors
        self._init_num_monitors = init_num_monitors

        # init executors.
        self._executors = {}
        for i in range(0, self._init_num_executors):
            executor_actor_handle = DExecutor.remote()
            self._executors[executor_actor_handle._ray_actor_id] = executor_actor_handle

        # init monitors
        self._monitors = {}
        for i in range(0, self.init_num_monitors):
            repo_name = "dst-project/drpc"
            monitor_actor_handle = DMonitor.remote(monitor_actor_handle)
            self._executors[repo_name] = monitor_actor_handle

    def start(self):
        pass
