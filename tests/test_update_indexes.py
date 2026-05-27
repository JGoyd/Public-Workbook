import importlib.util
import sys
import textwrap
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


def load_update_indexes(repo_root: Path):
    script = repo_root / "scripts" / "update-indexes.py"
    spec = importlib.util.spec_from_file_location("update_indexes_script", script)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class UpdateIndexesTest(unittest.TestCase):
    def test_rebuilds_readme_and_workbook_indexes_from_entries(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            (root / "workbook" / "outputs" / "2026" / "05" / "25" / "remoterat-rattrap").mkdir(parents=True)
            (root / "workbook" / "outputs" / "2026" / "05" / "24" / "zorro-ranch").mkdir(parents=True)
            (root / "workbook" / "outputs" / "2026" / "05" / "25" / "remoterat-rattrap" / "other").mkdir()

            (root / "README.md").write_text(
                textwrap.dedent(
                    """\
                    # Public Workbook

                    _Last updated: old_

                    ## Work Timeline

                    <!-- work-timeline:start -->
                    old timeline
                    <!-- work-timeline:end -->

                    ## By Topic

                    <!-- topic-index:start -->
                    old topics
                    <!-- topic-index:end -->
                    """
                ),
                encoding="utf-8",
            )

            (root / "workbook" / "outputs" / "2026" / "05" / "25" / "remoterat-rattrap" / "README.md").write_text(
                textwrap.dedent(
                    """\
                    ---
                    date: 2026-05-25
                    slug: remoterat-rattrap
                    title: RemoteRAT / RATtrap
                    headline: Public campaign write-up, IOC tables, YARA rule, and Pages export
                    public_url: https://example.test/remoterat-rattrap/
                    tags: [security]
                    status: published
                    ---

                    # RemoteRAT / RATtrap
                    """
                ),
                encoding="utf-8",
            )
            (
                root
                / "workbook"
                / "outputs"
                / "2026"
                / "05"
                / "25"
                / "remoterat-rattrap"
                / "other"
                / "packet.pdf.asc"
            ).write_text("signature", encoding="utf-8")

            (root / "workbook" / "outputs" / "2026" / "05" / "24" / "zorro-ranch" / "README.md").write_text(
                textwrap.dedent(
                    """\
                    # 2026-05-24 - Zorro Ranch

                    Headline: Guest access and ranch operations context
                    """
                ),
                encoding="utf-8",
            )

            module = load_update_indexes(Path.cwd())
            module.rebuild(root, today="2026-05-26")

            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertIn("_Last updated: 2026-05-26_", readme)
            self.assertIn("| 2026-05-25 | Mon | RemoteRAT / RATtrap | entry | 2026-05-25 | Public campaign write-up, IOC tables, YARA rule, and Pages export | [open](https://example.test/remoterat-rattrap/) |", readme)
            self.assertIn("| 2026-05-24 | Sun | Zorro Ranch | entry | 2026-05-24 | Guest access and ranch operations context | [open](workbook/outputs/2026/05/24/zorro-ranch/README.md) |", readme)
            self.assertIn("| RemoteRAT / RATtrap | 1 | 2026-05-25 | [topic page](workbook/topics/remoterat-rattrap.md) |", readme)

            master = (root / "workbook" / "indexes" / "master_output_index.md").read_text(encoding="utf-8")
            self.assertIn("| 2026-05-25 | RemoteRAT / RATtrap | entry | 2026-05-25 | [open](../outputs/2026/05/25/remoterat-rattrap/README.md) |", master)
            self.assertIn("verification files", master)

            topic_index = (root / "workbook" / "topics" / "_topic_index.md").read_text(encoding="utf-8")
            self.assertIn("| Zorro Ranch | 1 | 2026-05-24 | [open](zorro-ranch.md) |", topic_index)


if __name__ == "__main__":
    unittest.main()
