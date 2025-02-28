# Wiki.js Authoring Standards

This document outlines the standards and best practices for authoring content in Wiki.js. Following these guidelines ensures consistency across all documentation and improves readability.

## Document Structure

### Page Organization

1. **Title**: Every page must begin with a level 1 heading (`# Title`).
2. **Introduction**: A brief introduction should follow the title, explaining the purpose of the page.
3. **Table of Contents**: For longer documents, include a table of contents using `[[toc]]`.
4. **Sections**: Organize content into logical sections using appropriate heading levels.
5. **Conclusion**: When appropriate, end with a summary or conclusion section.

### Heading Hierarchy

- Use heading levels sequentially (don't skip levels)
- Avoid having only one subheading within a section
- Keep headings concise and descriptive
- Maximum heading level: h4 (####)

## Content Guidelines

### Text Formatting

- Use **bold** for emphasis on important terms or concepts
- Use *italics* for slight emphasis or to highlight terms
- Use `code formatting` for:
  - Code snippets
  - File names
  - Command line inputs
  - Technical parameters
- Avoid using underlines or all caps for emphasis

### Lists

- Use ordered lists (1., 2., 3.) for sequential steps or prioritized items
- Use unordered lists (- item) for non-sequential items
- Maintain consistent capitalization and punctuation within lists
- Limit nesting to 3 levels for readability

### Code Blocks

- Always specify the language for syntax highlighting
- Use fenced code blocks with triple backticks
- Include comments in code examples when necessary for clarity
- For terminal commands, indicate the prompt symbol ($ for user, # for root)

### Links and References

- Use descriptive link text that indicates the destination
- Avoid generic phrases like "click here" or "read more"
- Use relative links for internal wiki pages
- For external links, consider if they will remain stable over time

### Images

- All images must be stored in the `/assets/` directory
- Include descriptive alt text for accessibility
- Optimize images for web before uploading
- Use consistent naming convention: `topic-description-date.extension`
- Caption images when additional context is needed

## Technical Standards

### File Naming

- Use lowercase for all file names
- Use hyphens instead of spaces or underscores
- Keep file names concise but descriptive
- Include version numbers when appropriate

### Metadata

- Include appropriate tags for categorization
- Set the correct permissions level for the content
- Specify authors when multiple contributors are involved

### Versioning

- Indicate when content was last updated
- Note major changes in a changelog section when appropriate
- Use version numbers for documents that undergo significant revisions

## Language and Style

### Voice and Tone

- Use a professional, clear, and concise writing style
- Write in active voice when possible
- Address the reader directly using "you" rather than "the user"
- Maintain a consistent tone throughout the documentation

### Grammar and Mechanics

- Use present tense when possible
- Write in complete sentences
- Use Oxford commas in lists
- Capitalize proper nouns and the first word of sentences
- Spell out acronyms on first use with the acronym in parentheses

### Technical Terminology

- Define technical terms on first use
- Maintain a glossary for frequently used technical terms
- Use industry-standard terminology consistently
- Avoid jargon when simpler terms will suffice

## Accessibility

- Structure content with proper heading hierarchy
- Provide alt text for all images
- Use sufficient color contrast for text
- Avoid conveying information through color alone
- Create descriptive links that make sense out of context

## Review Process

- All new content should undergo peer review before publishing
- Technical accuracy should be verified by subject matter experts
- Content should be checked for adherence to these standards
- Regular audits of existing content should be conducted to ensure ongoing compliance