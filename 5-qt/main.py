# -*- coding: utf-8 -*-
"""
Главный файл приложения для анализа текста
"""

import sys
import re
from collections import Counter
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtCore import Qt, QTimer
from ui_main_window import Ui_MyMainWindow


class TextAnalyzer:
    """Класс для анализа текста"""

    @staticmethod
    def count_words(text):
        """Подсчет слов в тексте"""
        words = re.findall(r'\b\w+\b', text.lower())
        return len(words)

    @staticmethod
    def count_characters(text):
        """Подсчет символов в тексте (с пробелами и без)"""
        total_chars = len(text)
        chars_no_spaces = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
        return total_chars, chars_no_spaces

    @staticmethod
    def count_sentences(text):
        """Подсчет предложений в тексте"""
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

    @staticmethod
    def count_paragraphs(text):
        """Подсчет абзацев в тексте"""
        paragraphs = [p for p in text.split('\n') if p.strip()]
        return len(paragraphs)

    @staticmethod
    def most_common_words(text, n=10):
        """Поиск самых частых слов"""
        words = re.findall(r'\b\w+\b', text.lower())
        common_words = Counter(words).most_common(n)
        return common_words

    @staticmethod
    def analyze_text(text):
        """Полный анализ текста"""
        if not text.strip():
            return {
                'error': 'Введите текст для анализа'
            }

        try:
            word_count = TextAnalyzer.count_words(text)
            total_chars, chars_no_spaces = TextAnalyzer.count_characters(text)
            sentence_count = TextAnalyzer.count_sentences(text)
            paragraph_count = TextAnalyzer.count_paragraphs(text)
            common_words = TextAnalyzer.most_common_words(text, 5)

            # Рассчитываем среднюю длину слова
            avg_word_length = round(chars_no_spaces / word_count, 2) if word_count > 0 else 0

            # Рассчитываем среднюю длину предложения в словах
            avg_sentence_length = round(word_count / sentence_count, 2) if sentence_count > 0 else 0

            return {
                'word_count': word_count,
                'total_chars': total_chars,
                'chars_no_spaces': chars_no_spaces,
                'sentence_count': sentence_count,
                'paragraph_count': paragraph_count,
                'avg_word_length': avg_word_length,
                'avg_sentence_length': avg_sentence_length,
                'common_words': common_words,
                'error': None
            }
        except Exception as e:
            return {
                'error': f'Ошибка анализа: {str(e)}'
            }


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация UI
        self.ui = Ui_MyMainWindow()
        self.ui.setupUi(self)

        # Настройка окна
        self.setWindowTitle("Анализатор текста v1.0")

        # Настройка элементов интерфейса
        self.setup_ui()

        # Подключение сигналов
        self.connect_signals()

        # Инициализация анализатора
        self.analyzer = TextAnalyzer()

        # Таймер для автоматического обновления
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.on_text_changed)
        self.update_timer.setInterval(1000)  # 1 секунда

    def setup_ui(self):
        """Дополнительная настройка UI элементов"""
        # Настройка текстовых полей
        self.ui.plainTextEdit.setPlaceholderText("Введите текст для анализа...")
        self.ui.textBrowser.setReadOnly(True)

        # Установка стилей
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPlainTextEdit {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QPushButton {
                background-color: #4CAF50;
                color: black;
                border: none;
                padding: 8px 16px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QTextBrowser {
                background-color: white;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QLabel {
                font-weight: bold;
                color: #333333;
            }
        """)

    def connect_signals(self):
        """Подключение обработчиков событий"""
        # Кнопка анализа
        self.ui.pushButton_2.clicked.connect(self.analyze_text)

        # Автоматический анализ при изменении текста
        self.ui.plainTextEdit.textChanged.connect(self.start_auto_update)

        # Контекстное меню для текстового поля
        self.ui.plainTextEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.plainTextEdit.customContextMenuRequested.connect(self.show_text_context_menu)

    def start_auto_update(self):
        """Запуск таймера для автоматического обновления"""
        self.update_timer.start()

    def on_text_changed(self):
        """Обработчик изменения текста (вызывается по таймеру)"""
        if self.ui.plainTextEdit.toPlainText():
            self.analyze_text()
        else:
            self.ui.textBrowser.clear()
        self.update_timer.stop()

    def analyze_text(self):
        """Основная функция анализа текста"""
        text = self.ui.plainTextEdit.toPlainText()

        if not text.strip():
            self.ui.textBrowser.setPlainText("Введите текст для анализа")
            return

        try:
            # Анализ текста
            result = self.analyzer.analyze_text(text)

            if result.get('error'):
                self.ui.textBrowser.setPlainText(result['error'])
                return

            # Формирование отчета
            report = self.generate_report(result)
            self.ui.textBrowser.setPlainText(report)

            # Статистика в заголовке окна
            char_count = result['total_chars']
            word_count = result['word_count']
            self.setWindowTitle(f"Анализатор текста - {word_count} слов, {char_count} символов")

        except Exception as e:
            self.ui.textBrowser.setPlainText(f"Ошибка при анализе текста: {str(e)}")

    def generate_report(self, result):
        """Генерация форматированного отчета"""
        report = f"""=== ОСНОВНАЯ СТАТИСТИКА ===
Слов: {result['word_count']:,}
Символов (всего): {result['total_chars']:,}
Символов (без пробелов): {result['chars_no_spaces']:,}
Предложений: {result['sentence_count']:,}
Абзацев: {result['paragraph_count']:,}

=== СРЕДНИЕ ЗНАЧЕНИЯ ===
Средняя длина слова: {result['avg_word_length']} символов
Средняя длина предложения: {result['avg_sentence_length']} слов

=== ЧАСТОТНЫЙ АНАЛИЗ ===
"""

        # Добавляем самые частые слова
        if result['common_words']:
            report += "Самые частые слова:\n"
            for word, count in result['common_words']:
                report += f"  '{word}': {count} раз\n"
        else:
            report += "Не удалось определить частые слова\n"

        # Дополнительная информация
        report += f"\n=== ДОПОЛНИТЕЛЬНО ===\n"
        report += f"Плотность текста: {result['word_count'] / max(1, result['paragraph_count']):.1f} слов/абзац\n"

        return report

    def show_text_context_menu(self, position):
        """Показ контекстного меню для текстового поля"""
        from PySide6.QtWidgets import QMenu, QAction
        from PySide6.QtGui import QClipboard

        menu = self.ui.plainTextEdit.createStandardContextMenu()

        # Добавляем дополнительные действия
        menu.addSeparator()

        clear_action = QAction("Очистить поле", self)
        clear_action.triggered.connect(self.ui.plainTextEdit.clear)
        menu.addAction(clear_action)

        paste_action = QAction("Вставить и проанализировать", self)
        paste_action.triggered.connect(self.paste_and_analyze)
        menu.addAction(paste_action)

        menu.exec_(self.ui.plainTextEdit.mapToGlobal(position))

    def paste_and_analyze(self):
        """Вставка текста из буфера обмена и его анализ"""
        clipboard = QApplication.clipboard()
        text = clipboard.text()

        if text:
            self.ui.plainTextEdit.setPlainText(text)
            self.analyze_text()

    def keyPressEvent(self, event):
        """Обработка нажатий клавиш"""
        # Ctrl+Enter для анализа
        if event.key() == Qt.Key_Return and (event.modifiers() & Qt.ControlModifier):
            self.analyze_text()
        # Ctrl+C для копирования результата
        elif event.key() == Qt.Key_C and (event.modifiers() & Qt.ControlModifier):
            if self.ui.textBrowser.hasFocus():
                self.ui.textBrowser.copy()
        # Ctrl+A для выделения всего текста
        elif event.key() == Qt.Key_A and (event.modifiers() & Qt.ControlModifier):
            if self.ui.plainTextEdit.hasFocus():
                self.ui.plainTextEdit.selectAll()
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event):
        """Обработка закрытия окна"""
        reply = QMessageBox.question(
            self,
            'Подтверждение',
            'Вы уверены, что хотите выйти?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    """Точка входа в приложение"""
    app = QApplication(sys.argv)

    # Настройка стиля приложения
    app.setStyle('Fusion')

    # Создание и показ главного окна
    window = MainWindow()
    window.show()

    # Запуск приложения
    sys.exit(app.exec())


if __name__ == "__main__":
    main()