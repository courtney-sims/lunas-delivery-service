import builtins
import mock
import unittest

import introScene


class TestIntroScene(unittest.TestCase):

    def testFunctionalRun(self):
#want to be testing that we print the next scene
        test_scene = introScene.IntroScene()
        test_scene.run()
        with mock.patch("introScene.input", return_value=1):
            self.assertIsIntance(nextScene, Scene)
            self.assertIsInstance(nextScene, Traffic)

    def testUnitGetNextScene(self):
        test_scene = introScene.IntroScene()
        self.assertEqual(test_scene.get_next_scene(2), "Bistro")

    def testUnitGetUserInput(self):
        test_scene = introScene.IntroScene()
        with mock.patch("introScene.input", return_value="3"):
            self.assertEqual(test_scene.get_user_input(), "3")
    
