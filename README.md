# Game Translator

一个简单的游戏翻译工具，可以将中文翻译成东南亚 Dota 2 玩家常用的英文表达。

## 功能特点

- 全局快捷键支持（Ctrl+T）
- 自动翻译选中的文本
- 支持 Dota 2 游戏术语
- 贴近东南亚玩家日常用语风格

## 使用方法
1. 创建依赖环境
`conda env create -f environment.yml`
`conda activate game_translator`
2. 运行 hotkey_translator.py
`python .\hotkey_translator.py`
3. 在文本输入框中选中要翻译的文本
3. 按下 Ctrl+T 快捷键
4. 选中的文本将被自动翻译并替换

## 配置说明

`cp .env_example .env`

程序使用 .env 文件进行配置，包含以下参数：

- MODEL_NAME: 使用的模型名称
- OPENAI_API_KEY: API密钥
- OPENAI_API_BASE: API基础URL
- MAX_TOKENS: 最大token数
- TRANSLATION_PROMPT: 翻译提示词

如需修改配置，请编辑 .env 文件。

## 注意事项

- 程序会在后台运行，可以通过任务管理器关闭
- 确保有稳定的网络连接以使用翻译功能
- 请妥善保管 .env 文件中的 API 密钥

## 系统要求

- Windows 10 或更高版本
- 需要网络连接

## 技术支持

如有问题或建议，请提交 Issue。 