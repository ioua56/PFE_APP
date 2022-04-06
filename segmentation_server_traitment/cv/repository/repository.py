from threading import Lock
import os
import fnmatch


def discover_services():
    matches = []
    dir_path = os.path.realpath('.')
    root_folder = "cv"
    for root, _, filenames in os.walk(dir_path):
        for filename in fnmatch.filter(filenames, '*.py'):
            if os.path.basename(root) == "services" and filename != "__init__.py":
                matches.append(os.path.join(root, filename))
    print(matches)            
    rel_files = [file[len(dir_path) + 1:] for file in matches]
    modules = [rel_file.replace('/', '.')[:-3] for rel_file in rel_files]
    print("this is modules"+ str(modules))
    imported_mods = [__import__(module) for module in modules]
    print(imported_mods)



class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Repository(metaclass=SingletonMeta):
    def __init__(self):
        self.services = {}
        
    def register(self, service, instance):
        class_name = type(instance).__name__
        _instance = self.get_service(class_name)
        if _instance is None:
            task = {
                'name': class_name,
                'instance': instance
            }
            if service in self.services:
                self.services[service].append(task)
            else:
                self.services[service] = [task]

        
    def lookup_all(self):
        return self.services
    def available_services_html(self):
        list_modelname=self.services.values()
        list_names=[]
        for element in list_modelname:
            list_names.append(element[0]['name'])
            
        

        return list_names
    def available_services(self):
        return list(self.services.keys())
    
    # return a list of services that represent the main task
    def get_services_by_name(self, service):
        if service in self.services:
            return self.services[service]
        else:
            return []
    

    # return the service by name
    def get_service(self, service):
        for service_name in self.available_services():
            tasks = self.get_services_by_name(service_name)
            for task in tasks:
                if task['name'] == service:
                    return task['instance']
        return None

