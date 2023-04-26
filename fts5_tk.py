from sqlitefts import fts5
import re,sqlite3

class SimpleTokenizer(fts5.FTS5Tokenizer):
    _p = re.compile(r'\w+', re.UNICODE)

    def tokenize(self, text, flags=None):
        for m in self._p.finditer(text):
            s, e = m.span()
            t = text[s:e]
            l = len(t.encode('utf-8'))
            p = len(text[:s].encode('utf-8'))
            yield t, p, p + l

db = sqlite3.connect(':memory:')
tk = fts5.make_fts5_tokenizer(SimpleTokenizer())
fts5.register_tokenizer(db, 'simple_tokenizer', tk)