class BloodPanelAnalyzer:
    def __init__(self):
        # The dictionary is now stored as an attribute of the class.
        # You will need to fill in the rest of the age columns here.
        self.reference_ranges = {
            "Birth": {
                "Hb": (14.0, 22.0),
                "MCV": (100.0, 120.0),
                "MCH": (31.0, 37.0),
                "MCHC": (30.0, 36.0),
                "Reticulocytes": (12.0, 40.0),
                "WBC": (10.0, 26.0),
                "N": (4.0, 14.0),
                "L": (3.0, 8.0),
                "M": (0.5, 2.0),
                "E": (0.1, 1.0),
                "Platelets": (100.0, 450.0)
            },
            "Day-3": {
                "Hb": (15.0, 21.0),
                "MCV": (92.0, 118.0),
                "MCH": (31.0, 37.0),
                "MCHC": (29.0, 37.0),
                "Reticulocytes": (5.0, 35.0),
                "WBC": (7.0, 23.0),
                "N": (3.0, 5.0),
                "L": (2.0, 8.0),
                "M": (0.5, 1.0),
                "E": (0.1, 2.0),
                "Platelets": (210.0, 500.0)
            },
            "Day-7": {
                "Hb": (13.5, 21.5),
                "MCV": (88.0, 126.0),
                "MCH": (31.0, 37.0),
                "MCHC": (28.0, 38.0),
                "Reticulocytes": (5.0, 10.0),
                "WBC": (6.0, 22.0),
                "N": (3.0, 6.0),
                "L": (3.0, 9.0),
                "M": (0.1, 2.0),
                "E": (0.1, 0.8),
                "Platelets": (160.0, 500.0)
            },
            "Day-14": {
                "Hb": (12.5, 20.5),
                "MCV": (86.0, 124.0),
                "MCH": (31.0, 37.0),
                "MCHC": (28.0, 38.0),
                "Reticulocytes": (5.0, 10.0),
                "WBC": (6.0, 22.0),
                "N": (3.0, 7.0),
                "L": (3.0, 9.0),
                "M": (0.1, 2.0),
                "E": (0.1, 0.9),
                "Platelets": (170.0, 500.0)
            },
            "1 month": {
                "Hb": (11.5, 16.5),
                "MCV": (92.0, 116.0),
                "MCH": (30.0, 36.0),
                "MCHC": (29.0, 37.0),
                "Reticulocytes": (2.0, 6.0),
                "WBC": (5.0, 19.0),
                "N": (3.0, 9.0),
                "L": (3.0, 16.0),
                "M": (0.3, 2.0),
                "E": (0.2, 1.0),
                "Platelets": (200.0, 500.0)
            },
            "2 months": {
                "Hb": (9.4, 13.0),
                "MCV": (87.0, 103.0),
                "MCH": (27.0, 33.0),
                "MCHC": (28.0, 35.5),
                "Reticulocytes": (3.0, 5.0),
                "WBC": (5.0, 15.0),
                "N": (1.0, 5.0),
                "L": (4.0, 10.0),
                "M": (0.4, 2.2),
                "E": (0.1, 1.0),
                "Platelets": (210.0, 650.0)
            },
            "3-6 months": {
                "Hb": (11.1, 14.1),
                "MCV": (68.0, 84.0),
                "MCH": (24.0, 30.0),
                "MCHC": (30.0, 36.0),
                "Reticulocytes": (4.0, 10.0),
                "WBC": (6.0, 18.0),
                "N": (1.0, 6.0),
                "L": (4.0, 12.0),
                "M": (0.2, 2.2),
                "E": (0.1, 1.0),
                "Platelets": (200.0, 550.0)
            },
            "1 yr": {
                "Hb": (11.1, 14.1),
                "MCV": (72.0, 84.0),
                "MCH": (25.0, 29.0),
                "MCHC": (32.0, 36.0),
                "Reticulocytes": (3.0, 10.0),
                "WBC": (6.0, 16.0),
                "N": (2.0, 7.0),
                "L": (3.5, 11.0),
                "M": (0.2, 2.2),
                "E": (0.1, 1.0),
                "Platelets": (200.0, 550.0)
            },
            "2-6 yrs": {
                "Hb": (11.0, 14.0),
                "MCV": (75.0, 87.0),
                "MCH": (24.0, 30.0),
                "MCHC": (31.0, 37.0),
                "Reticulocytes": (3.0, 10.0),
                "WBC": (5.0, 15.0),
                "N": (1.5, 8.0),
                "L": (6.0, 9.0),
                "M": (0.2, 2.2),
                "E": (0.1, 1.0),
                "Platelets": (200.0, 490.0)
            },
            "6-12 yrs": {
                "Hb": (11.5, 15.5),
                "MCV": (77.0, 95.0),
                "MCH": (25.0, 33.0),
                "MCHC": (31.0, 37.0),
                "Reticulocytes": (3.0, 10.0),
                "WBC": (5.0, 13.0),
                "N": (2.0, 8.0),
                "L": (1.0, 5.0),
                "M": (0.2, 2.0),
                "E": (0.1, 1.0),
                "Platelets": (170.0, 450.0)
            },
            "Adult": {
                "Hb": (12.5, 16.5),
                "MCV": (80.0, 100.0),
                "MCH": (25.0, 33.0),
                "MCHC": (31.0, 37.0),
                "Reticulocytes": (3.0, 10.0),
                "WBC": (4.0, 11.0),
                "N": (1.5, 8.0),
                "L": (1.0, 4.0),
                "M": (0.1, 1.5),
                "E": (0.1, 0.5),
                "Platelets": (150.0, 450.0)
            }
        }

    def check_index(self, age_group: str, index_name: str, value: float) -> dict:
        """
        Evaluates a single blood index against the reference range.
        """
        if age_group not in self.reference_ranges:
            return {"status": "Error", "message": f"Age group '{age_group}' not found."}

        if index_name not in self.reference_ranges[age_group]:
            return {"status": "Error", "message": f"Index '{index_name}' not found for this age group."}

        min_val, max_val = self.reference_ranges[age_group][index_name]
        try:
            if value < min_val:
                status = "Low"
            elif value > max_val:
                status = "High"
            else:
                status = "Normal"
        except TypeError:
            status = "Error"

        return {
            "index": index_name,
            "status": status,
            "value": value,
            "reference_range": f"{min_val} - {max_val}"
        }

    def evaluate_panel(self, age_group: str, patient_results: dict) -> list:
        """
        Evaluates a full panel (dictionary) of results for a patient.
        Returns a list of dictionaries with the evaluation of each index.
        """
        report = []
        for index_name, value in patient_results.items():
            result = self.check_index(age_group, index_name, value)
            report.append(result)
        return report


# ==========================================
# Example Usage in your Application
# ==========================================

# 1. Instantiate the class
#analyzer = BloodPanelAnalyzer()

# 2. Check a single value
#single_check = analyzer.check_index(age_group="Birth", index_name="Hb", value=13.0)
#print("Single Check Result:")
#print(
   # f"  {single_check['index']}: {single_check['value']} -> {single_check['status']} (Range: {single_check['reference_range']})\n")
