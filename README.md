# Ollama 語意分析機器人 (Semantic Analysis Bot)

本專案示範如何利用 **Ollama** 本地端執行 `llama3.1:8b` 大語言模型，針對輸入的英文句子進行中文語意分析，判斷其動作隱含意圖為「開」或「關」。

---

## 📌 功能特點 (Features)

* 採用 **Ollama** 本地端 LLM 執行，確保資料隱私與零 API 費用。
* 使用 `llama3.1:8b` 模型進行精準的單字分類（限制輸出僅為「開」或「關」）。
* 簡易的 Python 整合範例，適合 LLM 語意理解與自然語言處理（NLP）初學者。

---

## 🛠️ 環境需求與準備 (Prerequisites)

在執行本程式前，請確保系統已安裝以下環境：

1. **Python** (建議 3.8 以上版本)
2. **Ollama** (請至 [Ollama 官方網站](https://ollama.com/) 下載並安裝)

安裝 Ollama 後，請打開終端機 (Terminal / CMD) 下載本專案所需的模型：

```bash
ollama pull llama3.1:8b