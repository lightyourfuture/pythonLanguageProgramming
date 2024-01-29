import numpy as np  # 导入NumPy库,用于数组操作
import matplotlib.pyplot as plt  # 导入matplotlib.pyplot,用于绘图
import matplotlib  # 导入matplotlib库,用于全局配置

# 设置字体以支持中文字符
matplotlib.rcParams["font.family"] = "SimHei"

# 在雷达标签中添加一个额外的空标签
radar_labels = np.array(
    ["研究型(I)", "艺术型(A)", "社会型(S)", "企业型(E)", "常规型(C)", "现实型(R)", ""]
)

# 定义数据,每个元素代表一个维度的值
data = np.array(
    [
        [0.40, 0.32, 0.35, 0.30, 0.30, 0.88],
        [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
        [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
        [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
        [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
        [0.34, 0.31, 0.38, 0.40, 0.92, 0.28],
    ]
)

# 定义数据标签
data_labels = ("艺术家", "实验员", "工程师", "推销员", "社会工作者", "记事员")

# 定义角度,将圆平均分成6份
angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)

# 为了使雷达图封闭,需要添加第一个data到data的末尾
data = np.concatenate((data, [data[0]]))

# 为了使雷达图封闭,需要添加第一个angle到angle的末尾
angles = np.concatenate((angles, [angles[0]]))

# 创建一个白色的画布
fig = plt.figure(facecolor="white")

# 添加一个极坐标子图
ax = plt.subplot(111, polar=True)

# 绘制线条,设置线条的颜色,线宽,透明度等
ax.plot(angles, data, "o-", linewidth=1, alpha=0.2)

# 填充颜色,设置透明度
ax.fill(angles, data, alpha=0.25)

# 设置雷达图的角度网格线,并添加标签
ax.set_thetagrids(angles * 180 / np.pi, radar_labels)

# 设置半径网格线的位置
ax.set_rgrids(np.arange(0.2, 1, 0.2), angle=0)

# 设置半径标签的位置
ax.set_rlabel_position(0)

# 在图中添加标题
plt.figtext(0.52, 0.95, "霍兰德人格分析", ha="center", size=20)

# 添加图例,并设置图例的位置和间距
legend = plt.legend(data_labels, loc=(0.94, 0.80), labelspacing=0.1)

# 设置图例的字体大小
plt.setp(legend.get_texts(), fontsize="large")

# 显示网格线
plt.grid(True)

# 保存图像
plt.savefig("HollandRadarDraw.png")

# 显示图像
plt.show()
