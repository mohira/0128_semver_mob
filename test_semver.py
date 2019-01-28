from __future__ import annotations

import unittest


class SemVer:
    def __init__(self, major: int, minor: int, patch: int):
        self.major, self.minor, self.patch = major, minor, patch

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"

    def __eq__(self, other: SemVer):
        return isinstance(other, SemVer) and \
               self.major == other.major and \
               self.minor == other.minor and \
               self.patch == other.patch


class TestSemVer(unittest.TestCase):
    def test_SemVerの文字列表現を取得できる_その1(self):
        semver = SemVer(major=1, minor=4, patch=2)

        self.assertEqual("1.4.2", str(semver))

    def test_SemVerの文字列表現を取得できる_その2(self):
        semver = SemVer(major=2, minor=5, patch=6)

        self.assertEqual("2.5.6", str(semver))

    def test_等価性を比較できる_等しい場合(self):
        semver1 = SemVer(1, 4, 2)
        semver2 = SemVer(1, 4, 2)

        self.assertEqual(semver1, semver2)

    def test_等価性を比較できる_等しくない場合(self):
        semver1 = SemVer(1, 4, 2)
        semver2 = SemVer(2, 4, 2)

        self.assertNotEqual(semver1, semver2)


if __name__ == "__main__":
    unittest.main()
