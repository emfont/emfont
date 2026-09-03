-- 一點明體 I.Ming https://github.com/ichitenfont/I.Ming
-- weights 留空，等原始字型檔 (8.10/I.Ming-8.10.ttf -> IMing/400.ttf) 上傳後由 init / admin upload 補上
INSERT INTO font_family (
    id, name, name_zh, name_en, weights, license, version, description,
    category, family, tags, repo_url, authors, format, languages, demo_content_id
) VALUES (
    'IMing',
    'I.Ming',
    '一點明體',
    'I.Ming',
    ARRAY[]::smallint[],
    'IPA Font License 1.0',
    '8.10',
    '一點明體（I.明體）是一點字坊依照傳承字形標準化文件《傳承字形部件檢校表》推薦字形製作的開源明體，前身為 IPAmj 明朝。收錄超過六萬字，覆蓋 Big5、GB2312、IICore、《通用規範漢字表》與《常用香港外字表》等字集，適合正體中文長文排版。',
    'serif',
    'IPAmj Mincho',
    ARRAY['明體', '傳承字形']::text[],
    'https://github.com/ichitenfont/I.Ming',
    ARRAY['一點字坊 ichitenfont']::text[],
    'ttf',
    '{
      "Common":1346,
      "Latin":563,
      "Bopomofo":77,
      "Inherited":50,
      "Greek":80,
      "Cyrillic":98,
      "Han":57124,
      "Hiragana":375,
      "Katakana":299,
      "private_area":5
    }'::json,
    1
)
ON CONFLICT (id) DO NOTHING;
