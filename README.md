<p align="center">
  <img src="https://ninamcunha.github.io/my-portfolio/images/icon_amooora.jpg" width="200" alt="Amooora Logo" style="border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
</p>

# Amooora Connection Algorithm Project

**[Explore the interactive demo](https://amooora.streamlit.app/)**

## 🌈 Project Motivation

Amooora is building Brazil's first dedicated platform for LGBTQ+ women, transgender, and non-binary individuals to find meaningful connections and community. This technical exploration uses existing dating platform data to develop connection algorithms that will later be adapted for our specific community context.

**Key Motivations:**
- Address the lack of dedicated platforms for LGBTQ+ women in Brazil
- Develop ethical matching algorithms focused on authentic connections
- Create technical foundations for our future platform
- Explore how machine learning can foster community belonging

## 🔍 Project Overview

We analyzed an OkCupid dataset (filtered to 24,117 female/non-male profiles) to develop and test connection algorithms through three technical pillars:

1. **Core Matching Algorithm** (Clustering models)
2. **Text Processing Pipeline** (Topic modeling approaches)
3. **Visualization System** (CNN proof-of-concept)

## 🧠 Methodology

### Data Preparation
- Filtered original 60K profile dataset to non-male users
- Processed 31 features including demographics, interests, and open-text responses
- Cleaned and normalized text data (tokenization, lemmatization)

### Model Exploration

#### 1. Connection Algorithms
| Model | Approach | Key Insight |
|-------|----------|-------------|
| KNN | Distance-based similarity | Struggled with high-dimensional data |
| K-Means | Thematic clustering | Required two-stage implementation |
| **DBSCAN** | Density-based communities | Best performance - naturally identified organic groups |

#### 2. Text Processing
Evaluated 8 approaches including:
- LDA Topic Modeling (2 & 5 topics)
- BERT-based classifiers
- PCA + Word2Vec/TF-IDF reductions

**Top Performers:**
1. 2 LDA Topics (Highest Silhouette score: 0.51)
2. PCA SDV (Best balanced performance)
3. PCA Word2Vec (Strong alternative)

#### 3. Image Processing (Proof of Concept)
- Synthetic profile visualization using:
  - Age detection (OpenCV/Caffe)
  - Gender classifier (TensorFlow/Keras)
- *Note: Uses separate face dataset, not OkCupid images*

## 🏆 Key Findings

**Optimal Model Architecture:**
```mermaid
graph TD
    A[Raw Profiles] --> B[Text Processing]
    A --> C[Feature Selection]
    B --> D[2 LDA Topics]
    C --> E[Demographic Filters]
    D & E --> F[DBSCAN Clustering]
    F --> G[5 Recommendations]
``` 

## 👥 Team

<table style="border:none; border-collapse: collapse; margin-bottom: 20px;">
  <tr style="border:none;">
    <td style="border:none; padding:0; width:150px; vertical-align:top;">
      <img src="images/img_nina.png" width="150" style="border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    </td>
    <td style="border:none; padding:0 0 0 20px; vertical-align:top;">
      <h3>Nina Menezes Cunha</h3>
      Data scientist with 10+ years of experience in machine learning and impact evaluation. Stanford Ph.D. in Economics of Education, former Senior Researcher at FHI 360 and World Bank consultant. Founder of Amooora.
      <br><br>
      <a href="https://github.com/ninamcunha" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github" alt="GitHub">
      </a>
    </td>
  </tr>
</table>

<table style="border:none; border-collapse: collapse; margin-bottom: 20px;">
  <tr style="border:none;">
    <td style="border:none; padding:0; width:150px; vertical-align:top;">
      <img src="images/img_thais.jpeg" width="150" style="border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    </td>
    <td style="border:none; padding:0 0 0 20px; vertical-align:top;">
      <h3>Thais Felipelli</h3>
      Mechatronics engineer and MIT MBA with venture capital experience. Specializes in LIMS systems and startup development. Passionate about data-driven solutions.
      <br><br>
      <a href="https://github.com/tfelipelli" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github" alt="GitHub">
      </a>
    </td>
  </tr>
</table>

<table style="border:none; border-collapse: collapse;">
  <tr style="border:none;">
    <td style="border:none; padding:0; width:150px; vertical-align:top;">
      <img src="images/img_andre.jpeg" width="150" style="border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    </td>
    <td style="border:none; padding:0 0 0 20px; vertical-align:top;">
      <h3>André Menezes</h3>
      Multidisciplinary professional turned tech specialist. Former Le Wagon instructor with expertise in web development and data science. Focused on AI product development.
      <br><br>
      <a href="https://github.com/dedemenezes" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github" alt="GitHub">
      </a>
    </td>
  </tr>
</table>
