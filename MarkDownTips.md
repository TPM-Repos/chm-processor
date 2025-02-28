# Markdown Tips for Wiki.js

This document provides guidelines for formatting Markdown content that will be used in Wiki.js.

## Headers

Use the `#` symbol for headers, with space after the symbol:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

## Text Formatting

- **Bold**: Use double asterisks `**bold text**`
- *Italic*: Use single asterisks `*italic text*`
- ~~Strikethrough~~: Use double tildes `~~strikethrough text~~`
- `Inline code`: Use backticks `` `inline code` ``

## Lists

### Unordered Lists

Use hyphens with a space after:

```markdown
- Item 1
- Item 2
  - Nested item 2.1
  - Nested item 2.2
- Item 3
```

### Ordered Lists

Use numbers followed by a period and space:

```markdown
1. First item
2. Second item
   1. Nested item 2.1
   2. Nested item 2.2
3. Third item
```

## Code Blocks

Use triple backticks with optional language specification:

````markdown
```javascript
function example() {
  console.log('Hello, world!');
}
```
````

## Links

```markdown
[Link text](https://example.com)
```

## Images

Images should follow the Wiki.js convention with paths starting with `/assets/`:

```markdown
![Alt text](/assets/images/example.png)
```

## Tables

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

## Blockquotes

Use the `>` symbol with a space after:

```markdown
> This is a blockquote.
> 
> It can span multiple lines.
```

## Horizontal Rules

Use three or more hyphens, asterisks, or underscores:

```markdown
---
```

## Task Lists

```markdown
- [x] Completed task
- [ ] Incomplete task
```

## Footnotes

```markdown
Here's a sentence with a footnote.[^1]

[^1]: This is the footnote.
```

## Special Wiki.js Features

### Table of Contents

```markdown
[[toc]]
```

### Mermaid Diagrams

````markdown
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
````

### Math Equations (KaTeX)

````markdown
```katex
E = mc^2
```
````

## Important Notes

1. Always leave a blank line before and after block elements (headers, lists, code blocks, etc.)
2. Ensure proper indentation for nested lists (2 spaces)
3. Use relative links when linking to other wiki pages
4. Follow consistent formatting throughout the document