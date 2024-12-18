from deepdiff import DeepDiff


def diff(a, b):
    return DeepDiff(a, b, ignore_order=True)

print(diff({'a': 1, 'b': 2}, {'b': 2, 'a': 1}))
print(diff({'a': 1, 'b': 2}, {'b': 2, 'a': 1, 'c': 3}))
print(diff({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'a': 1}))
print(diff({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'a': 1, 'c': 4}))
print(diff({'a': 1, 'b': 2, 'c': 3}, {'b': 2, 'a': 1, 'c': 3}))

# people = ['Jane', 'Kate', 'Christopher', 'Fiona']
people = [
    {
        'name': 'Jane',
        'age': 21,
        'stack': 'full',
        'tags': ['developer', 'poet'],
        'address': {
            'street': 'Cornelia St',
            'state': 'New York'
        }
    },
    {
        'name': 'Kate',
        'age': 21,
        'stack': 'full',
        'tags': ['developer', 'hunter'],
        'address': {
            'street': 'Maple St',
            'state': 'California'
        }
    },
    {
        'name': 'Christopher',
        'age': 21,
        'stack': 'design',
        'tags': ['figma'],
        'address': {
            'street': 'D-10 Main St',
            'state': 'Florida'
        }
    },
    {
        'name': 'Fiona',
        'age': 21,
        'stack': 'people',
        'tags': ['poet', 'HR'],
        'address': {
            'street': 'RE-10 Junction',
            'state': 'Pennsylvania'
        }
    }
]


newJane = {
    'name': 'Jane',
    'age': 21,
    'stack': 'full',
    'tags': ['developer', 'poet', 'hunter'],
    'address': {
        'street': 'Cornelia St',
        'state': 'Delaware'
    }
}

print(diff(people[0], newJane))