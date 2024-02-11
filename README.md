# Ragbuilder 😠😡😤

Ragbuilder is a Python package fueled by the fire of frustration and the desire to conquer complexity. It helps you navigate the tumultuous seas of information overload with ease and unleashes your inner warrior against the tyranny of dull content.

## Installation

To harness the raw power of Ragbuilder, simply wield pip:

```bash
pip install Ragbuilder
```

## Usage 🛡️⚔️

```python
from RagBuilder.ragebuilder import LangchainGemeni

# Unleash the fury of Ragbuilder
model = LangchainGemeni(GOOGLE_GEMENI_API, temperature=0.3)

# Convert your enemies... er, PDF pages into vectors
model.AIEmbeddingsPdfPages2Vector('./attention-is-all-you-need-Paper.pdf')

# Summon your trusty Question-Answering guardian
qa_client = model.BuildQA(return_source_documents=True)

# Strike fear into the heart of ignorance with your inquiries
qa_model = qa_client({
    'query': "Tell me about attention in deep learning?"
})

print(qa_model['result'])
```

## Requirements 🧰

- google-generativeai
- langchain-google-genai
- chromadb
- pypdf

## License 📜

Ragbuilder is a battle-tested warrior and is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙌

Ragbuilder stands on the shoulders of giants, fueled by the fury of frustration and the passion for knowledge. It is a tribute to the warriors who dare to challenge the status quo and seek enlightenment amidst chaos.
