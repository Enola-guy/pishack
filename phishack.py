import sublime
import sublime_plugin
import re


class ReplacerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        parsed_urls = []
        self.text = sublime.get_clipboard()
        for line in self.text.split("\n\n"):
            parsed_urls.append(line.strip())
        text = '\n'.join(parsed_urls)
        #self.view.insert(edit, 0, text)
        sublime.set_clipboard(text)