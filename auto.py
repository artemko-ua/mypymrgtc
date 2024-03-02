import time
from pynput.mouse import Button, Controller

mouse = Controller()

# Затримка перед початком виконання
time.sleep(5)

# Виконання автокліку
end_time = time.time() + 15  # 15 секунд
while time.time() < end_time:
    mouse.click(Button.left, 1)
    time.sleep(0.01)  # Затримка 10 мілісекунд між кожним кліком
