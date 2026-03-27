from cvlib import generate_cv, CVData, ContactInfo, Job, Education, Project, SkillCategory


data = CVData(
    full_name="JOHN DOE",
    headline="Software Engineer | Full Stack Developer",
    contact=ContactInfo(
        email="john.doe@email.com",
        linkedin="linkedin.com/in/johndoe",
        github="github.com/johndoe",
        location="New York, USA",
    ),
    summary=(
        "Software Engineer with 5+ years of experience building scalable web applications and distributed systems. "
        "Proficient in Python, Java, TypeScript, and cloud-native architectures. "
        "Passionate about clean code, test-driven development, and delivering high-impact solutions."
    ),
    jobs=[
        Job(
            title="Senior Software Engineer",
            company="Tech Corp",
            dates="January 2022 - Present",
            bullets=[
                "Architected and deployed microservices platform serving 1M+ daily active users with 99.99% uptime SLA.",
                "Reduced API response latency by 40% through Redis caching, query optimization, and connection pooling.",
                "Led migration from monolithic architecture to event-driven microservices using Kafka and Docker.",
                "Mentored team of 4 junior engineers through code reviews, pair programming, and technical design sessions.",
            ],
            tech="Python, FastAPI, PostgreSQL, Redis, Docker, Kubernetes, AWS",
        ),
        Job(
            title="Software Engineer",
            company="StartupX",
            dates="June 2019 - December 2021",
            bullets=[
                "Built real-time notification system using WebSockets and Redis Pub/Sub, handling 50k+ concurrent connections.",
                "Developed RESTful APIs in Node.js serving mobile and web clients with 200ms p95 response time.",
                "Implemented CI/CD pipelines with GitHub Actions and Docker, reducing deployment time from 2 hours to 15 minutes.",
            ],
            tech="Node.js, Express, MongoDB, React, GitHub Actions, Docker",
        ),
        Job(
            title="Junior Developer",
            company="Digital Agency",
            dates="January 2018 - May 2019",
            bullets=[
                "Developed responsive web applications for 10+ clients using React and TypeScript.",
                "Integrated third-party APIs (Stripe, Twilio, SendGrid) for payment processing and communications.",
            ],
            tech="React, TypeScript, Node.js, PostgreSQL, Stripe API",
        ),
    ],
    education=[
        Education(
            degree="B.S. Computer Science",
            school="Massachusetts Institute of Technology",
            location="Cambridge, MA",
            dates="September 2014 - June 2018",
            gpa="3.8/4.0",
            relevant_coursework=["Algorithms", "Distributed Systems", "Machine Learning", "Database Systems", "Computer Networks"],
        ),
    ],
    projects=[
        Project(
            name="Open Source Analytics Dashboard",
            description="Real-time analytics dashboard with WebSocket streaming, interactive charts, and role-based access control",
            tech="React, TypeScript, Node.js, Redis, PostgreSQL",
            link="https://github.com/johndoe/analytics-dashboard",
        ),
        Project(
            name="Task Scheduler Engine",
            description="Distributed task scheduling system with retry logic, dead-letter queues, and monitoring",
            tech="Python, Celery, RabbitMQ, Docker",
            link="https://github.com/johndoe/task-scheduler",
        ),
        Project(
            name="CLI Database Migration Tool",
            description="Command-line tool for schema versioning and zero-downtime database migrations",
            tech="Go, PostgreSQL, SQLite",
        ),
    ],
    skills=[
        SkillCategory("Backend", "Python (FastAPI, Django), Java (Spring Boot), Node.js (Express, NestJS), Go"),
        SkillCategory("Frontend", "React, TypeScript, Next.js, HTML/CSS, Tailwind CSS"),
        SkillCategory("Databases", "PostgreSQL, MongoDB, Redis, SQLite, DynamoDB"),
        SkillCategory("Cloud & DevOps", "AWS (EC2, S3, Lambda, EKS), Docker, Kubernetes, Terraform, GitHub Actions, CI/CD"),
        SkillCategory("Architecture", "Microservices, Event-Driven, REST, GraphQL, Clean Architecture, TDD"),
    ],
    languages="English (Native) | Spanish (B2) | French (A2)",
)


if __name__ == "__main__":
    generate_cv(data, "John_Doe_CV.docx", pdf=True)
