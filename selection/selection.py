import random
import time
import matplotlib.pyplot as plt
import copy

# -------------------------------
# 1. 선택 정렬 구현 + 성능 측정
# -------------------------------
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    # 리스트를 직접 수정하지 않도록 복사
    arr = arr.copy()

    for i in range(n - 1):
        min_idx = i

        # 최소값 찾기
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 필요할 때만 교환
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return comparisons, swaps


# -------------------------------
# 2. 데이터 생성 함수
# -------------------------------
def generate_data(size, data_type):
    if data_type == "random":
        return [random.randint(0, size) for _ in range(size)]

    elif data_type == "sorted":
        return list(range(size))

    elif data_type == "reversed":
        return list(range(size, 0, -1))

    elif data_type == "almost_sorted":
        arr = list(range(size))
        # 10%만 랜덤하게 섞기
        for _ in range(size // 10):
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr


# -------------------------------
# 3. 실험 실행
# -------------------------------
sizes = [100, 500, 1000, 2000]
data_types = ["random", "sorted", "reversed", "almost_sorted"]

results = {}

for data_type in data_types:
    results[data_type] = {
        "time": [],
        "comparisons": [],
        "swaps": []
    }

    for size in sizes:
        total_time = 0
        total_comp = 0
        total_swaps = 0

        # 5번 반복
        for _ in range(5):
            data = generate_data(size, data_type)

            start = time.time()
            comp, swaps = selection_sort(data)
            end = time.time()

            total_time += (end - start)
            total_comp += comp
            total_swaps += swaps

        # 평균값 저장
        results[data_type]["time"].append(total_time / 5)
        results[data_type]["comparisons"].append(total_comp / 5)
        results[data_type]["swaps"].append(total_swaps / 5)


# -------------------------------
# 4. 결과 출력 (표 형태)
# -------------------------------
print("===== 실험 결과 =====")
for data_type in data_types:
    print(f"\n[{data_type}]")
    print("크기 | 시간 | 비교횟수 | 교환횟수")
    for i in range(len(sizes)):
        print(f"{sizes[i]} | {results[data_type]['time'][i]:.5f} | "
              f"{results[data_type]['comparisons'][i]:.0f} | "
              f"{results[data_type]['swaps'][i]:.0f}")


# -------------------------------
# 5. 그래프 생성
# -------------------------------

# 실행 시간 그래프
plt.figure()
for data_type in data_types:
    plt.plot(sizes, results[data_type]["time"], label=data_type)

plt.xlabel("Input Size")
plt.ylabel("Execution Time")
plt.title("Selection Sort - Time")
plt.legend()
plt.savefig("time_graph.png")

# 비교 횟수 그래프
plt.figure()
for data_type in data_types:
    plt.plot(sizes, results[data_type]["comparisons"], label=data_type)

plt.xlabel("Input Size")
plt.ylabel("Comparisons")
plt.title("Selection Sort - Comparisons")
plt.legend()
plt.savefig("comparison_graph.png")

# 교환 횟수 그래프
plt.figure()
for data_type in data_types:
    plt.plot(sizes, results[data_type]["swaps"], label=data_type)

plt.xlabel("Input Size")
plt.ylabel("Swaps")
plt.title("Selection Sort - Swaps")
plt.legend()
plt.savefig("swap_graph.png")

print("\n그래프 이미지가 저장되었습니다!")

