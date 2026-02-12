# Qiuzhi Restaurant / 秋芝餐厅

🇬🇧 **English** | [🇨🇳 中文](#chinese)

## 🇬🇧 Description
A simulation environment for restaurant management. It demonstrates file-based state management (JSON menus) and basic CLI interaction.

### Capabilities
- **Menu System**: Add, remove, and list dishes.
- **Data Persistence**: Saves menu data to `assets/menu.json`.

### Usage
```bash
# List menu
python3 scripts/menu_manager.py list

# Add item
python3 scripts/menu_manager.py add "Spicy Noodles" 12.50
```

---

## <a id="chinese"></a>🇨🇳 描述
一个餐厅管理的模拟环境。它演示了基于文件的状态管理（JSON 菜单）和基本的命令行交互。

### 核心能力
- **菜单系统**: 添加、删除和列出菜品。
- **数据持久化**: 将菜单数据保存到 `assets/menu.json`。

### 使用方法
```bash
# 列出菜单
python3 scripts/menu_manager.py list

# 添加菜品
python3 scripts/menu_manager.py add "麻辣面" 12.50
```
