CODE_LEX = {
    'code', 'program', 'function', 'class', 'method', 'variable', 
    'loop', 'debug', 'compile', 'execute', 'script', 'commit', 
    'repository', 'syntax', 'algorithm', 'develop', 'engineer',
    'deploy', 'branch', 'merge', 'git', 'python', 'java', 'ruby','c',
    'cpp','optimize'
}

RESEARCH_LEX = {
    'study', 'paper', 'article', 'hypothesis', 'data', 'analyze', 
    'experiment', 'journal', 'methodology', 'result', 'finding', 
    'abstract', 'literature', 'theory', 'publish', 'citation', 
    'survey', 'statistic', 'model', 'sample', 'validity', 'source'
}


def domain_detection(tokens):
    DOMAIN_LEX={
        'CODE' :CODE_LEX,
        'RESERCH':RESEARCH_LEX
    }
    domain_scores = {domain:0 for domain in DOMAIN_LEX}
    token_set = set(tokens)
    for domain, lexicon in DOMAIN_LEX.items():
        matches = token_set.intersection(lexicon)
        domain_scores[domain] = len(matches)
    best_domain = max(domain_scores, key=domain_scores.get)
    max_score = domain_scores[best_domain]


    THRESHOLD = 2 
    
    if max_score >= THRESHOLD:
        return best_domain
    else:
        return 'UNKNOWN'