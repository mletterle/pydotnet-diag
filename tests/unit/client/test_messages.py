import unittest
from pydotnet_diag.client import messages, commands

class TestMessages(unittest.TestCase):

    def test_default_msg(self):
        msg = messages.DiagnosticMsg()

        self.assertEqual(msg.payload, None)
        self.assertEqual(msg.size, 20)
        self.assertEqual(msg.to_bytes(), b'DOTNET_IPC_V1\x00\x14\x00\x00\x00\x00\x00')

    def test_command_set(self):
        msg = messages.DiagnosticMsg()
        msg.command_set = commands.CommandSet.EVENTPIPE
        self.assertEqual(msg.to_bytes(), b'DOTNET_IPC_V1\x00\x14\x00\x02\x00\x00\x00')

    def test_command_id(self):
        msg = messages.DiagnosticMsg()
        msg.command_id = commands.EventPipeCommandId.COLLECT_TRACING
        self.assertEqual(msg.to_bytes(), b'DOTNET_IPC_V1\x00\x14\x00\x00\x02\x00\x00')

    def test_payload(self):
        msg = messages.DiagnosticMsg()
        our_payload = b'Test Payload'
        msg.payload = our_payload

        self.assertEqual(msg.payload, our_payload)
        self.assertEqual(msg.size, 32)
        self.assertEqual(msg.to_bytes(), b'DOTNET_IPC_V1\x00\x20\x00\x00\x00\x00\x00Test Payload')



