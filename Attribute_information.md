# Attribute Information

The Breast Cancer Wisconsin (Original) dataset includes features derived from Fine Needle Aspirate (FNA) samples of breast masses. Each attribute represents a specific characteristic of the cell nuclei present in the sample. The values for these attributes range from 1 to 10, indicating the relative severity or extent of the characteristic observed, with 1 being the least severe and 10 being the most severe. 

Description of each attribute and its biological significance:

**1. Clump Thickness:**
- **Description:** Measures the thickness of the cell clumps.
- **Biological Significance:** Thicker clumps of cells can indicate the presence of malignant tumors, as cancerous cells tend to clump together more densely compared to benign cells.
- **Scale (1-10):** 1 indicates thinner clumps, while 10 indicates very thick clumps.

**2.	Uniformity of Cell Size:**
- **Description:** Assesses the variation in cell size.
- **Biological Significance:** Cancer cells often vary greatly in size, whereas benign cells tend to be more uniform. High variability (high score) can be a sign of malignancy.
- **Scale (1-10):** 1 indicates uniform cell sizes, while 10 indicates highly variable cell sizes.

**3.	Uniformity of Cell Shape:**
- **Description:** Assesses the variation in cell shape.
- **Biological Significance:** Similar to cell size, malignant cells often have varied shapes, while benign cells are more uniform. High variability (high score) can indicate malignancy.
- **Scale (1-10):** 1 indicates uniform cell shapes, while 10 indicates highly variable shapes.

**4.	Marginal Adhesion:**
- **Description:** Measures how closely cells stick to each other.
- **Biological Significance:** Cancer cells tend to lose adhesion and spread more easily compared to benign cells, which stick together more.
- **Scale (1-10):** 1 indicates high adhesion (cells stick together well), while 10 indicates low adhesion (cells do not stick together well).

**5.	Single Epithelial Cell Size:**
- **Description:** Measures the size of single epithelial cells.
- **Biological Significance:** Larger single epithelial cells can indicate malignancy, as cancerous cells often grow larger than normal cells.
- **Scale (1-10):** 1 indicates smaller cell size, while 10 indicates larger cell size.

**6.	Bare Nuclei:**
- **Description:** Counts the number of bare nuclei (nuclei that are not surrounded by cytoplasm).
- **Biological Significance:** A higher number of bare nuclei can be a sign of malignancy, as cancer cells often have more prominent nuclei.
- **Scale (1-10):** 1 indicates fewer bare nuclei, while 10 indicates many bare nuclei.

**7.	Bland Chromatin:**
- **Description:** Describes the texture of the chromatin in the cell nucleus.
- **Biological Significance:** Cancer cells often have coarse, clumpy chromatin, whereas benign cells have finer, more uniform chromatin.
- **Scale (1-10):** 1 indicates finer, more uniform chromatin, while 10 indicates coarse, clumpy chromatin.

**8.	Normal Nucleoli:**
- **Description:** Measures the number of nucleoli (small structures within the nucleus) that are normal.
- **Biological Significance:** Malignant cells often have multiple and prominent nucleoli, whereas benign cells have fewer and less prominent nucleoli.
- **Scale (1-10):** 1 indicates fewer and less prominent nucleoli, while 10 indicates more and prominent nucleoli.

**9.	Mitoses:**
- **Description:** Counts the number of cells undergoing mitosis (cell division).
- **Biological Significance:** A higher rate of mitosis can indicate malignancy, as cancer cells tend to divide more frequently than normal cells.
- **Scale (1-10):** 1 indicates fewer cells undergoing mitosis, while 10 indicates many cells undergoing mitosis.

**10.	Class:**
- **Description:** Indicates whether the tumor is benign or malignant.
- **Biological Significance:** 2 represents benign tumors, while 4 represents malignant tumors.

Each feature is rated on a scale from 1 to 10 based on its appearance under the microscope, with 1 indicating normal/least severe and 10 indicating abnormal/most severe. This scaling helps to standardize the assessment and make it easier for machine learning models to interpret and learn from the data.
