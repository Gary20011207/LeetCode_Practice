#!/usr/bin/env python3
"""
LeetCode Problem File Generator

Usage: python leetcode_helper.py <leetcode_url> [language] [base_dir]

Examples:
    python leetcode_helper.py https://leetcode.com/problems/palindrome-number/
    python leetcode_helper.py https://leetcode.com/problems/two-sum/ py
    python leetcode_helper.py https://leetcode.com/problems/add-two-numbers/ c ./leetcode

Interactive mode (manual input):
    python leetcode_helper.py -i
    python leetcode_helper.py --interactive ./leetcode
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error

# Language configuration: file extensions and templates
# langSlug is the language identifier returned by LeetCode API
LANGUAGE_CONFIG = {
    'py': {
        'ext': '.py',
        'langSlug': 'python3',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''class Solution:
    pass
'''
    },
    'python': {
        'ext': '.py',
        'langSlug': 'python3',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''class Solution:
    pass
'''
    },
    'c': {
        'ext': '.c',
        'langSlug': 'c',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''// Solution here
'''
    },
    'cpp': {
        'ext': '.cpp',
        'langSlug': 'cpp',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''class Solution {
public:
    // Solution here
};
'''
    },
    'java': {
        'ext': '.java',
        'langSlug': 'java',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''class Solution {{
    // Solution here
}}
'''
    },
    'js': {
        'ext': '.js',
        'langSlug': 'javascript',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''/**
 * @param {{}}
 * @return {{}}
 */
var solution = function() {{
    // Solution here
}};
'''
    },
    'ts': {
        'ext': '.ts',
        'langSlug': 'typescript',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''function solution(): void {{
    // Solution here
}}
'''
    },
    'go': {
        'ext': '.go',
        'langSlug': 'golang',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''package main

func solution() {
    // Solution here
}
'''
    },
    'rs': {
        'ext': '.rs',
        'langSlug': 'rust',
        'template_with_code': '''{code_snippet}
''',
        'template_no_code': '''impl Solution {{
    // Solution here
}}
'''
    }
}


def extract_slug_from_url(url: str) -> str:
    """Extract problem slug from LeetCode URL"""
    patterns = [
        r'leetcode\.com/problems/([^/]+)',
        r'leetcode\.cn/problems/([^/]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1).rstrip('/')
    
    raise ValueError(f"Invalid LeetCode URL: {url}")


def fetch_problem_info(slug: str) -> dict:
    """Fetch problem info using LeetCode GraphQL API"""
    
    api_url = "https://leetcode.com/graphql"
    
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            difficulty
            content
            codeSnippets {
                lang
                langSlug
                code
            }
        }
    }
    """
    
    payload = json.dumps({
        "query": query,
        "variables": {"titleSlug": slug}
    }).encode('utf-8')
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": f"https://leetcode.com/problems/{slug}/"
    }
    
    req = urllib.request.Request(api_url, data=payload, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            question = data.get('data', {}).get('question')
            if not question:
                raise ValueError(f"Problem not found: {slug}")
            
            return {
                'number': question['questionFrontendId'],
                'title': question['title'],
                'slug': question['titleSlug'],
                'difficulty': question['difficulty'],
                'content': question.get('content', ''),
                'code_snippets': question.get('codeSnippets', [])
            }
    except urllib.error.URLError as e:
        raise ConnectionError(f"Cannot connect to LeetCode API: {e}")


def clean_html(html_content: str) -> str:
    """Clean HTML tags and convert to plain text"""
    if not html_content:
        return "No description available."
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html_content)
    # Handle HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    text = text.replace('&#39;', "'")
    # Clean extra whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()
    
    # Limit length
    if len(text) > 500:
        text = text[:500] + "..."
    
    return text


def sanitize_filename(title: str) -> str:
    """Sanitize title to be used as filename"""
    filename = title.replace(' ', '_')
    filename = re.sub(r'[^\w\-]', '', filename)
    filename = re.sub(r'_+', '_', filename)
    return filename


def get_code_snippet(code_snippets: list, lang_slug: str) -> str:
    """Get code snippet for the specified language"""
    if not code_snippets:
        return None
    
    for snippet in code_snippets:
        if snippet.get('langSlug') == lang_slug:
            return snippet.get('code', '')
    
    return None


def create_problem_file(problem_info: dict, language: str, base_dir: str = ".") -> str:
    """Create problem file"""
    
    if language not in LANGUAGE_CONFIG:
        raise ValueError(f"Unsupported language: {language}. Supported: {', '.join(LANGUAGE_CONFIG.keys())}")
    
    config = LANGUAGE_CONFIG[language]
    
    # Create difficulty folder
    difficulty_dir = os.path.join(base_dir, problem_info['difficulty'])
    os.makedirs(difficulty_dir, exist_ok=True)
    
    # Create filename
    clean_title = sanitize_filename(problem_info['title'])
    filename = f"{problem_info['number']}_{clean_title}{config['ext']}"
    filepath = os.path.join(difficulty_dir, filename)
    
    # Get code snippet
    code_snippet = get_code_snippet(
        problem_info.get('code_snippets', []), 
        config.get('langSlug', '')
    )
    
    # Generate content
    if code_snippet:
        content = config['template_with_code'].format(code_snippet=code_snippet)
    else:
        content = config['template_no_code']
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def interactive_mode(base_dir: str = "."):
    """Interactive mode: manually input problem info"""
    print("\n[Interactive Mode] Enter problem info\n")
    
    while True:
        number = input("Problem number (e.g. 9): ").strip()
        if number.isdigit():
            break
        print("Please enter a valid number")
    
    title = input("Problem title (e.g. Palindrome Number): ").strip()
    if not title:
        title = "Unknown"
    
    while True:
        difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().capitalize()
        if difficulty in ['Easy', 'Medium', 'Hard']:
            break
        print("Please enter Easy, Medium, or Hard")
    
    print(f"\nSupported languages: {', '.join(LANGUAGE_CONFIG.keys())}")
    language = input("Language [py]: ").strip().lower() or 'py'
    if language not in LANGUAGE_CONFIG:
        print(f"Unsupported {language}, using py")
        language = 'py'
    
    slug = title.lower().replace(' ', '-')
    slug = re.sub(r'[^\w\-]', '', slug)
    
    problem_info = {
        'number': number,
        'title': title,
        'slug': slug,
        'difficulty': difficulty,
        'content': '',
        'code_snippets': []
    }
    
    filepath = create_problem_file(problem_info, language, base_dir)
    print(f"\nFile created: {filepath}")
    print("Tip: Use URL mode to auto-fetch LeetCode code template")
    return filepath


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nSupported languages:")
        for lang, config in LANGUAGE_CONFIG.items():
            print(f"  {lang:8} -> {config['ext']}")
        print("\nTip: Use --interactive or -i to enter interactive mode")
        sys.exit(1)
    
    if sys.argv[1] in ['--interactive', '-i']:
        base_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
        interactive_mode(base_dir)
        return
    
    url = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) > 2 else 'py'
    base_dir = sys.argv[3] if len(sys.argv) > 3 else '.'
    
    try:
        print(f"Parsing URL: {url}")
        slug = extract_slug_from_url(url)
        
        print(f"Fetching problem: {slug}")
        problem_info = fetch_problem_info(slug)
        
        print(f"Problem: {problem_info['number']}. {problem_info['title']}")
        print(f"Difficulty: {problem_info['difficulty']}")
        
        filepath = create_problem_file(problem_info, language, base_dir)
        
        print(f"File created: {filepath}")
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ConnectionError as e:
        print(f"Connection error: {e}")
        print("\nTip: Use --interactive or -i to enter interactive mode")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
