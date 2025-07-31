def compute_spam_probability():
    total_emails = 1000
    free_emails = 300
    spam_emails = 400
    spam_and_free = 120

    p_spam = spam_emails / total_emails
    p_free = free_emails / total_emails
    p_free_given_spam = spam_and_free / spam_emails

    # Bayes' Theorem
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free
    return p_spam_given_free

print(f"Probability email is spam given it contains 'free': {compute_spam_probability():.2f}")
