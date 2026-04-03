import random
import time
import matplotlib.pyplot as plt

# -------------------------------
# 1. 버블 정렬 구현 + 성능 측정
# -------------------------------
def bubble_sort(arr):
    n = len(arr)
    compare_count = 0
    swap_count = 0

    start_time = time.time()

    # 버블 정렬
    for i in range(n):
        swapped = False  # 최적화 (이미 정렬된 경우 조기 종료)
        for j in range(0, n - i - 1):
            compare_count += 1  # 비교 횟수 증가

            if arr[j] > arr[j + 1]:
                # 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True

        if not swapped:
            break

    end_time = time.time()
    elapsed_time = end_time - start_time

    return compare_count, swap_count, elapsed_time


# -------------------------------
# 2. 다양한 데이터 생성 함수
# -------------------------------
def generate_data(size, data_type):
    arr = list(range(size))

    if data_type == "random":
        random.shuffle(arr)

    elif data_type == "sorted":
        pass  # 이미 정렬됨

    elif data_type == "reversed":
        arr.reverse()

    elif data_type == "almost":
        # 90% 정렬 → 일부만 섞기
        for _ in range(size // 10):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]

    return arr


# -------------------------------
# 3. 실험 수행
# -------------------------------
sizes = [100, 500, 1000, 2000]
data_types = ["random", "sorted", "reversed", "almost"]

results = {}

for dtype in data_types:
    results[dtype] = {
        "time": [],
        "compare": [],
        "swap": []
    }

    for size in sizes:
        total_time = 0
        total_compare = 0
        total_swap = 0

        # 5회 반복 평균
        for _ in range(5):
            data = generate_data(size, dtype)
            comp, swap, t = bubble_sort(data.copy())

            total_time += t
            total_compare += comp
            total_swap += swap

        # 평균 계산
        results[dtype]["time"].append(total_time / 5)
        results[dtype]["compare"].append(total_compare / 5)
        results[dtype]["swap"].append(total_swap / 5)


# -------------------------------
# 4. 결과 출력 (표 형태)
# -------------------------------
print("\n===== 실험 결과 =====")
for dtype in data_types:
    print(f"\n[{dtype}]")
    print("크기 | 시간 | 비교 | 교환")
    for i, size in enumerate(sizes):
        print(f"{size} | {results[dtype]['time'][i]:.6f} | {results[dtype]['compare'][i]:.0f} | {results[dtype]['swap'][i]:.0f}")


# -------------------------------
# 5. 그래프 생성
# -------------------------------

def plot_graph(metric, title, filename):
    for dtype in data_types:
        plt.plot(sizes, results[dtype][metric], label=dtype)

    plt.xlabel("Input Size")
    plt.ylabel(metric)
    plt.title(title)
    plt.legend()
    plt.savefig(filename)
    plt.show()
    plt.clf()


plot_graph("time", "Input Size vs Time", "time.png")
plot_graph("compare", "Input Size vs Compare Count", "compare.png")
plot_graph("swap", "Input Size vs Swap Count", "swap.png")