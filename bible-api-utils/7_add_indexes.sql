-- Performance indexes for Bible API
-- Run this with: wrangler d1 execute bible_data --remote --file=7_add_indexes.sql

-- Verses table indexes
CREATE INDEX IF NOT EXISTS idx_verses_uid ON verses(uid);
CREATE INDEX IF NOT EXISTS idx_verses_book_code ON verses(book_code);
CREATE INDEX IF NOT EXISTS idx_verses_chapter ON verses(chapter_num);
CREATE INDEX IF NOT EXISTS idx_verses_verse ON verses(verse_num);
CREATE INDEX IF NOT EXISTS idx_verses_text ON verses(text);

-- Entities table indexes
CREATE INDEX IF NOT EXISTS idx_entities_uid ON entities(uid);
CREATE INDEX IF NOT EXISTS idx_entities_name ON entities(entity_name);
CREATE INDEX IF NOT EXISTS idx_entities_type ON entities(entity_type);

-- Topics table indexes
CREATE INDEX IF NOT EXISTS idx_topics_uid ON topics(uid);
CREATE INDEX IF NOT EXISTS idx_topics_name ON topics(topic_name);

-- Lexicon table indexes
CREATE INDEX IF NOT EXISTS idx_lexicon_uid ON lexicon(uid);
CREATE INDEX IF NOT EXISTS idx_lexicon_strongs ON lexicon(strongs_number);
CREATE INDEX IF NOT EXISTS idx_lexicon_word ON lexicon(word);

-- Relationships table indexes
CREATE INDEX IF NOT EXISTS idx_relationships_verse ON relationships(verse_uid);
CREATE INDEX IF NOT EXISTS idx_relationships_target ON relationships(target_uid);
CREATE INDEX IF NOT EXISTS idx_relationships_type ON relationships(relationship_type);

-- Books table indexes
CREATE INDEX IF NOT EXISTS idx_books_code ON books(book_code);

-- Composite indexes for common queries
CREATE INDEX IF NOT EXISTS idx_verses_book_chapter ON verses(book_code, chapter_num);
CREATE INDEX IF NOT EXISTS idx_relationships_verse_type ON relationships(verse_uid, relationship_type);
