# 🖐️ AI Gesture Presentation Controller (Webcam AI 手勢無障礙簡報控制器)

> 國立東華大學 人工智慧概論 · 期中專題作品  
> 訓練平台：Google Teachable Machine (Standard Image Model)  
> 推論架構：TensorFlow.js (Client-side Edge AI)  

---

## 🌟 專題特色 (Features)

- **免安裝、純前端**：打開網頁即可啟用，無需安裝驅動程式或額外軟體。
- **保護隱私 (Zero Upload)**：所有影像處理皆在使用者電腦瀏覽器內進行，鏡頭畫面絕不上傳雲端。
- **抗誤觸雙重把關**：
  - 80% 信心門檻過濾
  - 1.5 秒動作冷卻 (Debounce)
- **多模態即時回饋**：視覺動態光效 ＋ 提示音，讓講者無須頻繁轉頭看螢幕。
- **支援控制外部真實簡報**：
  - 🖥️ **全域簡報筆模式**：可隔空控制全螢幕播放的 **Microsoft PowerPoint**、**Keynote** 或 **Adobe PDF**。
  - 📄 **網頁內建嵌入模式**：支援直接在網頁載入本機自訂 PDF 檔案或嵌入 Google 簡報 / Canva 連結。

---

## 🕹️ 手勢對應表 (Gestures)

| 手勢名稱 | 動作說明 | 系統功能 |
| :--- | :--- | :--- |
| **Next (👉 掌心向右)** | 掌心朝向鏡頭微向右偏 | 切換至下一頁 (Next Slide / Right Arrow) |
| **Prev (👈 掌心向左)** | 掌心朝向鏡頭微向左偏 | 切換至上一頁 (Prev Slide / Left Arrow) |
| **Confirm (👍 比讚/握拳)** | 拇指朝上或握拳於胸前 | 聚焦/確認 (Confirm) |
| **Neutral (待機自然狀態)** | 雙手自然下垂、桌面空景 | 保持安靜待機 |

---

## 🚀 快速開始 (Quick Start)

### 線上體驗 (Live Demo)
直接點擊由 GitHub Pages 代管的網址即可體驗：  
👉 **https://jensen2121-reaper.github.io/webcam-gesture-controller/**

---

## 🖥️ 如何在其他簡報中應用本系統？

### 方式 A：控制本機 PowerPoint / PDF（全域簡報筆模式）
想用手勢翻閱電腦中全螢幕播放的 PowerPoint、Keynote 或 Adobe PDF：
1. 雙擊執行專案目錄下的 `start-desktop-bridge.cmd`（或執行 `python desktop_bridge.py`）。
2. 在網頁頂部會看到狀態亮起：`🖥️ 本機 PPT 簡報筆：已連線`。
3. 將你的 PowerPoint 或 PDF 進入全螢幕播放，只要在鏡頭前比出 **👉 掌心向右** 或 **👈 掌心向左**，背景服務將自動向 Windows 系統發送真實鍵盤箭頭鍵，無縫翻頁！

### 方式 B：將外部簡報直接嵌入網頁中
不想跑背景程式，想純用瀏覽器報告：
1. 在網頁中央上方點選 **「📄 載入本機 PDF 簡報」**，直接選取你的 PDF 投影片。
2. 或點選 **「🌐 嵌入 Google 簡報 / Canva 網址」**，貼上公開發布連結。
3. 即可直接在同一個網頁視窗中隔空翻閱整份客製化簡報！

---

## 📁 專案目錄結構

```text
├── index.html                 # 互動式簡報介面與 TensorFlow.js 即時推論程式
├── desktop_bridge.py          # 系統級鍵盤橋接服務 (純 Python + Windows API)
├── start-desktop-bridge.cmd   # 一鍵啟動 PPT 簡報筆背景服務
├── run-app.cmd                # 一鍵啟動本機伺服器並開啟網頁
├── midterm-report.md          # 完整期中專題書面報告
├── midterm-report.pdf         # 匯出之標準 A4 PDF 報告
├── model/                     # Teachable Machine 匯出模型 (model.json, weights.bin, metadata.json)
└── README.md                  # 專案說明文件
```

---

## 📜 授權條款 (License)
MIT License.
