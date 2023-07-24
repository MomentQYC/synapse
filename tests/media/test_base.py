# Copyright 2019 New Vector Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import Mock

from synapse.media._base import add_file_headers, get_filename_from_headers

from tests import unittest


class GetFileNameFromHeadersTests(unittest.TestCase):
    # input -> expected result
    TEST_CASES = {
        b"attachment; filename=abc.txt": "abc.txt",
        b'attachment; filename="azerty"': "azerty",
        b'attachment; filename="aze%20rty"': "aze%20rty",
        b'attachment; filename="aze"rty"': 'aze"rty',
        b'attachment; filename="azer;ty"': "azer;ty",
        b"attachment; filename*=utf-8''foo%C2%A3bar": "foo£bar",
    }

    def tests(self) -> None:
        for hdr, expected in self.TEST_CASES.items():
            res = get_filename_from_headers({b"Content-Disposition": [hdr]})
            self.assertEqual(
                res,
                expected,
                f"expected output for {hdr!r} to be {expected} but was {res}",
            )


class AddFileHeadersTests(unittest.TestCase):
    TEST_CASES = {
        "text/plain": b"inline",
        "text/csv": b"inline",
        "text/png": b"inline",
        "text/html": b"attachment; filename=file.name",
        "any/thing": b"attachment; filename=file.name",
    }

    def tests(self) -> None:
        for media_type, expected in self.TEST_CASES.items():
            request = Mock()
            add_file_headers(request, media_type, 0, "file.name")
            request.setHeader.assert_any_call(b"Content-Disposition", expected)
