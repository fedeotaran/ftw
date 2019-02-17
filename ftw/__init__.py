import abc
from collections import namedtuple


class Condition(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.data = None

    @abc.abstractmethod
    def execute(self, data):
        pass

    def add_context(self, data):
        self.data = data
        return self

    def __nonzero__(self):
        return self.execute(self.data)


class Action(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass

    def __call__(self, **kwargs):
        return self.execute(**kwargs)


Option = namedtuple('Option', ['conditions', 'method'])


class Dispatcher(object):
    options = []

    @classmethod
    def dispatch(cls, data):

        if not cls.options:
            raise Exception("There is no options added!")

        try:
            method = next(
                option.method
                for option in cls.options
                if cls.match(option.conditions, data)
            )
        except StopIteration:
            raise Exception("This input doesn't match with any action")

        return method(**data)

    @classmethod
    def match(cls, conditions, data):
        return all(cond.add_context(data) for cond in conditions)

    @classmethod
    def options_from_dict(cls, options):
        cls.options = [Option(**option) for option in options]

    @classmethod
    def add_option(cls, conditions=None, method=None):
        cls.options.append(Option(conditions=conditions, method=method))
