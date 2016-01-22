from kubernetes.models.v1.Container import Container


class K8sContainer(object):
    def __init__(self, model=None, name=None, image=None):
        if model is not None:
            self.model = Container(model=model)
        else:
            if name is None or image is None:
                raise SyntaxError('You must provide a name and image')
            else:
                self.model = Container(name=name, image=image)

    def add_port(self, container_port, host_port, name, protocol='TCP'):
        assert isinstance(container_port, int)
        assert isinstance(host_port, int)
        assert isinstance(name, str)
        assert isinstance(protocol, str)
        self.model.add_port(container_port=container_port, host_port=host_port, name=name, protocol=protocol)
        return self

    def add_env(self, k, v):
        assert isinstance(k, str)
        assert isinstance(v, str)
        self.model.add_env(name=k, value=v)
        return self

    def add_volume_mount(self, name, mount_path, read_only=False):
        assert isinstance(name, str)
        assert isinstance(mount_path, str)
        assert isinstance(read_only, bool)
        self.add_volume_mount(name=name, mount_path=mount_path, read_only=read_only)
        return self

    def get(self):
        return self

    def get_liveness_probe(self):
        return self.model.get_liveness_probe()

    def get_model(self):
        return self.model

    def get_readiness_probe(self):
        return self.model.get_readiness_probe()

    def set_arguments(self, args):
        assert isinstance(args, list)
        self.model.set_arguments(args=args)
        return self

    def set_command(self, cmd):
        assert isinstance(cmd, list)
        self.model.set_command(cmd=cmd)
        return self

    def set_host_network(self, mode):
        assert isinstance(mode, bool)
        self.model.set_host_network(mode=mode)
        return self

    def set_image(self, image):
        assert isinstance(image, str)
        self.model.set_image(image=image)
        return self

    def set_liveness_probe(self, **kwargs):
        self.model.set_liveness_probe(**kwargs)
        return self

    def set_name(self, name):
        assert isinstance(name, str)
        self.set_name(name=name)
        return self

    def set_privileged(self, mode):
        assert isinstance(mode, bool)
        self.model.set_privileged(mode=mode)
        return self

    def set_pull_policy(self, policy):
        assert isinstance(policy, str)
        self.model.set_pull_policy(policy=policy)
        return self

    def set_readiness_probe(self, **kwargs):
        self.model.set_readiness_probe(**kwargs)
        return self

    def set_requested_resources(self, cpu, mem):
        assert isinstance(cpu, float)
        assert isinstance(mem, str)
        self.model.set_requested_resources(cpu=cpu, mem=mem)
        return self

    def set_limit_resources(self, cpu, mem):
        assert isinstance(cpu, float)
        assert isinstance(mem, str)
        self.model.set_limit_resources(cpu=cpu, mem=mem)
        return self
