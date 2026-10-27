# 🖐️ AI Gesture Presentation Controller (Webcam AI 手勢無障礙簡報控制器)

> 國立東華大學 人工智慧概論 · 期中專題作品  
> 訓練平台：Google Teachable Machine (Standard Image Model)  
> 推論架構：TensorFlow.js (Client-side Edge AI)  

---

## 🌟 專題特色 (Features)

- **免安裝、純前端**：打開網頁即可啟用，無需安裝驅動程式或額外軟體。
- **保護隱私 (Zero Upload)**：所有影像處理皆在使用者電腦瀏覽器內進行，鏡頭畫面絕不上傳雲端。
- **抗誤觸雙重把關**：
  - 85% 信心門檻過濾
  - 1.5 秒動作冷卻 (Debounce)
- **多模態即時回饋**：視覺動態光效 ＋ 提示音，讓講者無須頻繁轉頭看螢幕。

---

## 🕹️ 手勢對應表 (Gestures)

| 手勢名稱 | 動作說明 | 系統功能 |
| :--- | :--- | :--- |
| **Next (👉 掌心向右)** | 掌心朝向鏡頭微向右偏 | 切換至下一頁 (Next Slide) |
| **Prev (👈 掌心向左)** | 掌心朝向鏡頭微向左偏 | 切換至上一頁 (Prev Slide) |
| **Confirm (👍 比讚/握拳)** | 拇指朝上或握拳於胸前 | 聚焦/確認 (Confirm) |
| **Neutral (待機自然狀態)** | 雙手自然下垂、桌面空景 | 保持安靜待機 |

---

## 🚀 快速開始 (Quick Start)

### 線上體驗 (Live Demo)
直接點擊由 GitHub Pages 代管的網址即可體驗：  
`https://<your-github-username>.github.io/<repo-name>/`

### 本機執行 (Local Run)
1. 下載或複製本專案庫：
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. 使用任何本地伺服器開啟 `index.html`（例如 VS Code Live Server，或 Python 內建伺服器）：
   ```powershell
   python -m http.server 8000
   ```
3. 在瀏覽器打開 `http://localhost:8000`，允許視訊鏡頭權限，即可開始隔空手勢翻頁！

---

## 📁 專案目錄結構

```text
├── index.html            # 互動式簡報介面與 TensorFlow.js 即時推論程式
├── midterm-report.md     # 完整期中專題書面報告
├── README.md             # 專案說明文件
└── assets/               # 簡報圖示與輔助檔案
```

---

## 📜 授權條款 (License)
MIT License.
