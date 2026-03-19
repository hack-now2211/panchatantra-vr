from backend.story_data.lion_rabbit import story

class SceneManager:

    def __init__(self):
        self.current_scene = 0

    def get_scene(self):
        return story[self.current_scene]

    def next_scene(self):
        if self.current_scene < len(story) - 1:
            self.current_scene += 1
            return story[self.current_scene]
        else:
            print("\n--- STORY ENDED ---")
            exit()