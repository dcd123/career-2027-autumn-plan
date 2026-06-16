from pathlib import Path
import sys


REQUIRED = [
    "## 1. 本周唯一主目标",
    "必做任务",
    "低状态保底任务",
    "## 5. 输出物",
    "## 6. 验收标准",
    "## 7. 面试关联",
    "## 8. 周末复盘问题",
]


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [item for item in REQUIRED if item not in text]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    weekly_dir = root / "weekly"
    files = sorted(weekly_dir.glob("*.md"))

    if not files:
        print("FAIL: weekly/ 下没有周计划文件")
        return 1

    failed = False
    for path in files:
        missing = check_file(path)
        if missing:
            failed = True
            print(f"FAIL: {path.relative_to(root)} 缺少字段")
            for item in missing:
                print(f"  - {item}")
        else:
            print(f"OK: {path.relative_to(root)}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
