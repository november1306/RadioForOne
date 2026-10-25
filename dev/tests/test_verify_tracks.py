"""Unit tests for the skill's queue parser. Run: python -m unittest discover dev/tests"""
import importlib.util
import pathlib
import unittest

SCRIPT = (
    pathlib.Path(__file__).resolve().parents[2]
    / "skills/radio-for-one/scripts/verify_tracks.py"
)
spec = importlib.util.spec_from_file_location("verify_tracks", SCRIPT)
vt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vt)


class ParseLine(unittest.TestCase):
    def test_curator_output_with_bold_and_why(self):
        self.assertEqual(
            vt.parse_line("1. **DakhaBrakha — Specially for You** · house rule"),
            ("DakhaBrakha", "Specially for You"),
        )

    def test_star_and_en_dash(self):
        self.assertEqual(
            vt.parse_line("3. ★ Alcest – Autre temps · blackgaze peak"),
            ("Alcest", "Autre temps"),
        )

    def test_pipe_format(self):
        self.assertEqual(
            vt.parse_line("Scar Symmetry|Morphogenesis"),
            ("Scar Symmetry", "Morphogenesis"),
        )

    def test_hyphen_inside_names_survives(self):
        self.assertEqual(
            vt.parse_line("Jay-Z - 99 Problems"), ("Jay-Z", "99 Problems")
        )

    def test_prose_and_headers_are_skipped(self):
        for line in ["", "# Queue 9", "Work-energy · radio queue", "react below!"]:
            self.assertIsNone(vt.parse_line(line), line)


class ParseQueue(unittest.TestCase):
    def test_duplicates_dropped_order_kept(self):
        text = "1. A — X · why\n2. B — Y · why\n1. A — X · why\n"
        self.assertEqual(vt.parse_queue(text), [("A", "X"), ("B", "Y")])


class Verdict(unittest.TestCase):
    def test_exact_title_beats_first_hit(self):
        recs = [{"title": "X (Remix)", "id": "1"}, {"title": "X", "id": "2"}]
        self.assertEqual(vt.verdict("X", recs), ("OK", recs[1]))

    def test_different_title_flagged(self):
        recs = [{"title": "Other", "id": "1"}]
        self.assertEqual(vt.verdict("X", recs)[0], "??")

    def test_nothing_found(self):
        self.assertEqual(vt.verdict("X", []), ("MISS", None))


if __name__ == "__main__":
    unittest.main()
