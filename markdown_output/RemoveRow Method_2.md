       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RemoveRow Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5432.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SqlServerExport Class](topic5417.md) : RemoveRow Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_row_
    The row to be removed.

Glossary Item Box

Removes a row from the list of rows to be exported. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub RemoveRow( _
       ByVal _row_ As [DataExportRowDefinition](topic2635.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SqlServerExport](topic5417.md)
    Dim row As [DataExportRowDefinition](topic2635.md)
     
    instance.RemoveRow(row)  
  
C#|   
---|---  
      
    
    public void RemoveRow( 
       [DataExportRowDefinition](topic2635.md) _row_
    )  
  
#### Parameters

 _row_
    The row to be removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[SqlServerExport Members](topic5418.md)

©2024 DriveWorks Ltd. All Rights Reserved.
