#!/usr/bin/env python
# coding: utf-8

import delegator

from unittest import TestCase
from utils.git import GitUtility


class GitUtilityTestCase(TestCase):

    def setUp(self):

        self.git = GitUtility()

    def tearDown(self):

        pass

    def test_exists(self):

        proc = delegator.run("which git")

        if proc.return_code == 0:
            self.assertTrue(self.git._check_git_exists())

        else:
            with self.assertRaises(IOError):
                self.git._check_git_exists()
