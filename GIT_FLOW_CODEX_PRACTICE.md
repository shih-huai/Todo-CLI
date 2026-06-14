# Git Flow 與 Codex 協作開發流程筆記

## 1. 說明介紹

本文件記錄的是 Git Flow 與 Codex 協作開發的完整練習流程。重點不是 Todo CLI 專案本身的使用方式，而是如何在標準 Git Flow 中安排分支、使用 Codex 生成程式碼、分段 commit、上傳遠端分支，最後從 `feature` 合併到 `develop`，確認穩定後再合併到 `main`。

在這個流程中，分支角色如下：

- `main`：正式穩定版本，只放已確認可發布的程式。
- `develop`：整合開發版本，所有 feature 完成後先合併到這裡驗證。
- `feature/*`：單一功能開發分支，例如 `feature/todo-cli-functions`。

Codex 的角色是協作工程師。適合使用 Codex 的時機包含：

- 開始開發前，請 Codex 閱讀現有檔案並理解專案結構。
- 在 feature 分支上，請 Codex 依需求生成或修改程式。
- 每次生成後，請 Codex 說明修改內容並協助執行驗證。
- commit 前，請 Codex 檢查 `git diff`，確認變更是否符合需求。
- 文件需要同步時，請 Codex 更新 README 或練習筆記。

這次練習使用 Todo CLI 作為範例功能，曾透過 Codex 逐步完成 `add_task()`、`list_tasks()`、`delete_task()`，並更新 README。真正要練習的是：功能要在 feature 分支完成，完成後 commit、push、合併到 `develop`，最後再合併到 `main`。

## 2. 詳細使用說明

### Step 1：確認目前 Git 狀態

開始任何開發前，先確認工作區是否乾淨：

```powershell
git status
```

如果看到 modified 或 untracked 檔案，要先判斷這些變更是否與本次工作有關。

建議原則：

- 與本次功能相關：可以保留，稍後一起 commit。
- 與本次功能無關：先不要混進這次 commit。
- 不確定來源：先詢問或檢查內容，不要直接覆蓋或刪除。

這一步可以請 Codex 協助：

```text
請幫我檢查目前 git status，判斷哪些檔案和這次功能有關。
```

### Step 2：切到 develop 並更新

Git Flow 的功能開發通常從 `develop` 開始，不直接從 `main` 開 feature。

```powershell
git switch develop
git pull origin develop
```

如果本機還沒有 `develop`，可以從遠端建立追蹤分支：

```powershell
git fetch origin
git switch -c develop origin/develop
```

如果這是剛開始練習、遠端也還沒有 `develop`，可以從 `main` 建立：

```powershell
git switch main
git pull origin main
git switch -c develop
git push -u origin develop
```

### Step 3：從 develop 建立 feature 分支

每個功能都應該有自己的 feature 分支。這次 Todo CLI 功能可以命名為：

```powershell
git switch develop
git switch -c feature/todo-cli-functions
```

建立後確認目前所在分支：

```powershell
git branch --show-current
```

應該看到：

```text
feature/todo-cli-functions
```

這一步很重要，因為 Codex 生成程式碼前，必須確定自己正在 feature 分支上。不要在 `main` 或 `develop` 直接生成大量功能程式。

### Step 4：在 feature 分支使用 Codex 生成程式

確認在 feature 分支後，就可以請 Codex 協作開發。

第一次需求可以明確描述：

```text
Create a Python CLI todo application.
Add an add_task(task: str) function.
Save tasks into tasks.json.
Keep the implementation simple and production-quality.
```

Codex 應該先做這些事：

1. 讀取現有檔案，例如 `app.py`、`README.md`、`.gitignore`。
2. 判斷專案目前狀態。
3. 修改 `app.py`，建立 CLI 與 `add_task()`。
4. 用簡單命令驗證功能。
5. 回報修改內容與驗證結果。

生成後先檢查差異：

```powershell
git diff
```

如果內容符合需求，可以做第一次 commit：

```powershell
git add app.py README.md
git commit -m "Add todo CLI task creation"
```

這裡的重點是：不要等所有功能都做完才 commit。每完成一個清楚、可驗證的小功能，就建立一個 commit。

### Step 5：繼續在 feature 分支分段加入功能

接著可以請 Codex 加入列出任務功能：

```text
Add a list_tasks() function that prints indexed todo items.
```

Codex 修改後，執行驗證：

```powershell
python app.py list
```

確認輸出像這樣：

```text
1. Buy milk
```

檢查變更：

```powershell
git diff
```

建立第二個 commit：

```powershell
git add app.py README.md
git commit -m "Add indexed task listing"
```

再請 Codex 加入刪除任務功能：

```text
Add delete_task(index) with proper validation.
All updated functions need to be written in README.md.
```

驗證刪除成功與錯誤處理：

```powershell
python app.py delete 1
python app.py delete 0
python app.py delete 99
```

檢查變更：

```powershell
git diff
```

建立第三個 commit：

```powershell
git add app.py README.md
git commit -m "Add task deletion with validation"
```

如果中途請 Codex 產生文件，例如這份 Git Flow 筆記，也應該獨立 commit：

```powershell
git add GIT_FLOW_CODEX_PRACTICE.md
git commit -m "Document Git Flow and Codex workflow"
```

### Step 6：feature 分支開發完成後做最後確認

在合併前，先檢查目前分支狀態：

```powershell
git status
```

確認 commit 紀錄：

```powershell
git log --oneline --decorate -5
```

確認功能可執行：

```powershell
python app.py add "Final check"
python app.py list
python app.py delete 1
```

如果 `tasks.json` 只是本機測試資料，通常不要提交它。可以用 `git status` 確認它是否被修改，再決定是否還原或加入 `.gitignore`。

這時可以請 Codex 做一次 review：

```text
請幫我 review 目前 feature 分支的 git diff，確認是否有不該提交的檔案、README 是否同步、功能驗證是否足夠。
```

### Step 7：上傳 feature 分支

功能分支完成後，上傳到遠端：

```powershell
git push -u origin feature/todo-cli-functions
```

如果團隊使用 Pull Request，這時應該開 PR，目標分支選 `develop`。

PR 中應該說明：

- 本次新增或修改了哪些功能。
- Codex 協助生成了哪些部分。
- 做過哪些驗證。
- 是否有不提交的本機測試資料，例如 `tasks.json`。

### Step 8：將 feature 合併到 develop

如果使用 PR，確認 review 通過後，在平台上合併到 `develop`。

如果在本機操作，可以這樣做：

```powershell
git switch develop
git pull origin develop
git merge --no-ff feature/todo-cli-functions
```

合併後在 `develop` 再跑一次驗證：

```powershell
python app.py add "Develop check"
python app.py list
python app.py delete 1
```

確認沒有問題後，將 `develop` 推上遠端：

```powershell
git push origin develop
```

這一步代表功能已進入整合開發分支，但還沒有正式進入穩定版本。

### Step 9：在 develop 完成整合確認

`develop` 是多個 feature 的整合點。合併後應該確認：

- 功能是否正常。
- 文件是否同步。
- 沒有把本機測試資料誤提交。
- 沒有不必要的 debug print 或暫存程式。
- `git status` 是否乾淨。

常用指令：

```powershell
git status
git log --oneline --decorate -5
git diff main..develop
```

這時也可以請 Codex 協助總結差異：

```text
請幫我比較 main..develop，整理這次準備合併到 main 的變更重點與風險。
```

### Step 10：確認後將 develop 合併到 main

當 `develop` 確認穩定後，才合併到 `main`。

```powershell
git switch main
git pull origin main
git merge --no-ff develop
```

合併後做最後確認：

```powershell
python app.py list
git status
```

如果一切正常，推送 `main`：

```powershell
git push origin main
```

如果這次合併代表一個版本，也可以加上 tag：

```powershell
git tag v1.0.0
git push origin v1.0.0
```

到這裡，完整流程就是：

```text
develop
  -> feature/todo-cli-functions
  -> commit small changes
  -> push feature
  -> merge into develop
  -> verify develop
  -> merge into main
  -> push main
```

## 3. 結論和操作總結

這次練習的核心不是 Todo CLI，而是建立一個可追蹤、可回溯、可驗證的 AI 輔助開發流程。

最重要的 Git Flow 原則如下：

- 不直接在 `main` 開發功能。
- 功能從 `develop` 建立 `feature/*` 分支。
- Codex 生成程式碼前，先確認目前在正確的 feature 分支。
- 每完成一個小功能，就檢查 `git diff` 並 commit。
- commit 訊息要描述「做了什麼」，例如 `Add indexed task listing`。
- feature 完成後先 push，並合併到 `develop`。
- `develop` 驗證穩定後，才合併到 `main`。
- 合併到 `main` 後再次確認並 push。

Codex 的最佳使用時機如下：

- 開發前：請 Codex 閱讀專案並說明現況。
- 寫功能時：請 Codex 在 feature 分支上生成或修改程式。
- 驗證時：請 Codex 執行或建議測試命令。
- commit 前：請 Codex 檢查 `git diff`，避免混入不相關變更。
- 合併前：請 Codex 整理 `feature` 或 `develop` 的變更重點。
- 文件更新時：請 Codex 同步 README、流程文件或 PR 說明。

推薦的實際工作節奏是：

```text
確認狀態
切到 develop 並更新
建立 feature 分支
請 Codex 生成一小段功能
驗證功能
檢查 git diff
commit
重複功能開發與 commit
push feature
合併到 develop
驗證 develop
合併到 main
push main
```

用這種方式使用 Codex，比一次生成大量程式更穩定。每一段變更都有清楚的分支位置、commit 紀錄與驗證步驟，當功能出問題時也比較容易回頭檢查是哪一次修改造成的。
