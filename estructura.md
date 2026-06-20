ai-support-ticket-analyzer/
│
├── backend/
│
│   ├── app/
│   │
│   ├── domain/
│   │   ├── entities/
│   │   ├── repositories/
│   │   └── value_objects/
│   │
│   ├── application/
│   │   ├── services/
│   │   ├── use_cases/
│   │   └── dto/
│   │
│   ├── infrastructure/
│   │   ├── database/
│   │   ├── repositories/
│   │   ├── ai/
│   │   ├── rag/
│   │   └── loaders/
│   │
│   ├── presentation/
│   │   ├── api/
│   │   ├── schemas/
│   │   └── dependencies/
│   │
│   ├── knowledge_base/
│   │   ├── support_policies.md
│   │   ├── sla.md
│   │   ├── escalation_rules.md
│   │   └── teams.md
│   │
│   ├── tests/
│   │
│   ├── alembic/
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│
│   ├── app/
│   │   ├── dashboard/
│   │   ├── tickets/
│   │   └── assistant/
│   │
│   ├── components/
│   │
│   ├── hooks/
│   │
│   ├── services/
│   │
│   ├── types/
│   │
│   └── lib/
│
├── dataset/
│   └── tickets.csv
│
├── docker-compose.yml
│
├── .env.example
│
├── README.md
│
└── ARCHITECTURE.md
