import json
import matplotlib.pyplot as plt


with open('memory_usage.json', 'r') as f:
    data = json.load(f)


methods = list(data.keys())
memory_times = [info['memory'] for info in data.values()]


plt.figure(figsize=(10, 6))


plt.bar(methods, memory_times)
plt.xlabel('Métodos')
plt.ylabel('Tiempo de memoria')
plt.title('Uso de memoria por método')


plt.xticks(rotation=90)


plt.tight_layout()

plt.show()
