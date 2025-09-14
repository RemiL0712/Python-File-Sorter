# ============================================================================
# Професійний сортувальник файлів
# Цей скрипт сортує файли в папці за їх типом та генерує звіт.
# ============================================================================

import os
import shutil

# Словник, що відображає розширення файлів на назви папок.
# Це робить код гнучким і легко розширюваним.
FILE_TYPES = {
    'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Code': ['.py', '.js', '.html', '.css'],
    'Other': []  # Для всіх інших файлів
}

def create_folders(base_path):
    """Створює необхідні папки, якщо вони ще не існують."""
    for folder_name in FILE_TYPES.keys():
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Створено папку: '{folder_path}'")

def sort_files(folder_path):
    """Сортує файли у вказаній папці за їх типом."""
    if not os.path.isdir(folder_path):
        print(f"Помилка: Шлях '{folder_path}' не існує або не є папкою.")
        return

    # Ініціалізуємо лічильники для звіту
    counts = {folder: 0 for folder in FILE_TYPES}

    # Створюємо необхідні папки
    create_folders(folder_path)

    # Отримуємо всі файли та папки в директорії
    all_files_and_folders = os.listdir(folder_path)

    for item_name in all_files_and_folders:
        current_path = os.path.join(folder_path, item_name)

        # Пропускаємо папки, які ми самі створили, та основний скрипт
        if os.path.isdir(current_path) or item_name == 'main.py':
            continue

        try:
            # Визначаємо розширення файлу
            file_name, file_extension = os.path.splitext(item_name)
            file_extension = file_extension.lower()

            # Визначаємо цільову папку
            target_folder = 'Other'
            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    target_folder = folder
                    break
            
            # Вказуємо шлях призначення
            destination_path = os.path.join(folder_path, target_folder, item_name)
            
            # Переміщуємо файл
            shutil.move(current_path, destination_path)
            print(f'Переміщено "{item_name}" до "{target_folder}"')
            counts[target_folder] += 1
            
        except FileNotFoundError:
            print(f"Помилка: Файл '{item_name}' не знайдено.")
        except Exception as e:
            print(f"Помилка при обробці файлу '{item_name}': {e}")

    # Фінальний звіт
    print('\n--- ЗВІТ ПРО СОРТУВАННЯ ---')
    for folder, count in counts.items():
        if count > 0:
            print(f"Переміщено до '{folder}': {count} файл(ів)")
    print('---------------------------')

if __name__ == "__main__":
    print("Автоматичний сортувальник файлів.")
    # Користувач вводить шлях до папки для сортування
    path_to_sort = input("Введіть повний шлях до папки, яку потрібно відсортувати: ")
    sort_files(path_to_sort)
    