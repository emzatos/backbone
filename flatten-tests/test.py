#!/usr/bin/python3
from subprocess import check_output, STDOUT, CalledProcessError
import sys
import os


def call(cmd):
    try:
        result = check_output(cmd.split(), stderr=STDOUT, timeout=5).decode('utf-8')
    except CalledProcessError as e:
        result = e.output.decode('utf-8') + "exit code: " + str(e.returncode)
    return result


def testall():
    test_names = [x[:-3] for x in os.listdir('.')
                  if x.endswith('.bb')
                  if os.path.isfile(x[:-3] + '.ok')]
    if not test_names:
        print(' nothing to do...')
        return
    for filename in test_names:
        test(filename)


def test(testname):
    print(" --- ", testname, end=" ...")
    output = call('../cmake-build-debug/backbone flatten ' + testname + '.bb')
    with open(testname + ".ok", "r") as f:
        reference = f.read()
    output = output.strip()
    reference = reference.strip()
    if output != reference:
        print(" fail --- ")
        print(" EXPECTED:")
        print(reference)
        print(" FOUND:")
        print(output)
    else:
        print(" pass --- ")


if len(sys.argv) == 1:
    testall()
else:
    test(sys.argv[1])
