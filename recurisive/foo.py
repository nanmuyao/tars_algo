from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter

config = Config()
# config.trace_filter = GlobbingFilter(exclude=[
#     '_find_and_load',
#     '_find_and_load.*', # Tried a few similar variations
#     '_handle_fromlist',
#     '_handle_fromlist.*',
# ])


config.trace_filter = GlobbingFilter(include=['__main__'])


def run():
    with PyCallGraph(output=GraphvizOutput(), config=config):
        for i in range(3):
            print(i)
            run()


def foo_recursive(n):
    if n == 0:
        return 0
    return foo_recursive(n-1) + n



# foo_depth(n) = 计算n层的深度 
def foo_depth(n):
    if n == 0 or n == 1:
        return n
    
    return foo_depth(n-1) + 1
    


if __name__=="__main__":
    # foo_recursive(3)
    print(foo_depth(10))