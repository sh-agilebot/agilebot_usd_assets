# Agilebot Robotics USD Assets

[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)
[![Isaac Sim](https://img.shields.io/badge/Isaac%20Sim-Compatible-green.svg)](https://developer.nvidia.com/isaac-sim)
[![USD](https://img.shields.io/badge/USD-Universal%20Scene%20Description-orange.svg)](https://openusd.org/)

**Language:** [English](README.md) | [中文](README_zh.md)


---

## 📖 Repository Overview

This repository is the core asset repository for the official Agilebot Isaac ecosystem, containing USD (Universal Scene Description) digital assets for the full range of Agilebot collaborative robots. It primarily targets the **NVIDIA Isaac Sim and Isaac Lab** ecosystems for robot modeling, physics simulation, algorithm validation, and application development.

### Core Value

- **Standardized Assets**: All robot models are in USD format, supporting seamless integration across platforms and tools
- **Physics Optimized**: Pre-configured joint natural frequencies and damping parameters ensure simulation stability and accuracy
- **End-Effector Extension**: Users can import and assemble grippers following official NVIDIA tutorials
- **Ready to Use**: No additional configuration required, directly load and use in Isaac Sim and Isaac Lab

USD is an open standard for complex 3D scenes, supporting efficient hierarchical organization, composition, variants, physics, and semantic extensions. Through USD format, these robot models can be directly used in Isaac Sim, Isaac Lab, and Omniverse-related toolchains, with flexible component configuration and extension capabilities.

---

## 🔗 Ecosystem and Related Repositories

This repository works with the following repositories to provide a complete Agilebot Isaac simulation and learning workflow:

| Repository Name | Function | Main Content |
|-----------------|----------|--------------|
| **[agilebot_isaac_sim](https://github.com/sh-agilebot/agilebot_isaac_sim)** | Simulation Integration | Isaac Sim integration for Agilebot robots, including simulation configurations, setup files, and demo examples. *No robot digital assets are included.* |
| **[agilebot_isaac_lab](https://github.com/sh-agilebot/agilebot_isaac_lab)** | Training & Learning | Isaac Lab environments and training examples for Agilebot robots, including task definitions and learning pipelines. *No robot digital assets are included.* |
| **[agilebot_isaac_usd_assets](https://github.com/sh-agilebot/agilebot_isaac_usd_assets)** | Asset Management | This repository, maintaining centralized USD files, meshes, and textures for Agilebot robots. |

---

## 📁 Directory Structure

```
agilebot_usd_assets/
├── gbt-c5a/                    # GBT-C5A collaborative robot model
│   ├── configuration/
│   │   ├── materials/          # Material and texture resources
│   │   ├── gbt-c5a_base.usd    # Robot base structure
│   │   ├── gbt-c5a_physics.usd # Physics and joint properties
│   │   ├── gbt-c5a_robot.usd   # Main robot definition
│   │   └── gbt-c5a_sensor.usd  # Sensor configuration
│   └── gbt-c5a.usd             # Main entry USD file
├── gbt-c7a/                    # GBT-C7A collaborative robot model
│   └── (Same structure as gbt-c5a)
├── gbt-c12a/                   # GBT-C12A collaborative robot model
│   └── (Same structure as gbt-c5a)
├── gbt-c16a/                   # GBT-C16A collaborative robot model
│   └── (Same structure as gbt-c5a)
├── LICENSE                     # BSD 3-Clause License
├── README.md                   # This file (English version)
└── README_zh.md                # Chinese version
```

---

## 🤖 Robot Models

### GBT-C5A Collaborative Robot

- **Rated Payload**: 5 kg  
- **Working Radius**: 850 mm  
- **Features**: High-performance, cost-effective collaborative robot  
- **Applications**: Assembly, gluing, inspection, and other collaborative tasks  

### GBT-C7A Collaborative Robot

- **Rated Payload**: 7 kg  
- **Features**: Medium-load collaborative robot suitable for various industrial applications  

### GBT-C12A Collaborative Robot

- **Rated Payload**: 12 kg  
- **Features**: High-load collaborative robot suitable for various industrial applications  
- **Applications**: Heavy-duty assembly, material handling, etc.  

### GBT-C16A Collaborative Robot

- **Rated Payload**: 16 kg  
- **Features**: Large-load collaborative robot suitable for heavy-duty operations  

---

## 🔧 Gripper Import and Assembly (User Self-Conversion)

Due to copyright and compliance requirements, the README no longer provides gripper variant details.
Please follow the official NVIDIA Isaac Sim 5.1.0 tutorials to complete gripper conversion and assembly:

1. Gripper Conversion (Import Robotiq 2F-140, Linux only)
   https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html#import-the-robotiq-2f-140-gripper-linux-only
2. Robot Assembler (Connect arm with gripper)
   https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_import_assemble_manipulator.html#option-2-connect-the-ur10e-with-the-robotiq-2f-140-gripper-using-the-robot-assembler

---

## 💡 Tips

Gripper grasping issues: Insufficient force causes slipping, excessive force causes clipping.  
Troubleshooting guide:  
[docs/gripper_troubleshooting_zh.md](docs/gripper_troubleshooting_zh.md)

---

## 📦 Gripper Model Source

The gripper model is sourced from the open-source project:
[robotiq_2f_gripper](https://github.com/gen-robot/robotiq_2f_gripper/tree/main/robotiq_2f_140_gripper_visualization)

This model is for simulation and demonstration purposes only, and its copyright belongs to the original author.

Gripper import and assembly process refers to NVIDIA official documentation:
[Isaac Sim Robot Import and Assembly Tutorial](https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_import_assemble_manipulator.html)

---

## 🖥️ Experimental Environment

**Test Environment:**

- **System**: Ubuntu 22.04
- **GPU**: NVIDIA RTX 5090
- **Isaac Sim Version**: 5.1.0-rc.19+release.26219.9c81211b.gl
- **Isaac Lab Version**: 2.3.0

---

## 🚀 Usage

### Using in Isaac Sim

The current version provides standardized USD asset files, which can be directly loaded via Isaac Sim's USD Loader or Reference method. Complete sample projects for Isaac Sim will be provided in future releases.

### Using in Isaac Lab

The current version can be used as input for `Articulation` or custom assets in Isaac Lab. Task configurations and examples will be released separately.

---

## ⚠️ Physics Parameters Notice

**Important Note on Physics Parameters:**

For all robot models, the joint natural frequency and damping parameters have been configured with Isaac Sim recommended empirical values:

- **Active Joints**: Natural frequency = 300, Damping = 0.005
- **Linked Joints**: Natural frequency = 2500, Damping = 0.005

These values are based on Isaac Sim official recommendations and have been tested to reduce issues like robot flying or shaking during simulation.

Regarding mass and directional inertia:
- **All Models (GBT-C5A, GBT-C7A, GBT-C12A, GBT-C16A)**: Default values provided by Agilebot

Please manually adjust these parameters according to your specific simulation requirements to ensure accurate behavior.

---

## 🤝 Contribution Guidelines

Contributions are welcome via Issues and Pull Requests.

### Contribution Process

1. Fork this repository
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m "Add some AmazingFeature"`
4. Push to remote branch: `git push origin feature/AmazingFeature`
5. Create a Pull Request

---

## 📄 License

This project is licensed under the **BSD 3-Clause License**, see [LICENSE](LICENSE) for details.

---

## 📞 Contact

* **Business Inquiry**: [info@agilebot.com.cn](mailto:info@agilebot.com.cn)
* **Technical Support**: 400-996-7588
* **Official Website**: [https://www.sh-agilebot.com/](https://www.sh-agilebot.com/)

---

## 🙏 Acknowledgments

Thanks to the [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim) and [Isaac Lab](https://isaac-sim.github.io/IsaacLab/) teams for providing excellent robot simulation platforms.

For detailed information about third-party licenses, please refer to [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md).

---

## 📋 Changelog

For detailed version history and changes, please refer to [CHANGELOG.md](CHANGELOG.md).

---

## 🗺️ Roadmap

Future development plans include:

### Industrial Robot Models
- [ ] GBT-S3A - 3 kg payload industrial SCARA robot
- [ ] GBT-S6A - 6 kg payload industrial SCARA robot
- [ ] GBT-S10A - 10 kg payload industrial SCARA robot
- [ ] GBT-S20A - 20 kg payload industrial SCARA robot
- [ ] GBT-P7A - 7 kg payload industrial PUMA robot



---

## 🏢 About Agilebot Robotics

Shanghai Agilebot Robotics Co., Ltd. is a professional provider of industrial robots and intelligent magnetic drive conveyor systems. With the vision of "Driving Future Factories", the company provides high-performance, high-quality, cost-effective, and easy-to-use robot products based on advanced integrated drive and control technology.

The product line covers collaborative robots, industrial six-axis robots, and SCARA robots, widely used in assembly, material handling, inspection, and other industrial scenarios.

* **Official Website**: [https://www.sh-agilebot.com/](https://www.sh-agilebot.com/)
* **Business Email**: [info@agilebot.com.cn](mailto:info@agilebot.com.cn)
* **Contact Phone**: 400-996-7588

---

© 2026 Agilebot Robotics. All rights reserved.
