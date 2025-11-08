# advanced-renaming-python-script
It rename files in bulk based on command-line arguments.


If the Images folder has 5 images as below.

| Name     | Creation Date |
|----------|----------------|
| Dog      | 02-Dec-2024    |
| Ball     | 02-Aug-2024    |
| Cat      | 02-Jan-2024    |
| Elephant | 02-Apr-2024    |
| Apple    | 02-Sep-2024    |

**Example 1**

Running the script to rename files in Images folder **based on the name**.

python advanced_rename_by_name.py "C:\Users\patel\Documents\Images" -p New_Image_Name

Outcome will be as below.

| Name     | Creation Date | New Name          |
|----------|----------------|-------------------|
| Dog      | 02-Dec-2024    | New_Image_Name_4  |
| Ball     | 02-Aug-2024    | New_Image_Name_2  |
| Cat      | 02-Jan-2024    | New_Image_Name_3  |
| Elephant | 02-Apr-2024    | New_Image_Name_5  |
| Apple    | 02-Sep-2024    | New_Image_Name_1  |



**Example 2**

Running the script to rename files in Images folder **based on the creation date**.

python advanced_rename_by_creation_date.py "C:\Users\patel\Documents\Images" -p New_Image_Name


| Name     | Creation Date | New Name            |
|----------|----------------|---------------------|
| Dog      | 02-Dec-2024    | New_Image_Name_5    |
| Ball     | 02-Aug-2024    | New_Image_Name_3    |
| Cat      | 02-Jan-2024    | New_Image_Name_1    |
| Elephant | 02-Apr-2024    | New_Image_Name_2    |
| Apple    | 02-Sep-2024    | New_Image_Name_4    |


