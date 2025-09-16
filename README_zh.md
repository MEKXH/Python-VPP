# Python-VPP

基于 [ORC](https://www.orc.org/index.asp?id=21) 气动和水动力模型的 3 自由度速度预测程序。
请查看托管在 [https://yacht-vpp.streamlit.app/](https://yacht-vpp.streamlit.app/) 的演示，并去试航！

## 使用代码

要使用代码，请首先克隆或下载此存储库，然后安装所需的依赖项（见下文）。
使用的主要文件是 `runVPP.py` 和 `righting_moment.json`。这些文件必须填入您的船只数据。默认情况下，它们使用 YD-41（来自《游艇设计原理》）。
VPP 通过以下命令运行。

```bash
python runVPP.py
```

代码运行后，应生成以下图表（或类似的图表）
<p align="center">
    <img src="Figure.png" alt="YD-41 VPP results" width="1024">
</p>
请参阅 [文档](https://marinlauber.github.io/Python-VPP/)。

### 输入变量

以下是 VPP 中使用的关键变量列表。

1. 附体 :
    * Cu : 根弦长 / 上弦长 (m)
    * Cl : 尖弦长 / 下弦长 (m)
    * Span : 展长 (m)
1. 游艇 :
    * Lwl : 水线长 (m)
    * Vol : 船体排水体积 (m^3)
    * Bwl : 水线宽 (m)
    * Tc : 船体吃水 (m)
    * WSA : 湿表面积 (m^2)
    * Tmax : 最大吃水，即龙骨 (m)
    * Amax : 最大剖面面积 (m^2)
    * Mass : 游艇总质量，包括龙骨 (kg)
    * Ff : 艏部干舷高度 (m)
    * Fa : 艉部干舷高度 (m)
    * Boa : 全宽 (m)
    * Loa : 全长 (m)
    * App : 附体列表
    * Sails : 船帆列表
1. 船帆:
    标准测量，但 Roach 定义为 1-A/(0.5PE)
    风筝帆仅取面积和 vce 估计值（这很粗略）
1. VPP.set_analysis()
    * TWA range : 使用的 TWA 范围
    * TWS range : TWS 范围，必须在 [2, 35] 之间

## 贡献

我们非常希望看到代码、文档和功能开发方面的贡献！
当您做出贡献时，请确保任何新功能都有额外的测试覆盖。
请按照以下步骤为本项目做出贡献。

### 安装依赖项

从 `requirements.txt` 文件安装所需的依赖项。
如果使用 `pip`，则 `pip install requirements.txt`。
如果使用 `conda`，请按照以下步骤创建具有正确依赖项的环境：

```bash
conda create --name Python-VPP \
    && conda config --add channels conda-forge \
    && conda activate Python-VPP \
    && conda install -y --file requirements.txt
```

### 运行测试

测试使用 [pytest](https://docs.pytest.org/en/8.0.x/) 实现。
您可以使用以下命令运行测试

```bash
pytest -vv
```

您可以通过运行 `benchmark.py` 脚本针对 WinVPP 的 YD-41 结果运行基准测试。

```bash
python benchmark/benchmark.py -g -o
```

## 致谢

* **[Otto Villani](https://www.linkedin.com/in/otto-villani-552760108/)** - *初始想法，模型选择* - [GitHub](https://github.com/ottovillani)
* **[Marin Lauber](https://www.linkedin.com/in/marin-lauber/)** - *初始想法，开发* - [GitHub](https://github.com/marinlauber)
* **[Thomas Dickson](https://tajd.co.uk/about)** - *开发者* - [GitHub](http://github.com/TAJD)

## 许可证

本项目根据 MIT 许可证授权 - 有关详细信息，请参阅 [LICENSE](LICENSE) 文件
