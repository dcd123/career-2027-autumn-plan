from pathlib import Path
import sys


WEEKLY_REQUIRED = [
    "## 1. 本周唯一主目标",
    "## 2. 必做任务",
    "## 3. 选做任务",
    "## 4. 低状态保底任务",
    "## 5. 输出物",
    "## 6. 验收标准",
    "## 7. 周日复盘问题",
]

CURRENT_REQUIRED = [
    "## 1. 当前周",
    "## 2. 本周唯一主目标",
    "## 3. 本周任务清单",
    "### 必做任务",
    "### 低状态保底任务",
    "## 5. 本周输出物",
    "## 6. 验收标准",
    "## 8. 周日复盘",
]


def missing_items(path: Path, required: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [item for item in required if item not in text]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failed = False

    current = root / "WEEKLY_CURRENT.md"
    if not current.exists():
        print("FAIL: 缺少 WEEKLY_CURRENT.md")
        failed = True
    else:
        missing = missing_items(current, CURRENT_REQUIRED)
        if missing:
            print("FAIL: WEEKLY_CURRENT.md 缺少字段")
            for item in missing:
                print(f"  - {item}")
            failed = True
        else:
            print("OK: WEEKLY_CURRENT.md")

    weekly_files = sorted((root / "weekly").glob("*.md"))
    if not weekly_files:
        print("FAIL: weekly/ 下没有周计划归档文件")
        failed = True

    for path in weekly_files:
        missing = missing_items(path, WEEKLY_REQUIRED)
        if missing:
            print(f"FAIL: {path.relative_to(root)} 缺少字段")
            for item in missing:
                print(f"  - {item}")
            failed = True
        else:
            print(f"OK: {path.relative_to(root)}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
