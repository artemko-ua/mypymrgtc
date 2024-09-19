const int outputPin = 13;  // Пін для виводу сигналу Морзе
String message = "привіт";  // Повідомлення для закодування

String morseTable[] = {
  ".-", "-...", ".--", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", 
  "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "..-.", "...-", ".--", "-..-", "-.--", "--..", ".-.-", "-.-.", "---.", "--..", "..-..", "......", "..--..", "-.-.--", "-..-.", "-.--.", "-.--.-"
};

char ukrainianChars[] = {
  'а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', ' ', '.', ',', '?', '!', '/', '(', ')'
};

void setup() {
  Serial.begin(9600);  // Початок серійної передачі даних
  pinMode(outputPin, OUTPUT); // Налаштування піну як вихід для передачі Морзе
}

void loop() {
  String morseCode = encodeToMorse(message);
  Serial.println("Закодоване повідомлення в Морзе: " + morseCode);
  
  // Відправка повідомлення через заданий пін
  sendMorse(morseCode);
  
  delay(10000);  // Очікування 10 секунд перед наступним повідомленням
}

// Функція для закодування тексту в Морзе
String encodeToMorse(String text) {
  String morse = "";
  int charCount = sizeof(ukrainianChars) / sizeof(ukrainianChars[0]);
  for (int i = 0; i < text.length(); i++) {
    char c = text[i];
    for (int j = 0; j < charCount; j++) {
      if (c == ukrainianChars[j]) {
        morse += morseTable[j];
        morse += " ";  // Додаємо пробіл між символами Морзе
        break;
      }
    }
  }
  return morse;
}

// Функція для відправки Морзе через світлодіод або звуковий сигнал
void sendMorse(String morseCode) {
  for (int i = 0; i < morseCode.length(); i++) {
    if (morseCode[i] == '.') {
      digitalWrite(outputPin, HIGH);
      delay(200);  // Тривалість короткого сигналу
      digitalWrite(outputPin, LOW);
      delay(200);  // Пауза між сигналами
    } else if (morseCode[i] == '-') {
      digitalWrite(outputPin, HIGH);
      delay(600);  // Тривалість довгого сигналу
      digitalWrite(outputPin, LOW);
      delay(200);
    } else if (morseCode[i] == ' ') {
      delay(600);  // Пауза між літерами
    }
  }
}