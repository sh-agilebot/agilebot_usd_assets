# Agilebot Robotics USD Assets

[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Isaac Sim](https://img.shields.io/badge/Isaac%20Sim-Compatible-green.svg)](https://developer.nvidia.com/isaac-sim)
[![USD](https://img.shields.io/badge/USD-Universal%20Scene%20Description-orange.svg)](https://openusd.org/)

**语言 / Language:** [English](README.md) | [中文](README_zh.md)


---

## 📖 仓库简介

本仓库是 Agilebot Robotics 官方 Isaac 生态的核心资产仓库，包含全系列协作机器人的 **USD（Universal Scene Description）** 数字资产，主要面向 **NVIDIA Isaac Sim 与 Isaac Lab** 生态，用于机器人建模、物理仿真、算法验证与应用开发。

### 核心价值

- **标准化资产**：所有机器人模型均采用 USD 格式，支持跨平台、跨工具的无缝集成
- **物理优化**：预配置的关节自然频率和阻尼参数，确保仿真稳定性和准确性
- **末端执行器扩展**：夹爪请参考 NVIDIA 官方教程自行转换与装配
- **即开即用**：无需额外配置，直接在 Isaac Sim 和 Isaac Lab 中加载使用

USD 是一种面向复杂三维场景的开放标准，支持高效的层级组织、组合（Composition）、变体（Variant）、物理与语义扩展。通过标准化的 USD 格式，您可以快速将这些机器人模型集成到 Isaac Sim、Isaac Lab 及 Omniverse 相关工具链中，并支持灵活的组件配置与扩展。

---

## 🔗 生态系统与相关仓库

本仓库与以下仓库共同组成完整的 Agilebot Isaac 仿真与学习工作流：

| 仓库名称 | 功能定位 | 主要内容 |
|----------|----------|----------|
| **[agilebot_isaac_sim](https://github.com/sh-agilebot/agilebot_isaac_sim)** | 仿真集成 | Agilebot 机器人在 NVIDIA Isaac Sim 中的集成仓库，包含仿真配置、环境设置及示例 Demo。*不包含任何机器人数字资产。* |
| **[agilebot_isaac_lab](https://github.com/sh-agilebot/agilebot_isaac_lab)** | 训练学习 | 基于 NVIDIA Isaac Lab 的训练与学习仓库，包含任务定义、环境配置及训练示例。*不包含任何机器人数字资产。* |
| **[agilebot_isaac_usd_assets](https://github.com/sh-agilebot/agilebot_isaac_usd_assets)** | 资产管理 | 本仓库，统一维护 Agilebot 机器人的 USD 模型、网格文件及贴图资源。 |

---

## 📁 目录结构

```
agilebot_usd_assets/
├── gbt-c5a/                    # GBT-C5A 协作机器人模型
│   ├── configuration/
│   │   ├── materials/          # 材质与纹理资源
│   │   ├── gbt-c5a_base.usd    # 机器人基础结构
│   │   ├── gbt-c5a_physics.usd # 物理与关节属性
│   │   ├── gbt-c5a_robot.usd   # 机器人主体定义
│   │   └── gbt-c5a_sensor.usd  # 传感器配置
│   └── gbt-c5a.usd             # 主入口 USD 文件
├── gbt-c7a/                    # GBT-C7A 协作机器人模型
│   └── (结构与 gbt-c5a 相同)
├── gbt-c12a/                   # GBT-C12A 协作机器人模型
│   └── (结构与 gbt-c5a 相同)
├── gbt-c16a/                   # GBT-C16A 协作机器人模型
│   └── (结构与 gbt-c5a 相同)
├── LICENSE                     # BSD 3-Clause License
├── README.md                   # 英文版 README
└── README_zh.md                # 中文版 README
```

---

## 🤖 机器人型号

### GBT-C5A 协作机器人

- **额定负载**：5 kg  
- **工作半径**：850 mm  
- **特点**：高配置、高性能、高性价比的首款协作机器人  
- **适用场景**：装配、涂胶、检测等协作应用  

### GBT-C7A 协作机器人

- **额定负载**：7 kg  
- **特点**：中等负载协作机器人，适用于多种工业应用  

### GBT-C12A 协作机器人

- **额定负载**：12 kg  
- **特点**：高负载协作机器人，适用于多种工业应用 
- **适用场景**：重载装配、搬运等应用  

### GBT-C16A 协作机器人

- **额定负载**：16 kg  
- **特点**：大负载协作机器人，适用于重载作业场景  

---

## 🔧 夹爪导入与装配（用户自行转换）

出于版权与合规要求，README 不再提供夹爪变体细节。  
请按照 NVIDIA Isaac Sim 5.1.0 官方教程自行完成夹爪转换与装配：

1. 夹爪转换（Import Robotiq 2F-140, Linux only）  
   https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html#import-the-robotiq-2f-140-gripper-linux-only
2. 机械臂与夹爪装配（Robot Assembler）  
   https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html#option-2-connect-the-ur10e-with-the-robotiq-2f-140-gripper-using-the-robot-assembler

---

## 💡 小贴士

抓取常见问题：夹爪力太小时容易夹不住或打滑，力太大时可能导致穿模。  
抓取失败排查：  
[docs/gripper_troubleshooting_zh.md](docs/gripper_troubleshooting_zh.md)

---

## 🖥️ 实验环境

**测试环境：**

- **系统**：Ubuntu 22.04
- **GPU**：NVIDIA RTX 5090
- **Isaac Sim 版本**：5.1.0-rc.19+release.26219.9c81211b.gl
- **Isaac Lab 版本**：2.3.0

---

## 🚀 使用方法

### 在 Isaac Sim 中使用

当前版本提供标准化 USD 资产文件，可直接通过 Isaac Sim 的 USD Loader 或 Reference 方式加载。
Isaac Sim 的完整示例工程将在后续版本中提供。

### 在 Isaac Lab 中使用

当前版本可作为 Isaac Lab 中 `Articulation` 或自定义资产的输入。
相关任务配置与示例将另行发布。

---

## ⚠️ 物理参数说明

**重要提示：**

所有机器人型号的关节自然频率和阻尼参数均已配置为 Isaac Sim 推荐的经验值：

- **活动关节**：自然频率 = 300，阻尼 = 0.005
- **联动关节**：自然频率 = 2500，阻尼 = 0.005

这些值基于 Isaac Sim 官方推荐，并已通过测试可减少机器人仿真时出现的乱飞、晃动等问题。

关于质量和方向惯量：
- **所有机型（GBT-C5A、GBT-C7A、GBT-C12A、GBT-C16A）**：由捷勃特公司提供的默认值

请根据具体的仿真任务需求手动调整上述参数，以确保仿真行为的准确性。

---

## 📄 许可证

本项目采用 **BSD 3-Clause License**，详见 [LICENSE](LICENSE)。

---

## 📞 联系方式

* **商务咨询**：[info@agilebot.com.cn](mailto:info@agilebot.com.cn)
* **技术支持**：400-996-7588
* **官方网站**：[https://www.sh-agilebot.com/](https://www.sh-agilebot.com/)

---

## 🙏 致谢

感谢 [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) 和 [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) 团队提供的优秀机器人仿真平台。

有关第三方许可证的详细信息，请参考 [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)。

---

## 📋 更新日志

详细的版本历史和变更记录，请参考 [CHANGELOG_zh.md](CHANGELOG_zh.md)。

---

## 🗺️ 后续计划

未来的开发计划包括：

### 工业机器人机型
- [ ] GBT-S3A - 3kg 负载工业 SCARA 机器人
- [ ] GBT-S6A - 6kg 负载工业 SCARA 机器人
- [ ] GBT-S10A - 10kg 负载工业 SCARA 机器人
- [ ] GBT-S20A - 20kg 负载工业 SCARA 机器人
- [ ] GBT-P7A - 7kg 负载工业 PUMA 机器人

---

## 🏢 关于 Agilebot Robotics

上海捷勃特机器人有限公司是一家专业的工业机器人和智能磁驱输送系统提供商。公司以"驱动未来工厂"为愿景，依托先进的驱控一体控制技术，为客户提供高性能、高品质、高性价比、高易用性的机器人产品。

产品线涵盖协作机器人、工业六轴机器人与 SCARA 机器人，广泛应用于装配、搬运、检测等工业场景。

* **官方网站**：[https://www.sh-agilebot.com/](https://www.sh-agilebot.com/)
* **商务邮箱**：[info@agilebot.com.cn](mailto:info@agilebot.com.cn)
* **联系电话**：400-996-7588

---

© 2026 Agilebot Robotics. All rights reserved.
