from cv.repository.repository import *


class Pipeline:
    def __init__(self, tasks):
        discover_services()
        self.repository = Repository()
        #self.tasks = tasks
        #self.fetch_task_handler()

    def fetch_task_handler(self):
        self.pipeline = []
        for task in self.tasks:
            service = self.repository.get_service(task['model'])
            service.configure(task['config'])
            self.pipeline.append(service)

    def run(self, image):
        out = image
        for task in self.pipeline:
            out = task.run(out)
        return out

