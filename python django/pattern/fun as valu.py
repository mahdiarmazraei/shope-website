def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

print(greeting("Atlantis")())

# Output: Hello, Atlantis!