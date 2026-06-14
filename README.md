# Git Flow 與 Codex 練習專案

本專案是 Git Flow 與 Codex 協作開發的練習範例，使用 `todo-cli` 作為主題來實作一個簡單的 Python 命令列待辦事項工具。

練習重點不是 Todo CLI 本身的複雜度，而是學習如何在開發過程中：

- 從 `develop` 建立 `feature/*` 分支。
- 在 feature 分支中使用 Codex 生成與修改程式碼。
- 每完成一小段功能就檢查、驗證並 commit。
- 將 feature 分支上傳並合併回 `develop`。
- 在 `develop` 確認穩定後，再合併到 `main`。

完整的 Git Flow 操作流程、Codex 使用時機、commit 與 push 節奏，請參考：[GIT_FLOW_CODEX_PRACTICE.md](./GIT_FLOW_CODEX_PRACTICE.md)。

## Todo CLI 簡易操作

進入專案資料夾後，可以使用以下指令操作 Todo CLI：

```powershell
python app.py add "Buy milk"
python app.py list
python app.py delete 1
```

指令說明：

- `add "任務內容"`：新增一筆待辦事項，並儲存到 `tasks.json`。
- `list`：列出目前所有待辦事項，使用 1-based 編號顯示。
- `delete 編號`：依照 `list` 顯示的編號刪除待辦事項。

## Function 功能介紹

- `add_task(task: str)`：新增非空白任務，讀取目前的 `tasks.json`，加入新任務後寫回檔案。
- `list_tasks()`：讀取 `tasks.json`，並將所有任務以編號格式印出；如果沒有任務，會顯示 `No tasks yet.`。
- `delete_task(index: int)`：使用 1-based index 刪除任務，會驗證 index 是否大於等於 `1`，以及該任務是否存在。

本專案透過這些簡單功能，示範如何在 Git Flow 中分階段請 Codex 協助開發、驗證與文件更新。
