def match_resume(resume_skills: list, job_skills: list) -> dict:
    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))
    score = len(matched) / len(job_skills)
    return {"match_score": round(score, 2), "matched": matched, "missing": missing}

if __name__ == "__main__":
    print(match_resume(["Python", "SQL", "Pandas"], ["Python", "SQL", "Docker", "PyTorch"]))
