import keyboard
import pyperclip
import time
import os
from dotenv import load_dotenv
from game_translator import GameTranslator
from langchain_openai.chat_models.base import BaseChatOpenAI

class HotkeyTranslator:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize the LLM and GameTranslator
        llm = BaseChatOpenAI(
            model=os.getenv('MODEL_NAME', 'deepseek-chat'),
            openai_api_key=os.getenv('OPENAI_API_KEY'), 
            openai_api_base=os.getenv('OPENAI_API_BASE'),
            max_tokens=int(os.getenv('MAX_TOKENS', 1024))
        )
        
        prompt = os.getenv('TRANSLATION_PROMPT')
        
        self.translator = GameTranslator(llm=llm, propmt=prompt)
        
    def translate_selection(self):
        # Store original clipboard content
        original_clipboard = pyperclip.paste()
        
        # Simulate Ctrl+A and Ctrl+X to get selected text
        keyboard.send('ctrl+a')
        time.sleep(0.1)  # Small delay to ensure selection is complete
        keyboard.send('ctrl+x')
        time.sleep(0.1)  # Small delay to ensure clipboard is updated
        
        # Get the text from clipboard
        text_to_translate = pyperclip.paste()
        
        if text_to_translate:
            # Clear the conversation history before translation
            self.translator.clear_history()
            
            # Translate the text
            translated_text = self.translator.translate(text_to_translate)
            
            # Put translated text in clipboard
            pyperclip.copy(translated_text)
            
            # Simulate Ctrl+V to paste the translated text
            keyboard.send('ctrl+v')
            
            # Restore original clipboard content
            time.sleep(0.1)  # Small delay before restoring clipboard
            pyperclip.copy(original_clipboard)
    
    def start(self):
        # Register the hotkey (Ctrl+T)
        keyboard.add_hotkey('ctrl+t', self.translate_selection)
        
        print("Hotkey translator started. Press Ctrl+T to translate selected text.")
        print("Press Ctrl+C to exit...")
        
        # Keep the program running
        keyboard.wait('ctrl+c')

if __name__ == "__main__":
    translator = HotkeyTranslator()
    translator.start() 