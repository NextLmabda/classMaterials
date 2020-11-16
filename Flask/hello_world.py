import luigi

class HelloTask(luigi.Task):
    def run(self):
        with open('hello.txt', 'w') as hello_file:
            hello_file.write('Hello')
            hello_file.close()

if __name__ == '__main__':
    luigi.build()
'''
class MyTask1(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=0)

    def run(self):
        print(self.x + self.y)


class MyTask2(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=1)
    z = luigi.IntParameter(default=2)

    def run(self):
        print(self.x * self.y * self.z)


if __name__ == '__main__':
    luigi.build([MyTask1(x=10), MyTask2(x=15, z=3)])
'''