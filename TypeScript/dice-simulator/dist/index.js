import { Dice } from "./dice";
import Chart from "chart.js/auto"; // Chart.jsをインポート
// サイコロクラスのインスタンス作成
const dice = new Dice();
// GUI要素を取得
const diceCountInput = document.getElementById("dice-count");
const sidesInput = document.getElementById("sides");
const rollButton = document.getElementById("roll-button");
const diceContainer = document.getElementById("dice-container");
const resultArea = document.getElementById("results");
const chartContainer = document.getElementById("chart-container");
let rollHistory = [];
let chart = null;
/**
 * グラフを作成
 */
function createChart(results) {
    const frequencies = results.reduce((acc, result) => {
        acc[result] = (acc[result] || 0) + 1;
        return acc;
    }, {});
    const labels = Object.keys(frequencies).map(Number);
    const data = Object.values(frequencies);
    if (chart) {
        chart.destroy(); // 既存のグラフを破棄
    }
    const ctx = document.createElement("canvas");
    chartContainer.innerHTML = "";
    chartContainer.appendChild(ctx);
    chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels,
            datasets: [
                {
                    label: "結果の頻度",
                    data,
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1,
                },
            ],
        },
        options: {
            scales: {
                y: { beginAtZero: true },
            },
        },
    });
}
/**
 * サイコロの要素を作成
 */
function createDiceElements(count) {
    diceContainer.innerHTML = "";
    const diceElements = [];
    for (let i = 0; i < count; i++) {
        const diceElement = document.createElement("div");
        diceElement.className = "dice";
        for (let j = 1; j <= 6; j++) {
            const face = document.createElement("div");
            face.className = "dice-face";
            face.textContent = j.toString();
            diceElement.appendChild(face);
        }
        diceContainer.appendChild(diceElement);
        diceElements.push(diceElement);
    }
    return diceElements;
}
/**
 * サイコロの目を表示
 */
function showDiceFaces(diceElements, results, critical) {
    diceElements.forEach((diceElement, index) => {
        const faces = diceElement.querySelectorAll(".dice-face");
        faces.forEach((face, faceIndex) => {
            const isCritical = results[index] === critical;
            face.classList.toggle("active", faceIndex + 1 === results[index]);
            // faceをHTMLElement型にキャストすることでstyleプロパティにアクセス可能にする
            face.style.color = isCritical ? "red" : "";
        });
    });
}
/**
 * サイコロを振るボタンクリックイベント
 */
rollButton.addEventListener("click", () => {
    const diceCount = parseInt(diceCountInput.value, 10);
    const sides = parseInt(sidesInput.value, 10);
    // 入力値チェック
    if (isNaN(diceCount) || diceCount < 1 || diceCount > 100 || isNaN(sides) || sides < 2 || sides > 100) {
        resultArea.innerHTML = "⚠️ サイコロの数は1〜100、面数は2〜100の範囲で指定してください。";
        return;
    }
    // サイコロの要素を作成
    const diceElements = createDiceElements(diceCount);
    // アニメーション開始
    diceElements.forEach((dice) => dice.classList.add("rolling"));
    resultArea.innerHTML = "サイコロを振っています...";
    setTimeout(() => {
        // アニメーション終了
        diceElements.forEach((dice) => dice.classList.remove("rolling"));
        // サイコロを振る
        const results = Array.from({ length: diceCount }, () => dice.roll(sides));
        const critical = sides; // 最大値をクリティカル値とする
        showDiceFaces(diceElements, results, critical);
        rollHistory.push(results);
        updateResults(results, critical);
        createChart(results);
    }, 2000);
});
/**
 * 結果と履歴を更新
 */
function updateResults(results, critical) {
    const total = results.reduce((sum, num) => sum + num, 0);
    const average = (total / results.length).toFixed(2);
    const criticalCount = results.filter((num) => num === critical).length;
    resultArea.innerHTML = `
    <p>🎲 サイコロの結果: ${results.join(", ")}</p>
    <p>合計: ${total}</p>
    <p>平均: ${average}</p>
    <p>クリティカルヒット数: ${criticalCount}</p>
    <hr>
    <h3>履歴:</h3>
    <ul>
      ${rollHistory
        .map((roll, index) => `<li>振った回数 ${index + 1}: ${roll.join(", ")}</li>`)
        .join("")}
    </ul>
  `;
}
//# sourceMappingURL=index.js.map