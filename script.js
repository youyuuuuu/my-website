    let selectedLevel = null;
    let selectedMode = null;

    function selectLevel(level) {
      selectedLevel = level;
      alert(`你選擇了等級：${level}`);
    }

    function selectMode(mode) {
      selectedMode = mode;
      alert(`你選擇了題型：${mode}`);
    }

    function startQuiz() {
      if (!selectedLevel || !selectedMode) {
        alert("請選擇等級和題型！");
        return;
      }

      // 導向測驗頁面（你可以根據需要調整 quiz.html）
      const url = `quiz.html?level=${selectedLevel}&mode=${selectedMode}`;
      window.location.href = url;
    }
