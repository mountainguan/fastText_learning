import jieba
import fastText

input="东莞理工学院"

text = jieba.cut_for_search(input)
text = " ".join(text)

classify = fastText.load_model("model/classify.model")
result = classify.predict(text)

print(result)