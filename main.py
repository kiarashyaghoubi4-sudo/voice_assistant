from assistant import Assistant

assistant = Assistant()

while True:

    assistant.wake()

    command = assistant.listen()

    assistant.execute(command)

    assistant.sleep()