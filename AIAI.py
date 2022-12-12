import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.api_key)

start_sequence = "\nA:"
restart_sequence = "\n\nQ:"

contin = True

while contin:
    prompt = input(restart_sequence)
    if prompt == "quit":
        break
    else:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            print(start_sequence, response["choices"][0]["text"].strip())
        except Exception as exc:
            print(exc)


# javascript to Python
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="code-davinci-002",
#   prompt="#JavaScript to Python:\nJavaScript: \ndogs = [\"bill\", \"joe\", \"carl\"]\ncar = []\ndogs.forEach((dog) {\n    car.push(dog);\n});\n\nPython:",
#   temperature=0,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )


# JavaScript 助手聊天机器人
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#     model="code-davinci-002",
#     prompt="You: How do I combine arrays?\nJavaScript chatbot: You can use the concat() method.\nYou: How do you make an alert appear after 10 seconds?\nJavaScript chatbot",
#     temperature=0,
#     max_tokens=60,
#     top_p=1.0,
#     frequency_penalty=0.5,
#     presence_penalty=0.0,
#     stop=["You:"],
# )

# 用人类可理解的语言解释一段Python代码。
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="code-davinci-002",
#   prompt="# Python 3 \ndef remove_common_prefix(x, prefix, ws_prefix): \n    x[\"completion\"] = x[\"completion\"].str[len(prefix) :] \n    if ws_prefix: \n        # keep the single whitespace as prefix \n        x[\"completion\"] = \" \" + x[\"completion\"] \nreturn x \n\n# Explanation of what the code does\n\n#",
#   temperature=0,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0
# )


# 解释代码
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="code-davinci-002",
#   prompt="class Log:\n    def __init__(self, path):\n        dirname = os.path.dirname(path)\n        os.makedirs(dirname, exist_ok=True)\n        f = open(path, \"a+\")\n\n        # Check that the file is newline-terminated\n        size = os.path.getsize(path)\n        if size > 0:\n            f.seek(size - 1)\n            end = f.read(1)\n            if end != \"\\n\":\n                f.write(\"\\n\")\n        self.f = f\n        self.path = path\n\n    def log(self, event):\n        event[\"_event_id\"] = str(uuid.uuid4())\n        json.dump(event, self.f)\n        self.f.write(\"\\n\")\n\n    def state(self):\n        state = {\"complete\": set(), \"last\": None}\n        for line in open(self.path):\n            event = json.loads(line)\n            if event[\"type\"] == \"submit\" and event[\"success\"]:\n                state[\"complete\"].add(event[\"id\"])\n                state[\"last\"] = event\n        return state\n\n\"\"\"\nHere's what the above class is doing:\n1.",
#   temperature=0,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\"\"\""]
# )


# 将 JavaScript 函数转换为单行。
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="code-davinci-002",
#   prompt="Use list comprehension to convert this into one line of JavaScript:\n\ndogs.forEach((dog) => {\n    car.push(dog);\n});\n\nJavaScript one line version:",
#   temperature=0,
#   max_tokens=60,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=[";"]
# )


# 计算时间复杂度
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="def foo(n, k):\naccum = 0\nfor i in range(n):\n    for l in range(k):\n        accum += i\nreturn accum\n\"\"\"\nThe time complexity of this function is",
#   temperature=0,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\n"]
# )


#
# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="pr",
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
