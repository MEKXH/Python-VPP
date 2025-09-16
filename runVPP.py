# -*- coding: utf-8 -*-
import numpy as np

import logging

logging.basicConfig(level=logging.INFO)

from src.SailMod import Jib, Kite, Main
from src.VPPMod import VPP
from src.YachtMod import Keel, Rudder, Yacht

YD41 = Yacht(
    Name="YD41",
    Lwl=11.90,
    Vol=6.05,
    Bwl=3.18,
    Tc=0.4,
    WSA=28.20,
    Tmax=2.30,
    Amax=1.051,
    Mass=6500,
    Ff=1.5,
    Fa=1.5,
    Boa=4.2,
    Loa=12.5,
    App=[Keel(Cu=1.00, Cl=0.78, Span=1.90), Rudder(Cu=0.48, Cl=0.22, Span=1.15)],
    Sails=[
        Main("MN1", P=16.60, E=5.60, Roach=0.1, BAD=1.0),
        Jib("J1", I=16.20, J=5.10, LPG=5.40, HBI=1.8),
        Kite("A2", area=150.0, vce=9.55),
        Kite("A5", area=75.0, vce=2.75),
    ],
)

# NHtest = Yacht(
#     Name="NHtest",
#     Lwl=15.4,
#     Vol=16.2,
#     Bwl=,     # 未知
#     Tc=,       # 未知
#     WSA=,    # 未知
#     Tmax=2.50,
#     Amax=,   # 未知
#     Mass=16600,
#     Ff=,       # 未知
#     Fa=,       # 未知
#     Boa=,      # 未知
#     Loa=15.98,
#     App=[Keel(Cu=, Cl=, Span=), Rudder(Cu=, Cl=, Span=)],   # 未知
#     Sails=[
#         Main("NH1", P=20.0, E=6.80, Roach=, BAD=),
#         Jib("J1", I=, J=6.80, LPG=6.81, HBI=),
#         Kite("A2", area=243.95, vce=),
#         # Kite("A5", area=75.0, vce=2.75),
#     ],
# )

NHtest = Yacht(
    Name="NHtest",
    Lwl=15.4,
    Vol=16.2,
    Bwl=5.10,      # 估算: 典型水线宽，约为船宽的85%
    Tc=0.65,       # 估算: 现代帆船的船体吃水，总吃水减去龙骨长度
    WSA=69.5,      # 估算: 基于同尺寸船型的典型湿表面积
    Tmax=2.50,
    Amax=1.88,     # 估算: 基于合理的棱形系数(approx 0.56)反算得出
    Mass=16600,
    Ff=1.60,       # 估算: 52英尺船只的典型船首干舷
    Fa=1.25,       # 估算: 典型船尾干舷，低于船首
    Boa=5.80,      # 估算: 基于常见的长宽比(approx 3.3)
    Loa=15.98,
    App=[
        Keel(Cu=2.70, Cl=1.80, Span=1.85),  # 估算: Span = Tmax - Tc. 弦长基于典型梯形龙骨
        Rudder(Cu=1.00, Cl=0.75, Span=1.70) # 估算: 典型的高展弦比舵
    ],
    Sails=[
        Main("NH1", P=20.0, E=6.80, Roach=0.12, BAD=1.50), # 估算: Roach为典型性能帆的系数, BAD为帆杆高度
        Jib("J1", I=19.80, J=6.80, LPG=6.81, HBI=2.20), # 估算: I略小于P, HBI为估算的上部宽度参数
        Kite("A2", area=243.95, vce=11.50), # 估算: vce约为桅杆高度的58%
        Kite("A5", area=130.0, vce=10.0), # 示例: 一个较小的重风帆
        Kite("A7", area=60.0, vce=7.0), # 示例: 一个较小的重风帆
    ],
)

vpp = VPP(Yacht=NHtest)

vpp.set_analysis(
    tws_range=np.arange(4.0, 22.0, 2.0), twa_range=np.linspace(30.0, 180.0, 31)
)

vpp.run(verbose=False)
vpp.write("results")
vpp.polar(3, True)
vpp.SailChart(True)
