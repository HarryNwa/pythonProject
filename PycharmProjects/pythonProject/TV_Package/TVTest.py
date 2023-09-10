import unittest
from TV_Package.TV import Television


class TVTest(unittest.TestCase):

    def test_that_tv_exists(self):
        samsung = Television()
        self.assertIsNotNone(samsung)

    def test_that_tv_can_turn_on(self):
        samsung = Television()
        samsung.turn_on()
        self.assertTrue(samsung.is_on)

    def test_that_tv_can_turn_off(self):
        samsung = Television()
        samsung.turn_off()
        self.assertFalse(samsung.is_on)

    def test_that_tv_can_change_to_next_channel(self):
        samsung = Television()

        samsung.turn_on()
        self.assertTrue(samsung.is_on)

        samsung.set_channel(23)
        samsung.channel_up()
        samsung.channel_up()

        new_channel = samsung.get_channel()
        self.assertEqual(25, new_channel)

    def test_that_tv_can_change_to_previous_channel(self):
        samsung = Television()

        samsung.turn_on()
        self.assertTrue(samsung.is_on)

        samsung.set_channel(23)
        samsung.channel_down()
        samsung.channel_down()

        new_channel = samsung.get_channel()
        self.assertEqual(21, new_channel)

    def test_that_tv_can_increase_volume(self):
        samsung = Television()

        samsung.turn_on()
        self.assertTrue(samsung.is_on)

        samsung.set_volume(23)
        samsung.volume_up()
        samsung.volume_up()

        increase_volume = samsung.get_volume()
        self.assertEqual(25, increase_volume)

    def test_that_tv_can_decrease_volume(self):
        samsung = Television()

        samsung.turn_on()
        self.assertTrue(samsung.is_on)

        samsung.set_volume(23)
        samsung.volume_down()
        samsung.volume_down()

        increase_volume = samsung.get_volume()
        self.assertEqual(21, increase_volume)