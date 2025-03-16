import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import cx_Oracle as co

def connect_to_oracle(username, password, host, port):
    dsn = co.makedsn(host, port)
    conn = co.connect(username, password, dsn)
    return conn
# def check_box():
#     aaaaa= """<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
#     <script type="text/javascript">
#     $(document).ready(function(){
#         $("#newrows").click(function(){
#             var addcontrols = "<tr align="center">"
#         addcontrols += "<td><input type="text"></td>"
#         addcontrols += "<td><input type="text"></td>"
#         addcontrols += "<td><input type="text"></td>"
#         addcontrols += "<td><input type="text"></td>"
#         addcontrols += "<td><input type="text"></td>"
#         addcontrols += "<td><input type="checkbox" name=""></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#         addcontrols += "<td><input type="checkbox"></td>"
#             addcontrols += "</tr>";
#             $("table tbody").append(addcontrols);
#         });
#     });
#     </script>
#     """


# Define your HTML table
html_table = """
<table border="1">
    <thead>
    <tr align="center">
        <th rowspan="4">CMO</th>
        <th rowspan="4">Manufacturing Site</th>
        <th rowspan="4">Address</th>
        <th rowspan="4">City</th>
        <th rowspan="4">Country</th>
        <th rowspan="3" colspan="11">Offered Services</th>
        <th rowspan="3" colspan="13">Manufactured product types</th>
        <th rowspan="3" colspan="6">Accreditations</th>
        <th colspan="36">Bulk Production</th>
        <th rowspan="2" colspan="6">Primary Packaging</th>
        <th rowspan="3" colspan="14">Secondary Packaging</th>
    </tr>
    <tr align="center">
        <th colspan="13">Sterile</th>
        <th colspan="23">Non-Sterile</th>				
    </tr>
    <tr align="center">
        <th colspan="9">Liquide</th>
        <th colspan="4">Lyophilized</th>
        <th colspan="6">Liquide</th>
        <th colspan="11">Solid</th>
        <th colspan="6">Semi-Solid</th>
        <th rowspan="1" colspan="6">Solids/Semi-solids</th>
    </tr>
    <tr align="center">
        <th>GMP Warehouse</th>
        <th>GDP Warehouse</th>
        <th>QC Lab - Micro</th>
        <th>QC Lab - Phisical/Chemical</th>
        <th>QC Lab - Biological</th>
        <th>QP Release</th>
        <th>Development/ Pilot Production</th>
        <th>API production</th>
        <th>Bulk Production</th>
        <th>Packaging</th>
        <th>Other*</th>
        <th>Biologics</th>
        <th>Chemical</th>
        <th>Herbal</th>
        <th>Vaccines</th>
        <th>Onco/ Cytotoxic</th>
        <th>Hormons</th>
        <th>Probiotics</th>
        <th>Cosmetics</th>
        <th>Beta Lactam</th>
        <th>Food Supplements</th>
        <th>VET - Veterinarian</th>
        <th>Narcotics</th>
        <th>Other*</th>
        <th>EMA approval</th>
        <th>FDA approval</th>
        <th>ISO 13485</th>
        <th>EU GMP </th>
        <th>FSSC 22000</th>
        <th>Other*</th>
        <th>Vials</th>
        <th>Syrings</th>
        <th>Ampouls</th>
        <th>Spray</th>
        <th>Drops</th>
        <th>Single dose</th>
        <th>Bottles</th>
        <th>Ophthalmic Ointments</th>
        <th>Other*</th>
        <th>Vials</th>
        <th>Ampouls</th>
        <th>Bottles</th>
        <th>Other*</th>
        <th>Drops</th>
        <th>Bottles</th>
        <th>Spray</th>
        <th>Sache</th>
        <th>Syrup</th>
        <th>Other*</th>
        <th>Tablets</th>
        <th>Film Coated Tablets</th>
        <th>Bi-/Multi-layer Tablets</th>
        <th>Sugar Coated Tablets</th>
        <th>Effervescent Tablets</th>
        <th>ODT - Orally Disintegrating Tablets</th>
        <th>Pallets</th>
        <th>Powder</th>
        <th>Capsules</th>
        <th>Granulates</th>
        <th>Other*</th>
        <th>Ointment</th>
        <th>Cream</th>
        <th>Soft Capsules</th>
        <th>Gels</th>
        <th>Suppositories</th>
        <th>Other*</th>
        <th>Bottles</th>
        <th>Blisters</th>
        <th>Sache</th>
        <th>Sticks</th>
        <th>Tubes</th>
        <th>Other*</th>
        <th>Bottles</th>
        <th>Blisters</th>
        <th>Sache</th>
        <th>Spray</th>
        <th>Syrings</th>
        <th>Single dose</th>
        <th>Ampouls</th>
        <th>Plastic vials</th>
        <th>Glass vials</th>
        <th>Tubes</th>
        <th>Suppositories</th>
        <th>Bundling Packs</th>
        <th>Hospital packs</th>
        <th>Other*</th>
    </tr>
    </thead>
    <tbody>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script type="text/javascript">
    $(document).ready(function(){
        $("#newrows").click(function(){
            var addcontrols = "<tr align="center">"
        addcontrols += "<td><input type="text"></td>"
        addcontrols += "<td><input type="text"></td>"
        addcontrols += "<td><input type="text"></td>"
        addcontrols += "<td><input type="text"></td>"
        addcontrols += "<td><input type="text"></td>"
        addcontrols += "<td><input type="checkbox" name=""></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
        addcontrols += "<td><input type="checkbox"></td>"
            addcontrols += "</tr>";
            $("table tbody").append(addcontrols);
        });
    });
    </script>
    </tbody>
    <tfoot>
        <tr>
            <td><input type="button" value="Add New Row" id="newrows"></td>
        </tr>
    </tfoot>
    <tr align="center">
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="checkbox" name=""></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
    </tr>
    <tr align="center">
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="text"></td>
        <td><input type="checkbox" name=""></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
        <td><input type="checkbox"></td>
    </tr>
</table>
"""

fd = st.markdown(html_table, unsafe_allow_html=True)


def parse_html_table(html_table):
    soup = BeautifulSoup(html_table, 'html.parser')
    table = soup.find('table')
    data = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if cells:
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)
    return data

def insert_into_oracle(conn, data):
    cursor = conn.cursor()
    for row in data:
        cursor.execute("INSERT INTO abc(a,b,c,d,ef,g,h,i,j,k,l,m) VALUES (:1, :2, ...)", row)
    conn.commit()
    cursor.close()
conn = connect_to_oracle('system','root','localhost',1521)
table_data = parse_html_table(html_table)
st.write(table_data)
# Insert data into Oracle table
insert_into_oracle(conn, table_data)

# Close Oracle connection
conn.close()
fd = st.markdown(html_table, unsafe_allow_html=True)
#b = st.button("click",on_click=newrows)

cursor = conn.cursor()

# conn = connect_to_oracle('system','root','localhost',1521)


# # Parse HTML table using BeautifulSoup
# soup = BeautifulSoup(html_table, 'html.parser')
# table = soup.find('table')
# rows = table.find_all('tr')
# #st.write(rows)
# # Create a cursor
# cursor = conn.cursor()

# # Iterate over rows and insert data into database
# for row in rows:
#     #st.write(row)
#     cells = row.find_all('td')
#     #st.write(cells)
#     if len(cells) > 0:
#         cmo = cells[0].text.strip()
#         manufacturing_site = cells[1].text.strip()
#         address = cells[0].text.strip()
#         city = cells[0].text.strip()
#         country = cells[0].text.strip()
#         # st.write(123,cmo)
#         # st.write(12,manufacturing_site,234)
#         # st.write(cmo,manufacturing_site,address,city,country)
#         # You need to extract other cell values similarly
        
#         # Insert data into your database table
#         cursor.execute("insert into tablee values({cmo},{manufacturing_site},{address},{city},{country})")
#         # cursor.execute("INSERT INTO your_table_name (cmo, manufacturing_site, address, city, country) VALUES (12y1, 122y, 23y, 2y4, 3y5)",(cmo, manufacturing_site, address, city, country))

# # Commit the transaction
# conn.commit()

# # Close the cursor and connection
# cursor.close()
# conn.close()

# # Inform the user about successful data insertion
# st.success("Data inserted into the database successfully.")







#conn = connect_to_oracle('system','root','localhost',1521)
#st.success('Connected to Oracle database!')
#cursor = conn.cursor()
# cursor.execute("SELECT * FROM student")
# df = pd.DataFrame(html_table)
# st.dataframe(df)


#st.dataframe(fd)
#st.markdown(html_table, unsafe_allow_html=True)
#st.markdown(check_box(), unsafe_allow_html=True)

# df = pd.read_html(html_table)[0] 
# st.dataframe(df)

# # # # Parse the HTML content
# # # soup = BeautifulSoup(html_table, 'html.parser')

# # # # Extract table data
# # # table = soup.find('table')
# # # rows = table.find_all('tr')

# # # # Extract column headers
# # # columns = [th.get_text().strip() for th in rows[0].find_all('th')]

# # # # Extract row data
# # # data = []
# # # for row in rows[1:]:
# # #     row_data = [td.get_text().strip() for td in row.find_all('td')]
# # #     data.append(row_data)

# # # # Create DataFrame
# # # df = pd.DataFrame(data, columns=columns)

# # # df = pd.DataFrame(html_table)
# # # st.dataframe(df)
# # # Display the modified HTML table



# def check_box(num_rows):
#     rows = ""
#     for _ in range(num_rows):
#         row = """
#             <tr>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#             </tr>
#         """
#         rows += row
#     return rows




# import streamlit as st
# import pandas as pd
# from bs4 import BeautifulSoup

# def check_box():
#     row ="""<tr>
#             function greet() {
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             <td><input type="checkbox"></td>
#             }
#         </tr>"""
#     return row

# # Define your HTML table
# html_table = """
# <table>
#     <tr>
#         <th rowspan="4">CMO</th>
#         <th rowspan="4">Manufacturing Site</th>
#         <th rowspan="4">Address</th>
#         <th rowspan="4">City</th>
#         <th rowspan="4">Country</th>
#         <th rowspan="3" colspan="11">Offered Services</th>
#         <th rowspan="3" colspan="13">Manufactured product types</th>
#         <th rowspan="3" colspan="6">Accreditations</th>
#         <th colspan="36">Bulk Production</th>
#         <th rowspan="2" colspan="6">Primary Packaging</th>
#         <th rowspan="3" colspan="14">Secondary Packaging</th>
#     </tr>
#     <tr>
#         <td colspan="13">Sterile</td>
#         <td colspan="23">Non-Sterile</td>				
#     </tr>
#     <tr>
#         <td colspan="9">Liquide</td>
#         <td colspan="4">Lyophilized</td>
#         <td colspan="6">Liquide</td>
#         <td colspan="11">Solid</td>
#         <td colspan="6">Semi-Solid</td>
#         <td rowspan="1" colspan="6">Solids/Semi-solids</td>
#     </tr>
#     <tr>
#         <td>GMP Warehouse</td>
#         <td>GDP Warehouse</td>
#         <td>QC Lab - Micro</td>
#         <td>QC Lab - Phisical/Chemical</td>
#         <td>QC Lab - Biological</td>
#         <td>QP Release</td>
#         <td>Development/ Pilot Production</td>
#         <td>API production</td>
#         <td>Bulk Production</td>
#         <td>Packaging</td>
#         <td>Other*</td>
#         <td>Biologics</td>
#         <td>Chemical</td>
#         <td>Herbal</td>
#         <td>Vaccines</td>
#         <td>Onco/ Cytotoxic</td>
#         <td>Hormons</td>
#         <td>Probiotics</td>
#         <td>Cosmetics</td>
#         <td>Beta Lactam</td>
#         <td>Food Supplements</td>
#         <td>VET - Veterinarian</td>
#         <td>Narcotics</td>
#         <td>Other*</td>
#         <td>EMA approval</td>
#         <td>FDA approval</td>
#         <td>ISO 13485</td>
#         <td>EU GMP </td>
#         <td>FSSC 22000</td>
#         <td>Other*</td>
#         <td>Vials</td>
#         <td>Syrings</td>
#         <td>Ampouls</td>
#         <td>Spray</td>
#         <td>Drops</td>
#         <td>Single dose</td>
#         <td>Bottles</td>
#         <td>Ophthalmic Ointments</td>
#         <td>Other*</td>
#         <td>Vials</td>
#         <td>Ampouls</td>
#         <td>Bottles</td>
#         <td>Other*</td>
#         <td>Drops</td>
#         <td>Bottles</td>
#         <td>Spray</td>
#         <td>Sache</td>
#         <td>Syrup</td>
#         <td>Other*</td>
#         <td>Tablets</td>
#         <td>Film Coated Tablets</td>
#         <td>Bi-/Multi-layer Tablets</td>
#         <td>Sugar Coated Tablets</td>
#         <td>Effervescent Tablets</td>
#         <td>ODT - Orally Disintegrating Tablets</td>
#         <td>Pallets</td>
#         <td>Powder</td>
#         <td>Capsules</td>
#         <td>Granulates</td>
#         <td>Other*</td>
#         <td>Ointment</td>
#         <td>Cream</td>
#         <td>Soft Capsules</td>
#         <td>Gels</td>
#         <td>Suppositories</td>
#         <td>Other*</td>
#         <td>Bottles</td>
#         <td>Blisters</td>
#         <td>Sache</td>
#         <td>Sticks</td>
#         <td>Tubes</td>
#         <td>Other*</td>
#         <td>Bottles</td>
#         <td>Blisters</td>
#         <td>Sache</td>
#         <td>Spray</td>
#         <td>Syrings</td>
#         <td>Single dose</td>
#         <td>Ampouls</td>
#         <td>Plastic vials</td>
#         <td>Glass vials</td>
#         <td>Tubes</td>
#         <td>Suppositories</td>
#         <td>Bundling Packs</td>
#         <td>Hospital packs</td>
#         <td>Other*</td>
#     </tr>
#     <tr>
#         <td></td>
#         <td></td>
#         <td></td>
#         <td></td>
#         <td></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#     </tr>
# </table>
# """


# # Parse the HTML table using BeautifulSoup
# soup = BeautifulSoup(html_table, 'html.parser')

# # Extract the content of the table
# rows = []
# for row in soup.find_all('tr'):
# #     rows.append([cell.text for cell in row.find_all(['th', 'td'])])

# # # Convert the table content into a DataFrame
# # df = pd.DataFrame(rows)

# # # Display the DataFrame
# # st.write(df)




# import streamlit as st
# import pandas as pd
# from bs4 import BeautifulSoup

# # Define your HTML table
# html_table = """
# <table>
#     <tr>
#         <th rowspan="4">CMO</th>
#         <th rowspan="4">Manufacturing Site</th>
#         <th rowspan="4">Address</th>
#         <th rowspan="4">City</th>
#         <th rowspan="4">Country</th>
#         <th rowspan="3" colspan="11">Offered Services</th>
#         <th rowspan="3" colspan="13">Manufactured product types</th>
#         <th rowspan="3" colspan="6">Accreditations</th>
#         <th colspan="36">Bulk Production</th>
#         <th rowspan="2" colspan="6">Primary Packaging</th>
#         <th rowspan="3" colspan="14">Secondary Packaging</th>
#     </tr>
#     <tr>
#         <td colspan="13">Sterile</td>
#         <td colspan="23">Non-Sterile</td>				
#     </tr>
#     <tr>
#         <td colspan="9">Liquide</td>
#         <td colspan="4">Lyophilized</td>
#         <td colspan="6">Liquide</td>
#         <td colspan="11">Solid</td>
#         <td colspan="6">Semi-Solid</td>
#         <td rowspan="1" colspan="6">Solids/Semi-solids</td>
#     </tr>
#     <tr>
#         <td>GMP Warehouse</td>
#         <td>GDP Warehouse</td>
#         <td>QC Lab - Micro</td>
#         <td>QC Lab - Phisical/Chemical</td>
#         <td>QC Lab - Biological</td>
#         <td>QP Release</td>
#         <td>Development/ Pilot Production</td>
#         <td>API production</td>
#         <td>Bulk Production</td>
#         <td>Packaging</td>
#         <td>Other*</td>
#         <td>Biologics</td>
#         <td>Chemical</td>
#         <td>Herbal</td>
#         <td>Vaccines</td>
#         <td>Onco/ Cytotoxic</td>
#         <td>Hormons</td>
#         <td>Probiotics</td>
#         <td>Cosmetics</td>
#         <td>Beta Lactam</td>
#         <td>Food Supplements</td>
#         <td>VET - Veterinarian</td>
#         <td>Narcotics</td>
#         <td>Other*</td>
#         <td>EMA approval</td>
#         <td>FDA approval</td>
#         <td>ISO 13485</td>
#         <td>EU GMP </td>
#         <td>FSSC 22000</td>
#         <td>Other*</td>
#         <td>Vials</td>
#         <td>Syrings</td>
#         <td>Ampouls</td>
#         <td>Spray</td>
#         <td>Drops</td>
#         <td>Single dose</td>
#         <td>Bottles</td>
#         <td>Ophthalmic Ointments</td>
#         <td>Other*</td>
#         <td>Vials</td>
#         <td>Ampouls</td>
#         <td>Bottles</td>
#         <td>Other*</td>
#         <td>Drops</td>
#         <td>Bottles</td>
#         <td>Spray</td>
#         <td>Sache</td>
#         <td>Syrup</td>
#         <td>Other*</td>
#         <td>Tablets</td>
#         <td>Film Coated Tablets</td>
#         <td>Bi-/Multi-layer Tablets</td>
#         <td>Sugar Coated Tablets</td>
#         <td>Effervescent Tablets</td>
#         <td>ODT - Orally Disintegrating Tablets</td>
#         <td>Pallets</td>
#         <td>Powder</td>
#         <td>Capsules</td>
#         <td>Granulates</td>
#         <td>Other*</td>
#         <td>Ointment</td>
#         <td>Cream</td>
#         <td>Soft Capsules</td>
#         <td>Gels</td>
#         <td>Suppositories</td>
#         <td>Other*</td>
#         <td>Bottles</td>
#         <td>Blisters</td>
#         <td>Sache</td>
#         <td>Sticks</td>
#         <td>Tubes</td>
#         <td>Other*</td>
#         <td>Bottles</td>
#         <td>Blisters</td>
#         <td>Sache</td>
#         <td>Spray</td>
#         <td>Syrings</td>
#         <td>Single dose</td>
#         <td>Ampouls</td>
#         <td>Plastic vials</td>
#         <td>Glass vials</td>
#         <td>Tubes</td>
#         <td>Suppositories</td>
#         <td>Bundling Packs</td>
#         <td>Hospital packs</td>
#         <td>Other*</td>
#     </tr>
#     <tr>
#         <td></td>
#         <td></td>
#         <td></td>
#         <td></td>
#         <td></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#     </tr>
# </table>
# """

# # Parse the HTML table using BeautifulSoup
# soup = BeautifulSoup(html_table, 'html.parser')

# # Extract the content of the table
# rows = []
# col_counts = []  # To keep track of column spans
# for row in soup.find_all('tr'):
#     row_data = []
#     for cell in row.find_all(['th', 'td']):
#         # Handle colspan attribute
#         colspan = int(cell.get('colspan', 1))
#         col_counts.extend([cell.text] * colspan)
#         row_data.append(cell.text)
#     rows.append(row_data)

# # Determine the maximum number of columns
# max_cols = max(len(row) for row in rows)

# # Fill in missing values for cells with colspan
# for row in rows:
#     while len(row) < max_cols:
#         row.append('')

# # Adjust the DataFrame columns using col_counts
# df = pd.DataFrame(rows, columns=col_counts[:max_cols])

# # Display the DataFrame
# st.write(df)



# import streamlit as st
# import pandas as pd
# from bs4 import BeautifulSoup
# import cx_Oracle as co

# def connect_to_oracle(username, password, host, port):
#     dsn = co.makedsn(host, port)
#     conn = co.connect(username, password, dsn)
#     return conn

# def check_box(num_rows):
#     rows = ""
#     for _ in range(num_rows):
#         row = """
#             <tr>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#                 <td><input type="checkbox"></td>
#             </tr>
#         """
#         rows += row
#     return rows

# # Define your HTML table
# html_table = """
# <table id="data-table">
#     <tr>
#         <th rowspan="4">CMO</th>
#         <th rowspan="4">Manufacturing Site</th>
#         <th rowspan="4">Address</th>
#         <th rowspan="4">City</th>
#         <th rowspan="4">Country</th>
#         <th rowspan="3" colspan="11">Offered Services</th>
#         <th rowspan="3" colspan="13">Manufactured product types</th>
#         <th rowspan="3" colspan="6">Accreditations</th>
#         <th colspan="36">Bulk Production</th>
#         <th rowspan="2" colspan="6">Primary Packaging</th>
#         <th rowspan="3" colspan="14">Secondary Packaging</th>
#     </tr>
#     <!-- Other rows here -->
# </table>
# """

# # Function to add a new row to the HTML table
# def add_new_row():
#     st.markdown("<script>addRow()</script>", unsafe_allow_html=True)

# # Add New Row button
# if st.button("Add New Row"):
#     add_new_row()

# # Display the HTML table
# fd = st.markdown(html_table, unsafe_allow_html=True)

# JavaScript to dynamically add a new row to the HTML table
# script = """
# <script>
# function addRow() {
#     var table = document.getElementById("data-table");
#     var newRow = table.insertRow(-1);
#     var cells = [];
#     for (var i = 0; i < table.rows[0].cells.length; i++) {
#         cells[i] = newRow.insertCell(i);
#         cells[i].innerHTML = '<input type="text">';
#     }
# }
# </script>
# """
# script = """
# <script>
# function addRow() {
#         <td><input type="text"></td>
#         <td><input type="text"></td>
#         <td><input type="text"></td>
#         <td><input type="text"></td>
#         <td><input type="text"></td>
#         <td><input type="checkbox" name=""></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#         <td><input type="checkbox"></td>
#     }
# }
# </script>
# """





# st.markdown(script, unsafe_allow_html=True)

# # Connection to Oracle
# conn = connect_to_oracle('system', 'root', 'localhost', 1521)
