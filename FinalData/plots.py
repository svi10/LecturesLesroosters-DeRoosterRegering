
"""
plt.suptitle("")
ax.set_title("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(False)
"""


import matplotlib.pyplot as plt
import numpy as np

"""
Load Data
"""
# Random
random10000 = np.loadtxt("FinalData/Random10000_MP.csv")
random10000_ana = np.loadtxt("FinalData/Random10000_analysis.csv")

random10000_ana = [round(i / 10000) for i in random10000_ana]
print(f"Ana: {random10000_ana}")

# Random hillclimber
ranhill100 = np.loadtxt("FinalData/RandomHillclimber100_MP.csv")
ranhill10 = np.loadtxt("FinalData/RandomHillclimber10_MP.csv")
print(f"MIN: {min(ranhill10)}")

ranhill100_ana = np.loadtxt("FinalData/RandomHillclimber100_Analysis.csv")
ranhill10_ana = np.loadtxt("FinalData/RandomHillclimber10_Analysis.csv")

# Normalize to 1
ranhill100_ana = [round(i / 100) for i in ranhill100_ana]
ranhill10_ana = [round(i / 10) for i in ranhill10_ana]


# Greedy
gre = 864 # Always this amount
greana = np.loadtxt("FinalData/Greedy_analysis.csv")

# Greedy Hillclimber
grehill100 = np.loadtxt("FinalData/GreedyHillclimber100_MP.csv")
grehill10 = np.loadtxt("FinalData/GreedyHillclimber10_MP.csv")

print(f"MIN2: {min(grehill10)}")

grehill100_ana = np.loadtxt("FinalData/GreedyHillclimber100_Analysis.csv")
grehill10_ana = np.loadtxt("FinalData/GreedyHillclimber10_Analysis.csv")

grehill100_ana = [round(i / 100) for i in grehill100_ana]
grehill10_ana = [round(i / 10) for i in grehill100_ana]


"""
Random 1000x
"""
fig, ax = plt.subplots(figsize=(6,5))

avg1 = round(sum(random10000) / len(random10000))
best1 = round(min(random10000))
std2 = round(np.std(random10000))

# Random
plt.suptitle("Random 10000 keer",fontsize=16)
ax.set_title(f"Gem. random: {avg1} MP", fontsize=12)
ax.set_xlabel("Strafpunten", fontsize=14)
ax.set_ylabel("Norm. Frequentie", fontsize=14)
ax.set_xlim(0, 3000)
ax.set_ylim(0, 0.0022)
ax.grid(False)
# Turn off tick labels
# ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.locator_params(axis='y', nbins=2)
ax.set_yticklabels([0,0.5,1])


binwidth = 40
# ax.hist([random10000, ranhill100], normed=True)
ax.hist(random10000, bins=np.arange(min(random10000), max(random10000) + binwidth, binwidth), density=True, color='blue', label='Random')
ax.axvline(best1, linewidth=2, color='limegreen', label=f'Rand. Beste: {best1}', linestyle='--')
# ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True)
ax.legend(loc='upper left')
fig.savefig("FinalData/Plots/Random1000.png")


"""
Random Hillclimber
"""
plt.clf()
fig, ax = plt.subplots(figsize=(6,5))

avg2 = round(sum(ranhill100) / len(ranhill100))
best2 = round(min(ranhill100))
std2 = round(np.std(ranhill100))

# Random
plt.suptitle("Random & Hillclimber",fontsize=16)
ax.set_title(f"Gem. random: {avg1} MP   Gem. hillclimber {avg2} MP", fontsize=12)
ax.set_xlabel("Strafpunten", fontsize=14)
ax.set_ylabel("Norm. Frequentie", fontsize=14)
ax.set_xlim(0, 3000)
ax.set_ylim(0, 0.0040)
ax.grid(False)
# Turn off tick labels
# ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.locator_params(axis='y', nbins=2)
ax.set_yticklabels([0,0.5,1])


binwidth = 40
# ax.hist([random10000, ranhill100], normed=True)
ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True, color='darkviolet', label='Hillclimber')
ax.hist(random10000, bins=np.arange(min(random10000), max(random10000) + binwidth, binwidth), density=True, color='blue', label='Random')
ax.axvline(best2, linewidth=2, color='orange', label=f'Hill. Beste: {best2}', linestyle='--')
ax.axvline(best1, linewidth=2, color='limegreen', label=f'Rand. Beste: {best1}', linestyle='--')
# ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True)
ax.legend(loc='upper right')
fig.savefig("FinalData/Plots/ranhill100.png")


"""
Greedy 
"""

"""
Random Hillclimber
"""
plt.clf()
fig, ax = plt.subplots(figsize=(6,5))

avg2 = round(sum(ranhill100) / len(ranhill100))
best2 = round(min(ranhill100))
std2 = round(np.std(ranhill100))

# Random
plt.suptitle("Greedy",fontsize=16)
ax.set_title(f"Greedy: {gre} MP   Gem. random: {avg2} MP   Gem. hillclimber {avg2} MP", fontsize=12)
ax.set_xlabel("Strafpunten", fontsize=14)
ax.set_ylabel("Norm. Frequentie", fontsize=14)
ax.set_xlim(0, 3000)
ax.set_ylim(0, 0.0040)
ax.grid(False)
# Turn off tick labels
# ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.locator_params(axis='y', nbins=2)
ax.set_yticklabels([0,0.5,1])


binwidth = 40
# ax.hist([random10000, ranhill100], normed=True)
# ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True, color='darkviolet', label='Hillclimber')
# ax.hist(random10000, bins=np.arange(min(random10000), max(random10000) + binwidth, binwidth), density=True, color='blue', label='Random')
ax.axvline(best2, linewidth=2, color='orange', label=f'Hill. Beste: {best2}', linestyle='--')
ax.axvline(best1, linewidth=2, color='limegreen', label=f'Rand. Beste: {best1}', linestyle='--')
ax.axvline(gre, linewidth=3, color='darkblue', label=f'Greedy: {gre}', linestyle='-')
# ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True)
ax.legend(loc='upper right')
fig.savefig("FinalData/Plots/Greedy.png")


"""
Greedy Hillclimber
"""
plt.clf()
fig, ax = plt.subplots(figsize=(6,5))

avg3 = round(sum(grehill100) / len(grehill100))
best3 = round(min(grehill100))
std3 = round(np.std(grehill100))

# Random
plt.suptitle("Greedy",fontsize=16)
ax.set_title(f"Gem. Greedy: {avg3} MP   Gem. random: {avg1} MP   Gem. hillclimber {avg2} MP", fontsize=10)
ax.set_xlabel("Strafpunten", fontsize=14)
ax.set_ylabel("Norm. Frequentie", fontsize=14)
ax.set_xlim(0, 3000)
ax.set_ylim(0, 0.0040)
ax.grid(False)
# Turn off tick labels
# ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
ax.locator_params(axis='y', nbins=2)
ax.set_yticklabels([0,0.5,1])


binwidth = 40
# ax.hist([random10000, ranhill100], normed=True)
# ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True, color='darkviolet', label='Hillclimber')
# ax.hist(random10000, bins=np.arange(min(random10000), max(random10000) + binwidth, binwidth), density=True, color='blue', label='Random')
ax.hist(grehill100, bins=np.arange(min(grehill100), max(grehill100) + binwidth, binwidth), density=True, color='magenta', label='Greedy Hill.')
ax.axvline(best2, linewidth=2, color='orange', label=f'Hill. Beste: {best2}', linestyle='--')
ax.axvline(best1, linewidth=2, color='limegreen', label=f'Rand. Beste: {best1}', linestyle='--')
ax.axvline(gre, linewidth=3, color='darkblue', label=f'Greedy: {gre}', linestyle='--')
ax.axvline(best3, linewidth=2, color='black', label=f'Greedy Beste: {best3}', linestyle='-')
# ax.hist(ranhill100, bins=np.arange(min(ranhill100), max(ranhill100) + binwidth, binwidth), density=True)
ax.legend(loc='upper right')
fig.savefig("FinalData/Plots/GreedyHillclimber.png")

"""
Waar komen de maluspunten toch vandaan?
"""

plt.clf()
fig, ax = plt.subplots(figsize=(10,5))

labels = ["Capaciteit", "Avond", "Conflict", "Tussenuren"]
x = np.arange(len(labels))
width=0.20

bar1 = ax.bar(x - width, random10000_ana, width, label='Random', color='blue')
bar2 = ax.bar(x - 0, ranhill100_ana, width, label='Random Hillclimber', color='darkorange')
bar3 = ax.bar(x + width, greana, width, label='Greedy', color='green')
bar4 = ax.bar(x + 2 * width, grehill100_ana, width, label='Greedy Hillclimber', color='deeppink')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Strafpunten', fontsize=16)
ax.set_title('Strafpunten per type', fontsize=18)
ax.set_xticks(x, labels, fontsize=16)
ax.legend(fontsize=14)

ax.bar_label(bar1, padding=0.5, fontsize=12)
ax.bar_label(bar2, padding=0.5, fontsize=12)
ax.bar_label(bar3, padding=0.5, fontsize=12)
ax.bar_label(bar4, padding=0.5, fontsize=12)

fig.savefig("FinalData/Plots/MaluspuntenVergelijking2.png")
