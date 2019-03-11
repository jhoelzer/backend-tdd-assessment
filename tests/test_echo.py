#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def test_help(self):
        process = subprocess.Popen(
            ['python', './echo.py', '-h'],
            stdout=subprocess.PIPE
        )
        stdout, _ = process.communicate()
        usage = open('./USAGE', 'r').read()
        self.assertEquals(stdout, usage)

    def test_upper(self):
        args = ['-u', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)

        args = ['--upper', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)

        self.assertEqual(echo.main(args), 'TESTING TEXT')

    def test_lower(self):
        args = ['-l', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.lower)

        args = ['--lower', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.lower)

        self.assertEqual(echo.main(args), 'testing text')

    def test_title(self):
        args = ['-t', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.title)

        args = ['--title', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.title)

        self.assertEqual(echo.main(args), 'Testing Text')

    def test_all(self):
        args = ['-ult', 'TestINg tEXT']
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertTrue(namespace.lower)
        self.assertTrue(namespace.title)

        self.assertEqual(echo.main(args), 'Testing Text')

    def test_none(self):
        args = ['TestINg tEXT']
        self.assertEqual(echo.main(args), 'TestINg tEXT')


if __name__ == '__main__':
    unittest.main()
