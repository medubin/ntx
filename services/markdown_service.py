# import markdown
# from pygments import highlight
# from pygments.lexers import HtmlLexer
# from pygments.formatters import TerminalTrueColorFormatter

# import re



from base.base_service import BaseService
class MarkdownService(BaseService):
    # mdv.term_columns = 30

# calling like this (all CLI options supported, check def main

    def parse(self, text):
        return text

        # formatted = mdv.main(text)  
        # return formatted
        # return formatted
        # html = markdown.markdown(text)
        # return highlight(html, HtmlLexer(), TerminalTrueColorFormatter())

        # return self.__format_markdown(text)

    
    # def __format_markdown(self, text):
    #     content = []
    #     headers = re.compile("^#+")
    #     for line in text:
    #         match = headers.match(line)
    #         if (match):
    #             content.append(match.group())

    #     return "\n".join(content)
    #         # return headers.match(text) or ''
            






        # return markdown.markdown(text)

    

    # def __markdown2html(self, text):
    #     """Convert markdown file to html"""
    #     return markdown.markdown(text, extensions=[GithubFlavoredMarkdownExtension()])





    # def gfm(self, text):
    #     # Extract pre blocks.
    #     extractions = {}
    #     def pre_extraction_callback(matchobj):
    #         digest = md5(matchobj.group(0)).hexdigest()
    #         extractions[digest] = matchobj.group(0)
    #         return "{gfm-extraction-%s}" % digest
    #     pattern = re.compile(r'<pre>.*?</pre>', re.MULTILINE | re.DOTALL)
    #     text = re.sub(pattern, pre_extraction_callback, text)

    #     # Prevent foo_bar_baz from ending up with an italic word in the middle.
    #     def italic_callback(matchobj):
    #         s = matchobj.group(0)
    #         if list(s).count('_') >= 2:
    #             return s.replace('_', '\_')
    #         return s
    #     text = re.sub(r'^(?! {4}|\t)\w+_\w+_\w[\w_]*', italic_callback, text)

    #     # In very clear cases, let newlines become <br /> tags.
    #     def newline_callback(matchobj):
    #         if len(matchobj.group(1)) == 1:
    #             return matchobj.group(0).rstrip() + '  \n'
    #         else:
    #             return matchobj.group(0)
    #     pattern = re.compile(r'^[\w\<][^\n]*(\n+)', re.MULTILINE)
    #     text = re.sub(pattern, newline_callback, text)

    #     # Insert pre block extractions.
    #     def pre_insert_callback(matchobj):
    #         return '\n\n' + extractions[matchobj.group(1)]
    #     text = re.sub(r'{gfm-extraction-([0-9a-f]{32})\}', pre_insert_callback, text)

    #     return text

    



