class Pipeline():
    commands = ['test_cpu', 'test_gpu']
    split_commands = ['test_cpu']
    gpu_commands = ['test_gpu']

    def __init__(self, config, tmp_dir):
        self.config = config
        self.tmp_dir = tmp_dir

    def test_cpu(self, split_ind=0, num_splits=1):
        print(self.config)

    def test_gpu(self):
        print(self.config)
