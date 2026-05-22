---
name: "python-docstring-formatter"
description: "为 Python 代码生成标准化的结构化注释（Docstring）。当用户要求为 Python 文件、类或函数添加注释或结构化文档时触发。"
---

# Python Docstring Formatter

该 Skill 专门用于为 Python 代码（模块、类、方法和函数）生成或补全符合规范的结构化注释（Docstring）。默认采用 Google 风格（或遵循当前项目中已有的风格）。

## 执行步骤

1. **读取文件**：使用 `Read` 工具读取需要添加注释的 Python 文件代码。
2. **分析代码**：理解模块功能、类结构、函数输入输出及异常情况。
3. **生成/更新注释**：
   - 确保文件/模块顶部有**模块级别**的说明注释。
   - 确保所有类都有**类级别**的注释，包含 `Attributes`（属性说明）和 `Example`（可选，使用示例）。
   - 确保 `__init__` 方法和所有**普通函数/方法**都有详细注释，包含 `Args`（参数说明）、`Returns`（返回值说明，若有）和 `Raises`（异常说明，若有）。
4. **回写文件**：使用 `Write` 或 `SearchReplace` 工具将更新后的代码写入文件。

## 注释规范示例 (Google Style)

### 1. 模块级别注释
```python
"""
模块名称或简短描述

详细的模块功能描述，可以包含多行。
说明该模块的主要职责、提供的核心功能等。

技术要点：
- 要点 1
- 要点 2
"""
```

### 2. 类级别注释
```python
class ExampleClass:
    """
    类的简短描述
    
    类的详细描述，说明该类的作用和使用场景。
    
    Attributes:
        attr1: 属性 1 的描述
        attr2: 属性 2 的描述
        
    Example:
        >>> obj = ExampleClass("test")
        >>> obj.do_something()
    """
```

### 3. 函数/方法级别注释
```python
def example_function(param1: str, param2: int = 0) -> bool:
    """
    函数的简短描述
    
    函数的详细说明，包括它的具体行为、副作用等。
    
    Args:
        param1: 参数 1 的描述
        param2: 参数 2 的描述. Defaults to 0.
        
    Returns:
        返回值的描述
        
    Raises:
        ValueError: 当参数不合法时抛出
    """
```

## 注意事项
- 注释语言应与用户要求或项目现有注释语言保持一致（如中文）。
- 保持代码的原始缩进和格式不变。
- 确保 `Args` 和 `Returns` 中的类型提示与代码中的 Type Hint 对应。
