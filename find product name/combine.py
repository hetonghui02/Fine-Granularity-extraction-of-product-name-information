import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel("包.xlsx")

# 读取第二个Excel文件
df2 = pd.read_excel("时装.xlsx")

# 读取第三个Excel文件
df3 = pd.read_excel("香水.xlsx")

# 合并数据
combined_df = pd.concat([df1, df2, df3], ignore_index=True)

# 保存合并后的Excel文件
combined_df.to_excel("item_name.xlsx", index=False)
print("合并完成并保存为 item_name.xlsx 文件。")
