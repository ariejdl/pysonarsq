#!/usr/bin/env python
""" generated source for module Demo """
# package: org.yinwang.pysonar.demos

from org.jetbrains.annotations import NotNull
from pysonarsq.java.Analyzer import Analyzer
from pysonarsq.java.FancyProgress import FancyProgress
from pysonarsq.java._ import _

from java.io import File

from java.util import List

from Linker import Linker
from Styler import Styler
from StyleApplier import StyleApplier
from HtmlOutline import HtmlOutline

import os

class Demo(object):
    OUTPUT_DIR = None # File()

    CSS = "body { color: #666666; } \n" + "a {text-decoration: none; color: #5A82F7}\n" + "table, th, td { border: 1px solid lightgrey; padding: 5px; corner: rounded; }\n" + ".builtin {color: #B17E41;}\n" + ".comment, .block-comment {color: #aaaaaa; font-style: italic;}\n" + ".constant {color: #888888;}\n" + ".decorator {color: #778899;}\n" + ".doc-string {color: #aaaaaa;}\n" + ".error {border-bottom: 1px solid red;}\n" + ".field-name {color: #2e8b57;}\n" + ".function {color: #4682b4;}\n" + ".identifier {color: #8b7765;}\n" + ".info {border-bottom: 1px dotted RoyalBlue;}\n" + ".keyword {color: #0000cd;}\n" + ".lineno {color: #aaaaaa;}\n" + ".number {color: #483d8b;}\n" + ".parameter {color: #777777;}\n" + ".string {color: #999999;}\n" + ".type-name {color: #4682b4;}\n" + ".warning {border-bottom: 1px dotted orange;}\n"
    
    JS = "<script language=\"JavaScript\" type=\"text/javascript\">\n" + \
        "var highlighted = new Array();\n" + \
        "function highlight()\n" + \
        "{\n" + \
        "    // debugger; \n" + \
        "    // console.log(arguments); \n" + \
        "    // clear existing highlights\n" + \
        "    for (var i = 0; i < highlighted.length; i++) {\n" + \
        "        var elm = document.getElementById(highlighted[i]);\n" + \
        "        if (elm != null) {\n" + \
        "            elm.style.backgroundColor = 'white';\n" + \
        "        }\n" + \
        "    }\n" + \
        "    highlighted = new Array();\n" + \
        "    for (var i = 0; i < arguments.length; i++) {\n" + \
        "        var elm = document.getElementById(arguments[i]);\n" + \
        "        if (elm != null) {\n" + \
        "            elm.style.backgroundColor='gold';\n" + \
        "        }\n" + \
        "        highlighted.push(arguments[i]);\n" + \
        "    }\n" + \
        "} </script>\n"
        
    analyzer = Analyzer()
    rootPath = str()
    linker = Linker()

    def makeOutputDir(self):
        if not os.path.exists(self.OUTPUT_DIR):
            raise Exception('create ' + self.OUTPUT_DIR)

    def start(self, fileOrDir):
        rootDir = _.parentFile(fileOrDir) if os.path.isfile(fileOrDir) else fileOrDir
        try:
            self.rootPath = _.unifyPath(rootDir)
        except Exception as e:
            _.die("File not found: " + fileOrDir)
        self.analyzer = Analyzer()
        _.msg("Loading and analyzing files")
        self.analyzer.analyze(_.unifyPath(fileOrDir))
        self.analyzer.finish()
        self.generateHtml()
        self.analyzer.close()

    def generateHtml(self):
        _.msg("\nGenerating HTML")
        
        self.makeOutputDir()
        self.linker = Linker(self.rootPath, self.OUTPUT_DIR)
        self.linker.findLinks(self.analyzer)
        rootLength = len(self.rootPath)

        _.msg("\nGenerating HTML")
        
        total = 0
        for path in self.analyzer.getLoadedFiles():
            if path.startswith(self.rootPath):
                total += 1
                
        progress = FancyProgress(total, 50)
        for path in self.analyzer.getLoadedFiles():
            if path.startswith(self.rootPath):
                progress.tick()
                destFile = _.joinPath(self.OUTPUT_DIR, path.replace(self.rootPath, ''));
                destPath = os.path.abspath(destFile) + ".html";
                html = self.markup(path);                
                _.writeFile(destPath, html)
        _.msg("\nWrote " + str(len(self.analyzer.getLoadedFiles())) + " files to " + self.OUTPUT_DIR)

    def markup(self, path):
        source = str()
        try:
            source = _.readFile(path)
        except Exception as e:
            _.die("Failed to read file: " + path)
            return ""
        styles = Styler(self.analyzer, self.linker).addStyles(path, source)
        styles += self.linker.getStyles(path)
        styledSource = StyleApplier(path, source, styles).apply()
        outline = HtmlOutline(self.analyzer).generate(path)
        
        sb = []
        sb.append("<html><head title=\"")
        sb.append(path)
        sb.append("\">")
        sb.append("<style type='text/css'>\n")
        sb.append(self.CSS)
        sb.append("</style>\n")
        sb.append(self.JS)
        sb.append("</head>\n<body>\n")
        sb.append('<table width=100% border="1px solid gray"><tr><td valign="top">')
        sb.append(outline)
        sb.append("</td><td>")
        sb.append("<pre>")
        sb.append(self.addLineNumbers(styledSource))
        sb.append("</pre>")
        sb.append("</td></tr></table></body></html>")
        
        return ''.join(sb)

    def addLineNumbers(self, source):
        result = []
        count = 1
        for line in source.split(u"\n"):
            result.append(u"<span class='lineno'>")
            result.append(str(count).encode('utf-8'))
            result.append(u"</span> ")
            result.append(line.encode('utf-8'))
            result.append(u"\n")
            
            count += 1
            
        return u''.join(map(lambda s: s.encode('utf-8'), result))

    @classmethod
    def usage(cls):
        _.msg("Usage:  java -jar pysonar-2.0-SNAPSHOT.jar <file-or-dir> <output-dir>")
        _.msg("Example that generates an index for Python 2.7 standard library:")
        _.msg(" java -jar pysonar-2.0-SNAPSHOT.jar /usr/lib/python2.7 ./html")
        import sys
        sys.exit(0)

    @classmethod
    def checkFile(cls, path):
        if not os.path.exists(path):
            _.die("Path not found or not readable: " + path)
        return path

    @classmethod
    def main(cls, args):
        if not len(args):
            cls.usage()
        fileOrDir = cls.checkFile(args[0])
        cls.OUTPUT_DIR = args[1]
        Demo().start(fileOrDir)
        _.msg(_.getGCStats())


if __name__ == '__main__':
    import sys
    Demo.main(sys.argv)

