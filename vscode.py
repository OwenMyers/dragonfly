from dragonfly import (Grammar, 
                       AppContext, 
                       MappingRule, 
                       Dictation, 
                       InegerRef)

visual_studio_code_context_1 = AppContext(executable="vscode")
visual_studio_code_context_2 = AppContext(executable="visual studio code")

grammar = Grammar("vscode", context = (visual_studio_code_context_1 | visual_studio_code_context_2))

visual_studio_code_rule = MappingRule(
        name = "visual_studio_code",
        mapping = {
                    "end of line": Key("s-$"),
                    "quick open": Key("c-p"),
                    "toggle side bar": Key("c-b"),
                    "command palette": Key("c-s-p"),
                  },
        extras = [
                    Dictation("text"),
                 ],
)

grammar.add_rule(bash_rule)
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

