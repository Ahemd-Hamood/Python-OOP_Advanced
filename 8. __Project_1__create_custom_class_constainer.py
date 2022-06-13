class TagContent:
    def __init__(self):
        self.tags = {}

    def add(self, val):
        self.tags[val.lower()] = self.tags.get(val.lower(), 0) + 1

    # to get tag key value -> print(self[key])
    def __getitem__(self, item_name):
        return self.tags.get(item_name.lower(), 0)

    # to set tag key value -> self[key] = value
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # to get tags length -> len(self)
    def __len__(self):
        return len(self.tags)

    # to iterate over tags, we use a build-in method called iter() to allow us to iterate at each item inside the tag dictionary
    def __iter__(self):
        return iter(self.tags)

    def increase_tag_count(self, item_name):
        if item_name.lower() in self.tags.keys():
            self.tags[item_name.lower()] = self.tags.get(
                item_name.lower()) + 1
        else:
            print("Tag does not exist")

    def decrease_tag_count(self, item_name):
        if item_name.lower() in self.tags.keys():
            self.tags[item_name.lower()] = self.tags.get(
                item_name.lower()) - 1
        else:
            print("Tag does not exist")

    def remove_tag(self, item_name):
        del self.tags[item_name.lower()]

    def reset_tag(self, item_name):
        if item_name.lower() in self.tags.keys():
            self.tags[item_name] = 0

    def clear_all_tags(self):
        self.tags.clear()


con_1 = TagContent()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Adding new items into tags dictionary
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1.add("JS")
con_1.add("JS")
con_1.add("JS")
con_1.add("jS")
con_1.add("Python")
con_1.add("python")
con_1.add("php")
con_1.add("php")

print(con_1.tags)
# output:
# {
#  'js': 4,
#  'python': 2,
#  'php': 2
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> get tags length, with the the help __len__() magic method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

print("Tags length:", len(con_1))
# output:
# Tags length: 3

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> iterate over tags, with the the help __iter__() magic method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

for key, value in enumerate(con_1):
    print(f"key: {key}, value: {value}")

# output:
# key: 0, value: js
# key: 1, value: python
# key: 2, value: php

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> get tag value by name, with the the help __getitem__() magic method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

result = con_1["python"]

print(result)
# output:
# 2

result = con_1["C#"]
print(result)
# output:
# 0

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Update tag value by name, with the the help __setitem__() magic method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1["js"] = 100
con_1["c#"] = 50  # if key does not exist, here we are going to add it.

print(con_1.tags)
# output:
# {
#  'js': 100,
#  'python': 2,
#  'php': 2,
#  'c#': 50
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> remove tag by name
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1.remove_tag("python")

print(con_1.tags)
# output:
# {
# 'js': 100,
# 'php': 2,
#  'c#': 50
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> decrease tag by -1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1.decrease_tag_count("js")

print(con_1.tags)
# output:
# {
#  'js': 99,
#  'php': 2,
#  'c#': 50
# }

con_1.decrease_tag_count("Ruby")
# Tag does not exist

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> increase tag by +1
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1.increase_tag_count("js")

print(con_1.tags)
# output:
# {
#  'js': 100,
#  'php': 2,
#  'c#': 50
# }

con_1.increase_tag_count("Ruby")
# Tag does not exist

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> reset particular tag to 0
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1.reset_tag("js")

print(con_1.tags)
# output:
# {
#  'js': 0,
#  'php': 2,
#  'c#': 50
# }

# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Clear Tags
# >>>>>>>>>>>>>>>>>>>>>>>>>>>

con_1.clear_all_tags()

print(con_1.tags)
# output:
# { }
