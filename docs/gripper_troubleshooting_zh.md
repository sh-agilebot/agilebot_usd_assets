# 夹爪抓取失败排查指南

本文档针对 Isaac Sim 5.1 环境下的夹爪抓取失败问题，提供系统化的排查步骤和解决方案。

## 推荐排查顺序

按照以下顺序进行排查，通常可以解决大部分抓取失败问题：

### 1. 检查碰撞体配置

**问题描述**：碰撞体（Collider）几何形状与物体实际形状不匹配是导致抓取失败的常见原因。

**排查步骤**：
1. 在 Isaac Sim 中启用碰撞体可视化
2. 检查夹爪指尖的碰撞几何是否与视觉模型贴合
3. 检查被抓取物体的碰撞体是否准确

**解决方案**：
- 如果碰撞体过于简化，需要重新生成更精确的碰撞网格
- 确保碰撞体完全包裹物体，但不过于复杂

---

### 2. 提高物理仿真步频

**适用场景**：抓取重物或需要高力矩时，物体打滑或穿透夹爪表面。

**操作步骤**：
1. 在 Stage 面板中选择 `Physics Scene`
2. 修改 `Time Steps per Second` 参数
3. 建议值：**至少 80**，对于复杂场景可提高至 120

**参考案例**：官方教程中 2.5kg 负载的抓取案例，通过将该参数提高到 80，成功解决了抓取失败问题。

> **参考链接**：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/rig_closed_loop_structures.html

---

### 3. 调整夹爪关节力参数

#### 3.1 力的大小调节

抓取过程需要在**夹持稳定性**和**接触安全性**之间取得平衡：

| 问题现象 | 可能原因 | 解决方案 |
|---------|---------|---------|
| 物体打滑、夹不住 | 关节力过小 | 适当增大 `Joint Max Force` |
| 物体被夹穿模 | 关节力过大 | 适当减小 `Joint Max Force` |

**推荐值**：
- 标准抓取：10.0 - 20.0
- 精密抓取：5.0（官方教程示例中该值表现更稳定）

#### 3.2 摩擦系数设置

为夹爪指尖添加 Physics Material：
1. 在 `Property` 面板中找到 `Physics Material`
2. 创建或选择材质，设置摩擦系数
3. **推荐值**：静摩擦系数和动摩擦系数均设为 **1.0**

> **参考链接**：
> - https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/rig_closed_loop_structures.html
> - https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_configure_manipulator.html

---

### 4. 并联夹爪刚度参数（适用于 Robotiq 等）

对于 Robotiq 2F-85 / 2F-140 这类并联机构夹爪，需要额外配置关节刚度。

**配置步骤**：
1. 找到 `[left,right]_outer_finger_joint` 关节
2. 在 `Drive` 属性中设置 `stiffness = 0.05`

**作用**：
- 减少夹爪闭合时的内鼓现象
- 提高接触稳定性

> **参考链接**：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/rig_closed_loop_structures.html

---

### 5. Surface Gripper 排查（吸附/约束式抓取）

如果使用 Surface Gripper 实现吸附式抓取，请检查以下配置：

#### 5.1 Attachment Points 检查清单

| 检查项 | 要求值 | 说明 |
|-------|-------|------|
| 关节类型 | D6 Joint | 必须使用 D6 关节 |
| 启用状态 | Enabled | 确保勾选启用 |
| Body0 | 与夹爪一致 | 参考体必须与夹爪根节点一致 |
| Exclude from Articulation | True | 必须从关节链中排除 |

#### 5.2 关键参数调优

| 参数 | 功能 | 过低表现 | 建议范围 |
|-----|------|---------|---------|
| Max Grip Distance | 最大吸附距离 | 无法吸附目标 | 0.01 - 0.05 |
| Retry Interval | 重试间隔 | 错过吸附时机 | 0.1 - 0.5 |
| Shear Force Limit | 剪切力限制 | 提起后物体滑落 | 50 - 200 |
| Coaxial Force Limit | 同轴力限制 | 吸附力不足 | 100 - 500 |

> **参考链接**：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_simulation/ext_isaacsim_robot_surface_gripper.html

---

## Isaac Sim 5.1 新特性

Isaac Sim 5.1 版本针对夹爪抓取场景进行了专项优化：

1. **新增关节参数调优教程**：官方提供了专门针对夹爪关节参数调优的详细教程
2. **接触求解器改进**：提升了接触检测和求解的稳定性

> **参考链接**：https://docs.omniverse.nvidia.com/kit/docs/omni_physics/107.3/dev_guide/guides/gripper_tuning_example.html

---

## 常见问题速查

| 问题现象 | 最可能原因 | 优先检查项 |
|---------|-----------|-----------|
| 完全夹不住 | 碰撞体不匹配 | 第 1 项 |
| 夹住后打滑掉落 | 步频不足/摩擦不足 | 第 2、3.2 项 |
| 物体被夹穿 | 关节力过大 | 第 3.1 项 |
| 闭合时抖动不稳 | 刚度参数缺失 | 第 4 项 |
| 吸附不上 | Attachment 配置错误 | 第 5.1 项 |
| 吸附后提起掉落 | 力限制过低 | 第 5.2 项 |

---

## 相关链接

- Isaac Sim 5.1 官方文档：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/
- 闭环结构配置教程：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/rig_closed_loop_structures.html
- 机械臂配置教程：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup_tutorials/tutorial_configure_manipulator.html
- Surface Gripper 文档：https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_simulation/ext_isaacsim_robot_surface_gripper.html
