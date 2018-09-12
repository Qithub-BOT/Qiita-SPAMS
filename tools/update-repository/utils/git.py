#!/usr/bin/env python
# coding: utf-8

import delegator


class GitUtility(object):

    def __init__(self):

        return

    def _check_git_exists(self):
        """Gitが存在するかを確認し、なければIOErrorをraiseする"""

        proc = delegator.run("which git")

        if proc.return_code == 0:
            return True

        else:
            raise IOError("fatal: Gitが存在しません。プログラムを終了します")
