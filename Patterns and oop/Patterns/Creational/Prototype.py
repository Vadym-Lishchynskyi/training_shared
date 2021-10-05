"""
The prototype pattern is useful when one needs to create objects based on existing object by using a cloning technique.

As you may have guessed, the idea is to use a copy of that object's complete structure to produce the new object. We
will see that this is almost natural in Python because we have a copy feature that helps greatly in using this
technique.

Pros and cons:
+ less TIME consuming
  let's us make an object with the same data much !!!FASTER!!! then to make it by __new__ and __init__
+ for copying the object responsible the same object. In such way it has access to all hidden methods and attributes.
+ less code for creating new objects
+ don't depend on the class of the object

Use cases:
- when code shouldn't depend on the class of objects that must be copied
"""
import copy


class SelfReferenceEntity:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class SomeComponent:
    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    def __copy__(self):
        """
        Поверхностное копирование. Этот метод будет вызван когда кто-либо вызывает метод
        'copy.copy' с этим обьектом и возвращаемое значение будет поверхностным копированием
        """
        # First, let's create copies of the nested objects
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        # Then let's clone the object itself, using the prepared clones of the nested objects.

        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo={}):    # `memo` in accordance to documentation helps us get rid of circular references.
        """
        Глубокое копирование. Этот метод будет вызван когда кто-либо вызывает метод
        'copy.deepcopy' с этим обьектом и возвращаемое значение будет глубоким копированием
        """

        # First, let's create copies of the nested objects
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        # Then let's clone the object itself, using the prepared clones of the nested objects.
        new = self.__class__(
            self.some_int, some_list_of_objects, some_circular_ref
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == '__main__':

    "copy() method implementation testing"
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferenceEntity()
    component = SomeComponent(32, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    # shallow_copied_component = copy.copy(component)
    #
    # # Let's change some element in shallow_copied_component and see if it changes in component.
    # shallow_copied_component.some_list_of_objects.append('new object')
    # if component.some_list_of_objects[-1] == 'new object':
    #     print(
    #         'Adding elements to `shallow_copied_component`s '
    #         'list_of_objects adds it to `components`s '
    #         'list_of_objects.'
    #     )

    "deepcopy() method implementation testing"
    deep_copied_component = copy.deepcopy(component)

    # Let's change some element in deep_copied_component and see if it changes in component.
    deep_copied_component.some_list_of_objects.append('one more object')
    if component.some_list_of_objects[-1] == 'one more object':
        print(
            'Adding elements to `deep_copied_component`s '
            'list_of_objects adds it to `components`s '
            'list_of_objects.'
        )
