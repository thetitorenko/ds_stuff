import pandas as pd
from sklearn import metrics


# Словарь скоров классификации
proj_scores = {
    'Model': [], 'Subset': [], 'Accuracy': [],
    'Precision': [], 'Recall': [], 'F1 score': [],
    'Duration': []}


# Функция для подсчета метрик классификации
def get_metrics(y_true, y_pred, model_name, subset, round_digits, time, horiz_line=False):
    # Подсчет метрик
    accuracy_score = metrics.accuracy_score(y_true, y_pred)
    precision_score = metrics.precision_score(y_true, y_pred)
    recall_score = metrics.recall_score(y_true, y_pred)
    f1_score = metrics.f1_score(y_true, y_pred)

    # Логирование метрик в словарь
    proj_scores['Model'].append(model_name)
    proj_scores['Subset'].append(subset)
    proj_scores['Accuracy'].append(accuracy_score)
    proj_scores['Precision'].append(precision_score)
    proj_scores['Recall'].append(recall_score)
    proj_scores['F1 score'].append(f1_score)
    proj_scores['Duration'].append(time)

    # Вывод
    if horiz_line: print('-'*40)
    print(f'{model_name} {subset} Accuracy score {round(accuracy_score, round_digits)}')
    print(f'{model_name} {subset} Precision score {round(precision_score, round_digits)}')
    print(f'{model_name} {subset} Recall score {round(recall_score, round_digits)}')
    print(f'{model_name} {subset} F1 score {round(f1_score, round_digits)}')


# Подсветка максимальных, минимальных и переобучения
def highlight_values(series):
    # Работаем только с числовыми данными
    if pd.api.types.is_numeric_dtype(series):

        # Раскраска для признака времени
        if series.name == 'Duration':
            # Создать серию с параметром True для нужно значения в столбце и False для остальных
            is_max = series == series.max()
            is_min = series == series.min()

            # Применяем стили на основе заданных условий
            styles = []
            for max_val, min_val in zip(is_max, is_min):
                if min_val:
                    styles.append('font-weight: bold; color: green')
                elif max_val:
                    styles.append('font-weight: bold; color: red')
                else:
                    styles.append('')
            return styles

        # Раскраска для других чисел
        else: 
            # Создать серию с параметром True для нужно значения в столбце и False для остальных
            is_max = series == series[series != 1].max()
            is_min = series == series.min()
            is_value_one = series == 1

            # Применяем стили на основе заданных условий
            styles = []
            for max_val, min_val, is_value_one in zip(is_max, is_min, is_value_one):
                if max_val and not is_value_one:
                    styles.append('font-weight: bold; color: green')
                elif is_value_one:
                    styles.append('font-weight: bold; color: yellow')
                elif min_val:
                    styles.append('font-weight: bold; color: red')
                else:
                    styles.append('')
            return styles

    # Возвращается пустой список для нечисловых столбцов
    else: return [''] * len(series)
