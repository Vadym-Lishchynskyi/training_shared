"""

A little bit of theory

Situation:
Imagine that we want to create an object that is composed of multiple parts and the composition needs to be done step
by step. The object is not complete unless all its parts are fully created. That's where the builder design pattern
can help us.

How it works:
The builder pattern separates the construction of a complex object from its representation. By keeping
the construction separate from the representation, the same construction can be used to create several different
representations (https://sourcemaking.com/design_patterns/builder).

Practical example:
A practical example can help us understand what the purpose of the builder pattern is. Suppose
that we want to create an HTML page generator. The basic structure (construction part) of an HTML page is always the
same: it begins with <html> and finishes with </html>, inside the HTML section are the <head> and </head> elements,
inside the head section are the <title> and </title> elements, and so forth. But the representation of the page can
differ. Each page has its own title, its own headings, and different <body> contents. Moreover, the page is usually
built in steps: one function adds the title, another adds the main heading, another the footer, and so on. Only after
the whole structure of a page is complete can it be shown to the client using a final render function. We can take it
even further and extend the HTML generator so that it can generate totally different HTML pages. One page might
contain tables, another page might contain image galleries, yet another page contains the contact form, and so on.

The HTML page generation problem can be solved using the builder pattern. In this pattern, there are two main
participants:

The builder: The component responsible for creating the various parts of a complex object. In this example,
these parts are the title, heading, body, and the footer of the page. The director: The component that controls the
building process using a builder instance. It calls the builder's functions for setting the title, the heading,
and so on. And, using a different builder instance allows us to create a different HTML page without touching any of
the code of the director.


We can also find software examples:

- The HTML example that was mentioned at the beginning of the chapter is actually used by django-widgy (
https://wid.gy/), a third-party tree editor for Django that can be used as a content management system (CMS). The
django-widgy editor contains a page builder that can be used for creating HTML pages with different layouts.
- The django-query-builder library (https://github.com/ambitioninc/django-query-builder) is another third-party Django
library that relies on the builder pattern. This library can be used for building SQL queries dynamically,
allowing you to control all aspects of a query and create a different range of queries, from simple to very complex
ones.


Difference with factory patterns:
1) At this point, the distinction between the builder pattern and the factory
pattern might not be very clear. The main difference is that a factory pattern creates an object in a single step,
whereas a builder pattern creates an object in multiple steps, and almost always through the use of a director.

2)Another difference is that while a factory pattern returns a created object immediately, in the builder pattern the
client code explicitly asks the director to return the final object when it needs it.


Use cases, pros and cons:

We use the builder pattern for creating an object in situations where using the factory pattern (either a factory
method or an abstract factory) is not a good option. A builder pattern is usually a better candidate than a factory
pattern when the following applies:

We want to create a complex object (an object composed of many parts and created in different steps that might need
to follow a specific order). Different representations of an object are required, and we want to keep the
construction of an object decoupled from its representation. We want to create an object at one point in time,
but access it at a later point.

"""


class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None    # in gigabytes
        self.gpu = None

    def __str__(self):
        info = (f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}')
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (self.builder.configure_memory(memory),
                 self.builder.configure_hdd(hdd),
                 self.builder.configure_gpu(gpu))
        [step for step in steps]

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500,
                                memory=8,
                                gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)


if __name__ == '__main__':
    main()


# Things to add

"""The basic changes are the introduction of a builder, ComputerBuilder, a director, HardwareEngineer, 
and the step-by-step construction of a computer, which now supports different configurations (notice that memory, 
hdd, and gpu are parameters and are not preconfigured). What do we need to do if we want to support the construction 
of tablets? Implement this as an exercise. 

You might also want to change the computer's serial_number into something that is different for each computer, 
because as it is now, it means that all computers will have the same serial number (which is impractical). """