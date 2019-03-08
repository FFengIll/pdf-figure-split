# 目标
快速的，自动的将包含多张图的单一pdf，
拆解为多个独立的pdf，每个pdf仅包含一张图用于latex等用作引用。

# 场景
- 不打算一一打印图表，一次性打印为一个pdf，包含多个图
- 确定好图的caption，ref
  - 写成config
  - 且与pdf每一页对应
  - 配置为csv格式，每一行对应每一页，无用的页对应空行，或者''
- 自动拆分pdf，并输出
  - 每一张图一个pdf文件，文件名为ref
  - 输出所有的对应latex语句（template.tex）中可以修改

# 使用
- python3 -m pip install PyPDF2
- python3 splitor.py -t figure.tex -c figure.csv testcase.pdf
- python3 splitor.py -t table.tex -c table.csv testcase.pdf
  - 请选用需要分割的pdf文件
  - 如需要，请对应修改tex模板
  - 请对应pdf，填写csv文件（直接文本编辑，或在excel中编辑皆可）
  - 因为实际使用时，图表是分开的，所以分为了两套