export class Dice {
    /**
     * サイコロを1回振る
     * @param sides サイコロの面数（デフォルト: 6）
     * @returns サイコロの結果（1から面数までのランダムな整数）
     */
    roll(sides = 6) {
        if (sides < 2) {
            throw new Error("サイコロの面数は2以上である必要があります。");
        }
        return Math.floor(Math.random() * sides) + 1;
    }
    /**
     * サイコロを複数回振る
     * @param count サイコロを振る回数
     * @param sides サイコロの面数（デフォルト: 6）
     * @returns サイコロの結果の配列
     */
    rollMultiple(count, sides = 6) {
        if (count < 1) {
            throw new Error("サイコロの数は1以上である必要があります。");
        }
        return Array.from({ length: count }, () => this.roll(sides));
    }
    /**
     * クリティカルヒットの判定
     * @param result サイコロの結果
     * @param criticalValue クリティカル値（デフォルト: サイコロの面数）
     * @returns クリティカルヒットかどうか
     */
    isCriticalHit(result, criticalValue) {
        return result === criticalValue;
    }
}
//# sourceMappingURL=dice.js.map