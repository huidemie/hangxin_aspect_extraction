import json
import os
import time


true_positive = 0
positive = 0  # TP + TN
total_num = 0  # TP + FN
false_positive = 0
# wrong_file = open(os.path.join(result_path, 'wrong.json'), 'w', encoding='utf-8')
with open('result.txt', 'r', encoding='utf-8') as f:
    last_content = 'a'
    kong = set()
    predict_label = set()
    true_label = set()
    for line in f.readlines():
        rs_line = json.loads(line.strip())
        content = rs_line['content']
        if content != last_content:
            if (true_label & predict_label) != kong:
                true_positive += 1
            else:
                false_positive += 1
            total_num += 1
            positive += len(predict_label)
            predict_label = set()
            true_label = set()
            true_label.add(rs_line['true_label'])
        for i in rs_line['pred_label']:
            predict_label.add(i)
        last_content = content
precision = 100.0 * true_positive / positive
recall = 100.0 * true_positive / total_num
F1 = 2 * precision * recall / (precision + recall)
print('Results: right:%d wrong:%d model find:%d total:%d' % (true_positive, false_positive, positive, total_num))
print('Metrics: Precision:%.3f Recall:%.3f F1:%.3f' % (precision, recall, F1))
print(time.asctime(time.localtime(time.time())))
