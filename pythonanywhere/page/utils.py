import pandas as pd
import numpy as np
df = pd.read_excel("data/df_output.xlsx")
df.drop(df.columns[[0]], axis=1, inplace=True)


df2 = df.pivot_table(index=['SenderCompID','Error Type','MsgType','Flow Category','ExDestination','OrderSide','OrderType','TimeInForce'], aggfunc='size')
df2 = df2.reset_index()
df2.columns = ['49','Error Type','35','10200','100','40','54','59','Count']

html_2 = df2.to_html()
#write html to file
text_file_2 = open("templates/error_count.html", "w")
text_file_2.write(html_2)
text_file_2.close()

df3 = df.pivot_table(index=['Error Type'],columns=['MsgType'],aggfunc='size')
df3 = df3.replace(np.nan, 0)
df3 = df3.reset_index()


html_3 = df3.to_html()
#write html to file
text_file_3 = open("templates/MsgType.html", "w")
text_file_3.write(html_3)
text_file_3.close()

df4 = df.pivot_table(index=['Error Type'],columns=['Flow Category'],aggfunc='size')
df4 = df4.replace(np.nan, 0)


import matplotlib.pyplot as plt
import matplotlib
print(df4)
colors = ["#b84592", "#5ecc62"]

df_4 = df4.loc[:,['DSA','DMA']].plot.bar(stacked=True, color=colors, figsize=(5,3.5))
plt.title('Error Occurrence In Different FlowCategory Values')
plt.xlabel('Error Types')
plt.ylabel('Occurrence')
plt.show()
df4 = df4.reset_index()
html_4 = df4.to_html()
#write html to file
text_file_4 = open("templates/FlowCategory.html", "w")
text_file_4.write(html_4)
text_file_4.close()

df_x = df
df_x.columns = ['49','Error Type','35','10200','100','40','54','59']

html_1 = df_x.to_html()
#write html to file
text_file_1 = open("templates/error_type.html", "w")
text_file_1.write(html_1)
text_file_1.close()