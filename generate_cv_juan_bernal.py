from cvlib import (
    Achievement,
    ContactInfo,
    CVData,
    Education,
    Job,
    Project,
    Research,
    SkillCategory,
    generate_cv,
)


contact = ContactInfo(
    email="juan.bernal.2004.gil@gmail.com",
    linkedin="https://linkedin.com/in/juan-andres-bernal/",
    github="https://github.com/JuanBernal13",
    location="Bogotá, Colombia"
)

jobs = [
    Job(
        title="Software Engineer Associate",
        company="Scotiabank",
        dates="February 2026 – Present",
        bullets=[
            "Develop backend services and integrations for banking technology teams, supporting financial operations with reliable and maintainable software.",
            "Work with Java, Spring Boot, AWS, CI/CD pipelines, and microservice-based architectures within a regulated enterprise environment.",
            "Collaborate with cross-functional teams to translate business requirements into scalable technical solutions."
        ],
        tech="Java, Spring Boot, AWS, Microservices, CI/CD, Jenkins, ArgoCD, Jira"
    ),
    Job(
        title="AI Engineer / Backend Engineer",
        company="Nebula Medical",
        dates="August 2025 – February 2026",
        bullets=[
            "Led backend architecture of an AI-driven medical platform using LangChain for multi-model orchestration across Claude, GPT-5, and Gemini, reducing average AI response latency by 35% through intelligent model routing and caching.",
            "Designed and implemented a RAG-based conversational memory system with vector search in Pinecone, enabling persistent clinical chat context, reducing AI hallucination rate, and improving diagnostic response accuracy.",
            "Engineered a scalable Data Access Layer (DAL) with Prisma 7 and PostgreSQL, optimizing complex queries through advanced indexing and caching strategies, sustaining p99 < 500ms and p95 < 200ms under concurrent clinical workloads.",
            "Implemented end-to-end encryption and HIPAA-compliant security protocols across all patient data flows, achieving no critical findings in our internal audits.",
            "Integrated 3+ healthcare interoperability APIs (FHIR R4, SaludTools) enabling seamless data exchange across provider systems and reducing integration overhead by 50%.",
            "Architected and deployed a multi-tenant authentication system using Clerk, reducing onboarding friction for new healthcare organizations by 70%.",
            "Implemented an API Gateway with AWS API Gateway and Lambda functions, reducing API response latency by 80% and decreasing application bundle size."
        ],
        tech="Next.js, LangChain, RAG, Prisma, PostgreSQL, HIPAA, React, AWS Lambda, Deepgram, FHIR, Pinecone, Confluence, Jira, Clerk"
    ),
    Job(
        title="Intern - Software Developer I",
        company="Caseware",
        dates="June 2024 – July 2025",
        bullets=[
            "Engineered integrations within the imports/bindings module of the Caseware platform, a mission-critical data ingestion layer used by 475,000+ professionals across 130 countries, ensuring reliable, schema-compliant data mapping at enterprise scale.",
            "Developed critical backend microservices in Java Spring Boot and Node.js and deployed serverless infrastructure on AWS through CDK, optimizing operational costs. Launched CDK projects from development to production environment.",
            "Led massive data migrations (500k+ records) ensuring transactional atomicity and reliability. Improved data access patterns latency time by 40%.",
            "Implemented reactive components in Angular, reducing application load time by 30% through lazy loading and bundle optimization techniques.",
            "Configured orchestrated deployments in Kubernetes.",
            "Responded to on-call production incidents with rapid triage and resolution for clients.",
            "Led Scrum ceremonies for a 7-developer team, ensuring continuous value delivery for the imports team.",
            "Worked with AWS services such as S3, DynamoDB, EC2, EKS, RDS."
        ],
        tech="Java, Spring Boot, AWS CDK, Angular, Kubernetes, Scrum, DynamoDB, S3, Jira, Agile, Copilot"
    )
]

# Create education
education = [
    Education(
        degree="B.S. Systems and Computing Engineering",
        school="Universidad de los Andes",
        location="Bogotá, Colombia",
        dates="Jan 2021 – June 2025",
        gpa="4.21 / 5.0",
        relevant_coursework=["Transactional Systems", "Software Architecture", "Data Structures and Algorithms", "Business Intelligence", "API Development", "Object-Oriented Programming", "Web Development"]
    ),
    Education(
        degree="B.S. Industrial Engineering",
        school="Universidad de los Andes",
        location="Bogotá, Colombia",
        dates="Jan 2022 – June 2025",
        gpa="4.21 / 5.0",
        relevant_coursework=["Advanced Optimization", "Metaheuristics", "Probabilistic models", "Discrete simulation", "Probabilities and statistics"]
    )
]

# Create projects
projects = [
    Project(
        name="Trove: Local Open-Source Search Engine & MCP Server",
        description="A high-performance local search engine that indexes content across GitHub, Notion, Slack, and local files into a unified vector database. Includes an MCP server implementation that optimizes AI agent workflows.",
        tech="TypeScript, Node.js, SQLite, Electron, React, MCP, Transformers.js, Ollama",
        link="https://github.com/antoinebecker10-afk/Trove"
    ),
    Project(
        name="Aura AI: Intelligent Talent Matching Platform with NLP, GNN & LLMs",
        description="An end-to-end ML platform that transforms talent acquisition by replacing keyword matching with semantic fit. Features multi-modal document understanding, learned skill taxonomy via Knowledge Graphs (Neo4j), and contrastive candidate-job matching using GNN.",
        tech="FastAPI, Next.js, PyTorch (GNN), Neo4j, Qdrant, PostgreSQL, MongoDB, Redis/Celery, LangChain",
        link="https://github.com/JuanBernal13/aura-ai"
    ),
    Project(
        name="CV Generator",
        description="A modular Python library for generating professional CVs in DOCX and PDF format.",
        tech="Python, docx, reportlab",
        link="https://github.com/JuanBernal13/cv_generator"
    ),
    Project(
        name="Sports Betting Prediction Engine - ML Pipeline with Kelly Criterion",
        description="ML pipeline that implements temporal features from historical match data, trains and calibrates ensemble models (Random Forest, XGBoost, LightGBM), and sizes bets using the Kelly Criterion.",
        tech="Python, scikit-learn, XGBoost, LightGBM, pandas, NumPy, matplotlib, seaborn",
        link="https://github.com/JuanBernal13/bet-lck-2025"
    ),
    Project(
        name="Financial Market Alert WebSocket System",
        description="Real-time financial market alert system using WebSocket technology. Implements event-driven architecture with Redis for message brokering and PostgreSQL for data persistence.",
        tech="TypeScript, NestJS, Redis, PostgreSQL, WebSocket, Docker",
        link="https://github.com/JuanBernal13/web-sockets-finance-yahoo"
    ),
    Project(
        name="EV Charging Station Multi-Objective Optimizer",
        description="Developed a high-performance optimization system in Java and C++ for Electric Vehicle charging infrastructure. The system leverages multi-objective algorithms to minimize energy costs while maximizing customer service levels.",
        tech="Java, C++, Optimization Algorithms, Data Modeling"
    ),
    Project(
        name="Enterprise Management Platform (Hogar de Abuelos)",
        description="A comprehensive management platform for facility administration, streamlining operations, records management, and resource allocation.",
        tech="Python, Django, SQLite, HTML/CSS",
        link="https://github.com/je-lopezu1/hogarAbuelos"
    ),
    Project(
        name="Microservice orchestration using Spring Boot and Docker",
        description="Architected a scalable distributed system using Java Spring Cloud (Eureka, Config, Gateway) within an Nx monorepo. Implemented asynchronous messaging via RabbitMQ and resilience patterns with Resilience4j.",
        tech="Spring Boot, Docker, AWS"
    )
]

skills = [
    SkillCategory(
        category="Data Science",
        skills="Python, pandas / NumPy, scikit-learn, Statistical Modeling, Feature Engineering, Data Visualization, Experiment Design"
    ),
    SkillCategory(
        category="Machine Learning & AI",
        skills="LLM Development, RAG Systems, LangChain, Prompt Engineering, PyTorch, TensorFlow / Keras, XGBoost / LightGBM, Graph Neural Networks"
    ),
    SkillCategory(
        category="Data Engineering",
        skills="Data Pipelines, ETL / ELT, SQL, Data Modeling, Apache Airflow, RabbitMQ, Event-Driven Data Flows"
    ),
    SkillCategory(
        category="Databases",
        skills="PostgreSQL, MySQL, MongoDB, DynamoDB, Redis, Pinecone, Neo4j, Qdrant"
    ),
    SkillCategory(
        category="MLOps & Cloud",
        skills="AWS, Docker, Kubernetes, GitHub Actions, Model Serving APIs, Monitoring & Observability"
    ),
    SkillCategory(
        category="Backend & APIs",
        skills="FastAPI, Node.js / NestJS, Java / Spring Boot, REST APIs, GraphQL, Microservices"
    ),
    SkillCategory(
        category="Soft Skills & Tools",
        skills="English, Technical Communication, Scrum, Design Thinking, Confluence & Jira"
    )
]

research = [
    Research(
        title="Biological Predictive Modeling (B.S. Thesis)",
        description="Developed predictive models for complex biological data using machine learning techniques, applying advanced preprocessing (PCA), class balancing, and Deep Learning (TensorFlow/Keras) to achieve 98% accuracy.",
        date="2025 - I",
        link="https://hdl.handle.net/1992/76592"
    ),
    Research(
        title="Analytics Forum 2025",
        description="Showcased undergraduate thesis findings at the 2025 Analytics Forum, presenting advanced machine learning applications in bioinformatics to an audience of industry experts and researchers.",
        date="2025 - I"
    ),
    Research(
        title="COPA Research Group Presentation",
        description="Speaker at the Center for Optimization and Applied Probability (COPA) to discuss the integration of neural networks and probabilistic modeling in biological systems.",
        date="2025 - I"
    )
]

achievements = [
    Achievement(
        title="Finalista - Quala Business Challenge",
        description="Finalist in the Quala Business Challenge 2025-1, competing against top business and engineering students in a case-based competition.",
        date="2025-1"
    ),
    Achievement(
        title="ICFES Saber 11 Score",
        description="Achieved a score of 466/500 on Colombia's national high school exit exam.",
        date="2020"
    )
]

cv_data = CVData(
    full_name="Juan Bernal",
    headline="Software & Industrial Engineer | AI Enthusiast",
    contact=contact,
    summary="I am a Software and Industrial Engineer specializing in the architecture of high-scale distributed systems and AI-driven ecosystems. By integrating Industrial Engineering principles, I treat software development as a rigorous optimization process where efficiency, scalability, and long-term reliability are engineered into the foundation.",
    jobs=jobs,
    education=education,
    projects=projects,
    skills=skills,
    research=research,
    achievements=achievements,
    languages="English (Fluent C1), Spanish (Native)"
)

generate_cv(cv_data, "cv_juan_bernal_en.docx", pdf=True)
print("CV generated successfully!")
