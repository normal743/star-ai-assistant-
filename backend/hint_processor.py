from config import MODE_PROMPTS

class HintProcessor:
    def __init__(self):
        self.hint_types = {
            'tone': self.process_tone_hint,
            'length': self.process_length_hint,
            'focus': self.process_focus_hint,
            'style': self.process_style_hint,
            'expertise': self.process_expertise_hint,
            'status': self.process_status_hint
        }

    def process_tone_hint(self, tone, message):
        tone_prefixes = {
            'formal': "In a formal tone, ",
            'casual': "Speaking casually, ",
            'enthusiastic': "With enthusiasm, ",
            'serious': "On a serious note, ",
            'humorous': "In a light-hearted manner, "
        }
        return tone_prefixes.get(tone.lower(), "") + message

    def process_length_hint(self, length, message):
        length_instructions = {
            'brief': "Provide a concise response: ",
            'detailed': "Give a comprehensive explanation: ",
            'normal': ""
        }
        return length_instructions.get(length.lower(), "") + message

    def process_focus_hint(self, focus, message):
        focus_prefixes = {
            'technical': "Focusing on technical aspects, ",
            'practical': "From a practical standpoint, ",
            'theoretical': "In theory, ",
            'example': "Using an example to illustrate, "
        }
        return focus_prefixes.get(focus.lower(), "") + message

    def process_style_hint(self, style, message):
        style_instructions = {
            'analytical': "Analyze the following: ",
            'descriptive': "Describe in detail: ",
            'argumentative': "Present arguments for and against: ",
            'comparative': "Compare and contrast: "
        }
        return style_instructions.get(style.lower(), "") + message

    def process_expertise_hint(self, level, message):
        expertise_prefixes = {
            'beginner': "Explaining for a beginner: ",
            'intermediate': "For someone with intermediate knowledge: ",
            'expert': "From an expert perspective: "
        }
        return expertise_prefixes.get(level.lower(), "") + message

    def process_status_hint(self, status, message):
        status_instructions = {
            'thinking': "Before responding, take a moment to carefully consider the question and organize your thoughts. ",
            'uncertain': "If you're not entirely sure about the answer, express your uncertainty and provide the best information you can. ",
            'creative': "For this response, think outside the box and provide an innovative or unconventional perspective. ",
            'step_by_step': "Please provide a step-by-step explanation or solution to the query. ",
            'summarize': "After providing your response, please summarize the key points briefly. "
        }
        return status_instructions.get(status.lower(), "") + message

    def process_hint(self, hint, message):
        hint_parts = hint.split(':')
        if len(hint_parts) != 2:
            return message
        
        hint_type, hint_value = hint_parts
        hint_type = hint_type.strip().lower()
        hint_value = hint_value.strip().lower()

        if hint_type in self.hint_types:
            return self.hint_types[hint_type](hint_value, message)
        elif hint_type in MODE_PROMPTS:
            return MODE_PROMPTS[hint_type] + " " + message
        else:
            return message

# Usage example:
# hint_processor = HintProcessor()
# user_message = "What is quantum computing?"
# hint = "tone: formal"
# processed_message = hint_processor.process_hint(hint, user_message)
# print(processed_message)
